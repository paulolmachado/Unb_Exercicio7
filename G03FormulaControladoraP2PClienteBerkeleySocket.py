#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Cliente Berkeley Socket
# Descricao: Responsavel por remontar e enviar o comando ao server Berkeley Socket.
#

import socket

def __enviar_comando(ModoPersistencia, comando):
    p2p_server_host = "127.0.0.1"
    p2p_server_port = 8080
    p2p_msg_size = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((p2p_server_host,p2p_server_port))

    s.send(ModoPersistencia+"|"+comando) # Envia o comando.
    data = s.recv(p2p_msg_size) # Obtem o resultado do comando
    print "Dados recebidos:",data

    s.close()
    return data

def recuperar_berkeley(ModoPersistencia, codigo):
    return __enviar_comando(ModoPersistencia, "GET "+str(codigo))

def incluir_berkeley(ModoPersistencia, formula):
    return (ModoPersistencia,"POST "+formula) # Configura modo de persistencia

def alterar_berkeley(ModoPersistencia, codigo, formula):
    return __enviar_comando(ModoPersistencia,"PUT "+str(codigo)+" "+formula) # Configura modo de persistencia

def excluir_berkeley(ModoPersistencia, formula):
    return __enviar_comando(ModoPersistencia,"DELETE "+formula) # Configura modo de persistencia

def listar_berkeley(ModoPersistencia):
    return __enviar_comando(ModoPersistencia,"OPTIONS") # Configura modo de persistencia

def limpar_berkeley(ModoPersistencia):
    return __enviar_comando(ModoPersistencia,"HEAD") # Configura modo de persistencia
