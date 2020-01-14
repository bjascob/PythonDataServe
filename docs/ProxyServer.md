# Proxy Server and Client

The Proxy Client makes calls into the server via a proxy class that the user defines.  Python object data is passed back to the client via `pickling`.

There are a few things to note about this process...
* All processing defined in the proxy class happens on the server side
* Whenever you connect (via `get_proxy_class`) the proxy is instantiated on the server.  This means all data is passed through the proxy but is generally not part of the proxy (ie... global xdata, not self.xdata).
* Any object that can be pickled can but sent but there are some limits such as pickled data can't be larger than 4GB


## Example

```
# In the Server File
from dataserve import run_proxy_server
xdata = 1

class MyProxyClass(object):
     def get_xdata(self, val):
         global xdata
         return xdata + val
     def get_ydata(self):
         return 2

run_proxy_server(MyProxyClass, port=5000)


# In the Client File
from dataserve import get_proxy_class

client = get_proxy_class('MyProxyClass', port=5000)
ret_val = client.get_xdata(val=5)
ret_val = client.get_ydata()
```

See more complete examples in the repository's tests/manual directory: **[RunProxyServer](https://bjascob/pythondataserve/tests/manual/10_RunProxyServer.py)** and **[TestProxyServer](https://bjascob/pythondataserve/tests/manual/12_TestProxyServer.py)**.

## Methods
**run_proxy_server**
```
run_proxy_server(proxy_class, port)
```
This function starts the server.

Arguments:
* `proxy_class` is a class definition, not an instantiated object.
* `port` is the port to serve the data on

This method blocks until a keyboard interrupt is received.

**get_proxy_class**
```
get_proxy_class(proxy_name, port, host='localhost')
```
This function retrieves a reference to the proxy.

Arguments:
* `proxy_name` must be the same name as the user defined class
* `port` needs to be the same port used in the server.
* `host` default to localhost.  Supply an ip address if connecting to a remote computer.

Returns: an instantiated proxy object allowing the user access to any of the methods they've defined.
