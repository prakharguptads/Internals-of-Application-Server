from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import sys
addr = ('127.0.0.1',2121)
authorizer = DummyAuthorizer()
authorizer.add_user('admin','adminpass',sys.argv[1],perm='elradfmw')
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(addr,handler)
server.serve_forever()
