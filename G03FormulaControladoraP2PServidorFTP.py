#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Servidor FTP
# Descricao: Responsavel por desencapusular a mensagem e chamar a funcao apropriada na
#            camada de controle.
#

import os
#import socket

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

class MeusHandler(FTPHandler):
    def on_connect(self):
        FTPHandler.on_connect();
    def on_disconnect(self):
        FTPHandler.on_disconnect();
    def on_login(self, username):
        FTPHandler.on_login(username);
    def on_logout(self, username):
        FTPHandler.on_logout(username);
    def on_file_sent(self, file):
        print "on_file_sent",file
        FTPHandler.on_file_sent(file);
        # do something when a file has been sent
        pass
    def on_file_received(self, file):
        print "on_file_received",file
        FTPHandler.file_received(file);
    def on_incomplete_file_sent(self, file):
        FTPHandler.on_incomplete_file_sent(file);
    def on_incomplete_file_received(self, file):
        FTPHandler.on_incomplete_file_received(file);
        os.remove(file)

p2p_server_port = 8081
p2p_usuario="dummy"
p2p_senha="dummy"

authorizer = DummyAuthorizer()
authorizer.add_user(p2p_usuario, p2p_senha, os.getcwd(), perm='elradfmw')
authorizer.add_anonymous(os.getcwd())
handler = MeusHandler
handler.authorizer = authorizer

# Specify a masquerade address and the range of ports to use for
# passive connections.  Decomment in case you're behind a NAT.
if (p2p_ipnat != ""):
    handler.masquerade_address = "" #ipnat
    handler.passive_ports = range(60000, 65535)

# Instantiate FTP server class and listen on <localhost>:2121
address = ("127.0.0.1", p2p_server_port)
server = FTPServer(address, handler)

# set a limit for connections
server.max_cons = 256
server.max_cons_per_ip = 5

# start ftp server
server.serve_forever()
