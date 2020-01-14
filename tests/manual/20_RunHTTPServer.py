#!/usr/bin/python3
import os
import sys
# put '../..' in the lib search path so it can find this library
sys.path.insert(0, '..' + os.sep + '..')
from dataserve import HTTPDataHandler, run_http_server

# Load some test data to serve
xdata = {'list':[1, 2, 3, 4], 'other':5}
with open('image.bmp', 'rb') as f:
    zdata = f.read()


class MyDataHandler(HTTPDataHandler):
    def handle_request(self, resource, payload):
        if resource == '/xdata':
            out_data = xdata.copy()
            out_data.update(payload)
            return out_data
        elif resource == '/ydata':
            return payload + ' with server appended text'
        elif resource == '/zdata':
            return zdata
        return None


if __name__ == "__main__":
    run_http_server(5001, MyDataHandler)
