#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Servidor FTP
# Descricao: Responsavel por desencapusular a mensagem e chamar a funcao apropriada na
#            camada de controle.
#

import os
import socket

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler

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
        FTPHandler.on_file_sent(file);
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        FTPHandler.file_received(file);
        print file

    def on_incomplete_file_sent(self, file):
        FTPHandler.on_incomplete_file_sent(file);

    def on_incomplete_file_received(self, file):
        FTPHandler.on_incomplete_file_received(file);
        os.remove(file)

def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user('dummy', 'dummy', os.getcwd(), perm='elradfmwM')
    authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = MeusHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "Conexao P2P via FTP."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    if (p2p_ipnat != ""):
        handler.masquerade_address = "" #ipnat
        handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on <localhost>:2121
    address = ("127.0.0.1", p2p_porta)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()
