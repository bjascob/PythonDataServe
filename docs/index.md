PythonDataServe

**A module for serving up python data in a stand-alone process.**


## About
PythonDataServe is a simple library that allows you to serve data from a different python process.  This eliminates the need to load large data files every time you want to run your program.

The library includes a very simple HTTP server for basic data types and a Proxy server for python objects.  Both servers implement a similar methodology, allowing the user to define functions on the server side which the client can call with a data payload to and get a return response.  This is a remote-procedure-call type of implementation which also makes the library an excellent tool for doing multiprocessing across computers.

There library also contains a DataContainer utility class to encapsulate pickling, gzipping, loading and saving functionality.  This simplifies some common data operations.

The only external requirement is the very common, "requests" library.


## Documentation
For the latest documentation, see **[ReadTheDocs](https://xxxx.readthedocs.io/en/latest/)**.  Alternatively, you can view the markup files directly in the __*docs*__ folder of this project.

You can see example implementations in the __*tests*__ folder.
