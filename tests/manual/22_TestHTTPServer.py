#!/usr/bin/python3
import os
import sys
import time
# put '../..' in the lib search path so it can find this library
sys.path.insert(0, '..' + os.sep + '..')
from dataserve import HTTPDataClient


if __name__ == '__main__':
    client = HTTPDataClient(port=5001)

    st = time.time()
    resp = client.send('/xdata', {'list':[6, 7, 8, 9]})
    dur = time.time() - st
    print('Send returned: %s in %d us' % (resp, 1e6*dur))

    st = time.time()
    resp = client.send('/ydata', 'client message')
    dur = time.time() - st
    print('Send returned: %s in %d us' % (resp, 1e6*dur))

    st = time.time()
    resp = client.send('/zdata', None)
    dur = time.time() - st
    print('Send returned a %s: in %d us' % (type(resp), 1e6*dur))
    if 0:
        fn = 'img_out.bmp'
        with open(fn, 'wb') as f:
            f.write(data)
            print('Data written to', fn)
