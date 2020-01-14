import logging
import inspect
from multiprocessing.managers import BaseManager, SyncManager

logger = logging.getLogger(__name__)


# Run the proxy server defined by the proxy_class
def run_proxy_server(proxy_class, port):
    if not inspect.isclass(proxy_class):
        logger.error('Supplied proxy_class is not an un-instantiated class definition')
    proxy_name = proxy_class.__name__
    authkey = proxy_name.encode()
    class myManager(SyncManager): pass
    myManager.register(proxy_name, proxy_class)
    mgr = myManager(address=('', port), authkey=authkey)
    server = mgr.get_server()
    # Start the server
    print('Serving data on port %d. Press <ctrl>-c to stop.' % port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('exiting')


# Return an instance of the proxy class
def get_proxy_class(proxy_name, port, host='localhost'):
    class myManager(BaseManager): pass
    myManager.register(proxy_name)
    authkey = proxy_name.encode()
    mgr = myManager(address=(host, port), authkey=authkey)
    try:
        mgr.connect()
    except ConnectionRefusedError:
        logger.error('Can not connect to server at %s:%s' % (host, port))
        return None
    class_ = getattr(mgr, proxy_name, None)
    if class_ is None:
        logger.error('Server does not have a proxy class: %s' % proxy_name)
        return None
    return class_()
