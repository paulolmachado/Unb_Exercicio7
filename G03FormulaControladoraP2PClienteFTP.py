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

def __enviar_comando(mensagem):
    p2p_server_host = "127.0.0.1"
    p2p_server_port = 8081
    p2p_timeout=10
    p2p_usuario="dummy"
    p2p_senha="dummy"

    try:
        ftp = ftplib.FTP()
        ftp.connect(host=p2p_server_host, port=p2p_server_port, timeout=p2p_timeout)
        ftp.login(p2p_usuario, p2p_senha)
        data = ftp.retrlines("RETR " + mensagem)
        ftp.quit()
        return data
    except:
        return "Erro ao conectar via FTP"

def envia_comando_berkeley(ModoPersistencia,ValidacaoFormula,comando,codigo,formula):
    # Encapsula mensagem separando os campos com pipes, antes de enviar.
    if formula == None:
        formula = ""
    mensagem = ModoPersistencia+"|"+ValidacaoFormula+"|"+comando+"|"+str(codigo)+"|"+formula
    return __enviar_comando(mensagem)
