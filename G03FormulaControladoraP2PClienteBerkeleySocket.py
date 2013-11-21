#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Cliente Berkeley Socket
# Descricao: Responsavel por encapusular os parametros e enviar ao servidor Berkeley Socket.
#

import socket

def __enviar_comando(mensagem):
    p2p_server_host = "127.0.0.1"
    p2p_server_port = 8080
    p2p_msg_size = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((p2p_server_host,p2p_server_port))

    s.send(mensagem) # Envia o comando.
    data = s.recv(p2p_msg_size) # Obtem o resultado do comando
    #print "Dados recebidos:",data

    s.close()
    return data

def envia_comando_berkeley(ModoPersistencia,ValidacaoFormula,comando,codigo,formula):
    # Encapsula mensagem separando os campos com pipes, antes de enviar.
    if formula == None:
        formula = ""
    mensagem = ModoPersistencia+"|"+ValidacaoFormula+"|"+comando+"|"+str(codigo)+"|"+formula
    return __enviar_comando(mensagem)
