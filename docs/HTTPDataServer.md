# HTTP Data Server and Client

The HTTP Server and Client pass data back and forth via http PUT requests.  The requests are handled by a user defined class, which is derived from `HTTPDataHandler`.  You can pass `strings`, or any json-able types such as `lists` or `dicts`.  Raw `bytearray` data can also passed which means images or anything that can be serialized can be passed from client to server and server to client.

Because this class does not do `pickling`, it is generally faster than the ProxyServer but it is not setup to pass generic python objects.  If you want to pass full objects, you'll need to first `pickle` the data yourself and then pass the resulting ``bytearray`` to the `send` method.


## Example
```
# In the Server File
from dataserve import HTTPDataHandler, run_http_server

xdata = [1, 2, 3]

class MyDataHandler(HTTPDataHandler):
    def handle_request(self, resource, payload):
        if resource == '/xdata':
            global xdata
            return xdata + payload
        elif resource == '/ydata':
            return 2
        return None

run_http_server(5001, MyDataHandler)


# In the Client File
from dataserve import HTTPDataClient

client = HTTPDataClient(port=5001)
ret = client.send('/xdata', [4, 5, 6])
ret = client.send('/ydata')
```
See more complete examples in the repository's tests/manual directory: **[RunHTTPServer](https://bjascob/pythondataserve/tests/manual/20_RunHTTPServer.py)** and **[TestHTTPServer](https://bjascob/pythondataserve/tests/manual/22_TestHTTPServer.py)**.

## HTTPDataHandler Class
A user defined class must derive from **HTTPDataHandler**.  The only required method is **handle_request**
```
handle_request(self, resource, payload)
```
Arguments:
* `resource` is the url resource that the client will specify.
* `payload` is the data that was pass in at the client.

Return value: The method should return a `string`, json-able type or `bytearray`.  The type of data will automatically be detected by the system.  The allowed data types are the same as what's passed in at the client.  A return of `None` will indicate that the url resource is not handled.

## Run server function
**run_http_server**
```
run_http_server(port, data_handler)
```
Arguments:
* `port` is the port to serve the data on
* `data_handler` is a class definition for the user-defined data handler class.  This must derive from HTTPDataHandler
This method blocks until a keyboard interrupt is received.


## HTTPClient Class
This class encapsulates the client functionality.

**init**
```
__init__(self, port, address='http://localhost:')
```
Arguments:
* `port` specifies the port the server is serving data on
* `address` is optional.  Supply the http address if connecting to a non-local computer.  The address must end in a colon.

**send**
```
send(self, resource, payload=None)
```
Arguments:
* `resource` the resource url to sent the request to
* `payload` is an optional parameter.  It may be a `string`, json-able type or `bytearray`.  Note that the type of data will automatically be detected by the system.


## Notes on HTTP
The HTTPDataServer only utilizes the PUT request and not the full list (GET, POST, DELETE, ...). This is done for simplicity but is not strictly correct according to how the normal request methods are defined. The PUT command allows sending and receiving data, meaning it allows for a full remote procedure-call type of function and thus should be usable for most use cases.
