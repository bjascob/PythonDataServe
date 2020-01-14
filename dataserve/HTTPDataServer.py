#!/usr/bin/python3
from abc import ABC, abstractmethod
import logging
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from .http_utils import to_binary, from_binary, CONTENT_TYPE

logger = logging.getLogger(__name__)


# Run the server
def run_http_server(port, data_handler):
    server_address = ('', port)
    httpd = HTTPServer(server_address, data_handler)
    print('Serving data on port %d. Press <ctrl>-c to stop.' % port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('exiting')
        httpd.server_close()


# Base class for user defined handlers
class HTTPDataHandler(ABC, BaseHTTPRequestHandler):
    # Header for OK response
    def form_ok_header(self, dtype):
        self.send_response(200)     # code 200 = OK
        self.send_header(CONTENT_TYPE, dtype)
        self.end_headers()

    # Header for bad request response
    def form_bad_header(self):
        self.send_response(400)     # Bad request
        self.end_headers()

    # Extract the resource path
    # When sending, if 'params' are added, they show-up in self.path so
    # use urlparse to clean this up.
    # ie.. self.path = /test1?address=12
    def get_resource(self):
        result = urlparse(self.path)
        return result.path

    # The HEAD method asks for a response identical to that of a GET request,
    # but without the response body.
    def do_HEAD(self):
        self.form_ok_header()

    # The PUT method replaces all current representations of the target
    # resource with the request payload.
    def do_PUT(self):
        # Read the message
        length = int(self.headers.get('content-length', -1))
        if length < 0:
            logger.warning('No specified content-length')
            self.form_bad_header()
            return
        data = self.rfile.read(length)
        # Handle different content types
        ctype = self.headers.get(CONTENT_TYPE, '')
        payload_in = from_binary(data, ctype)
        if payload_in is None:
            logger.warning('Invalid content type: %s' % ctype)
            self.form_bad_header()
            return
        # Run the handler, if one exists
        resource = self.get_resource()
        response = self.handle_request(resource, payload_in)
        if response is None:
            logger.warning('Unhandled resource path: %s' % resource)
            self.form_bad_header()
            return
        # return the response
        payload_out, dtype = to_binary(response)
        self.form_ok_header(dtype)
        self.wfile.write(payload_out)

    # Silence the accepted (success) message logging. Errors are still logged
    def log_request(self, format, *args):
        return

    #######################################################
    #### Define these in the derived class
    #######################################################

    # Given a resource path, return some data
    @abstractmethod
    def handle_request(self, resource, payload):
        logger.warning('Request received but no handler is implemented.')
