#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Cliente FTP
# Descricao: Responsavel por encapusular os parametros e enviar ao servidor FTP
#

import ftplib
#import os
import string
import warnings
import socket

msg = ""

def __imprime_mensagem(mensagem):
    global msg
    msg = msg + mensagem + "\n"

def __enviar_comando(mensagem):
    global msg
    msg = ""
    p2p_server_host = "127.0.0.1"
    p2p_server_port = 21
    p2p_timeout=10
    p2p_usuario="dummy"
    p2p_senha="dummy"

    try:
        ftp = ftplib.FTP()
        ftp.connect(host=p2p_server_host, port=p2p_server_port)
        ftp.login(p2p_usuario, p2p_senha)
        data = ftp.retrlines("LIST |"+mensagem,__imprime_mensagem)
        ftp.quit()
        return msg
    except:
        return "Erro ao conectar via FTP"

def envia_comando_ftp(ModoPersistencia,ValidacaoFormula,comando,codigo,formula):
    # Encapsula mensagem separando os campos com pipes, antes de enviar.
    if formula == None:
        formula = ""
    mensagem = ModoPersistencia+"|"+ValidacaoFormula+"|"+comando+"|"+str(codigo)+"|"+formula
    return __enviar_comando(mensagem)

#print envia_comando_ftp("Textual","eval","GET",1,"1 + 2")
