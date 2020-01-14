#!/usr/bin/python3
import os
import sys
import time
# put '../..' in the lib search path so it can find this library
sys.path.insert(0, '..' + os.sep + '..')
from dataserve import get_proxy_class


def time_it(function, *args):
    st = time.time()
    ret = function(*args)
    et = time.time()
    return et-st, ret


if __name__ == '__main__':
    st = time.time()
    client = get_proxy_class('MyProxyClass', port=5000)
    print('Getting client proxy took %d ms' % (1e3*(time.time()-st)))
    client = get_proxy_class('MyProxyClass', port=5000)

    dur, _ = time_it(client.say_hello)
    print('First simple call took %d ms' % (1e3*dur))

    dur, data = time_it(client.get_xdata)
    print(data)
    print('Getting xdata took %d ms' % (1e3*dur))

    dur, data = time_it(client.get_ydata)
    print(data)
    print('Getting ydata took %d ms' % (1e3*dur))

    dur, data = time_it(client.get_zdata)
    print(data.shape)
    print('Getting zdata took %d ms' % (1e3*dur))

    dur, data = time_it(client.get_zdata, 5)
    print(data)
    print('Getting one zdata value took %d ms' % (1e3*dur))

    try:
        xdata = client.xdata
    except AttributeError:
        print('Class data not available on client side')
