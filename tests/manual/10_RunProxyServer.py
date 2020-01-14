#!/usr/bin/python3
import os
import sys
import numpy
# put '../..' in the lib search path so it can find this library
sys.path.insert(0, '..' + os.sep + '..')
from dataserve import run_proxy_server


print('Initializing global data to be served')
xdata = {'list':[1, 2, 3, 4], 'other':5}

class MyProxyClass(object):
    print('Initializing class data to be served')
    ydata = {'list':[6, 7, 8, 9], 'other':10}
    # Note: can not serialize objects larger than 4GB
    zdata = numpy.zeros(shape=(int(1e8)), dtype='float64')
    def __init__(self):
        print('ProxyClass init happens on the server side every time the client connects')

    def say_hello(self):
        print('Methods process on the server side')

    def get_xdata(self):
        global xdata
        return xdata

    def get_ydata(self):
        return self.ydata

    def get_zdata(self, index=None):
        if index is not None:
            return self.zdata[index]
        else:
            return self.zdata


if __name__ == '__main__':
    run_proxy_server(MyProxyClass, port=5000)
