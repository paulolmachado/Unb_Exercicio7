

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

p2p_server_port = 8081
p2p_usuario="dummy"
p2p_senha="dummy"

class CunstomHandler(FTPHandler):
    #def on_connect(self):
    #    FTPHandler.on_connect();
    #def on_disconnect(self):
    #    FTPHandler.on_disconnect();
    #def on_login(self, username):
    #    FTPHandler.on_login(username);
    #def on_logout(self, username):
    #    FTPHandler.on_logout(username);
    def on_file_sent(self, file):
        print "on_file_sent",file
        FTPHandler.on_file_sent(file);
        # do something when a file has been sent
        pass
##    def on_file_received(self, file):
##        print "on_file_received",file
##        FTPHandler.file_received(file);
##    def on_incomplete_file_sent(self, file):
##        FTPHandler.on_incomplete_file_sent(file);
##    def on_incomplete_file_received(self, file):
##        FTPHandler.on_incomplete_file_received(file);
##        os.remove(file)


authorizer = DummyAuthorizer()
authorizer.add_user(p2p_usuario, p2p_senha, "/", perm="elradfmw")
authorizer.add_anonymous("/")

handler = CunstomHandler
handler.authorizer = authorizer

server = FTPServer.FTPServer(("127.0.0.1", p2p_server_port), handler)

# set a limit for connections
server.max_cons = 256
server.max_cons_per_ip = 5

# start ftp server
server.serve_forever()
