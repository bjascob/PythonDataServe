#!/usr/bin/python3
import requests
import logging
from .http_utils import to_binary, from_binary, CONTENT_TYPE

logger = logging.getLogger(__name__)


class HTTPDataClient(object):
    def __init__(self, port, address='http://localhost:'):
        self.url = address + str(port)

    # Execute a PUT request
    def send(self, resource, payload=None):
        if not resource.startswith('/'):
            resource = '/' + resource
        payload_out, dtype = to_binary(payload)
        try:
            r = requests.put(url=self.url + resource, data=payload_out,
                             headers={CONTENT_TYPE:dtype})
        except requests.exceptions.RequestException:
            logger.error('No connection on: %s' % self.url)
            return None
        return self.form_response(r)

    def form_response(self, r):
        if not r.ok:
            return None
        ctype = r.headers.get(CONTENT_TYPE, None)
        if ctype is None:
            logger.error('Content-Type not specified in header: %s' % r.headers)
            return None
        payload = from_binary(r.content, ctype)
        if payload is None:
            logger.error('Unhandled Content-Type: %s', ctype)
        return payload
