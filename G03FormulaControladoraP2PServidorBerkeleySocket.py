#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Servidor Berkeley Socket
# Descricao: Recebe as mensagens do cliente, trata a mensagem e chama a funcao
#            apropriada de G03FormulaControladoraMonolitica, devolvendo o
#            resultado pela conexao.
#

from G03FormulaControladoraMonolitica import *
import socket

p2p_server_host = "127.0.0.1"
p2p_server_port = 8080
p2p_backlog = 5 # Quantidade de conexões na fila.
p2p_msg_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((p2p_server_host,p2p_server_port))
s.listen(p2p_backlog)
while 1:
    client, address = s.accept()
    data = client.recv(p2p_msg_size)
    if data:
        print "Dado recebido:",data
        if data.find("|") < 1: # Se nao foi passado a primeira parte da mensagem com o tipo de persistencia ...
            ModoPersistencia = "Textual" # ... entao assume a persistencia "Textual".
            Mensagem = data
        else:
            ModoPersistencia = data.split("|",1)[0]
            Mensagem = data.split("|",1)[1]
        print "ModoPersistencia:",ModoPersistencia
        print "Mensagem:",Mensagem

        # Trata as mensagens
        comando = Mensagem.split(" ",1)[0]
        parametro1 = Mensagem.split(" ",1)[1]
        try:
            parametro2 = Mensagem.split(" ",2)[2]
        except:
            parametro2 = None

        if comando == "GET":
            resultado = recuperar_monolitica(ModoPersistencia, int(parametro1))
            if resultado == None:
                client.send("")
            else:
                client.send(resultado)
        elif comando == "POST":
            client.send(incluir_monolitica(ModoPersistencia, parametro1))
        elif comando == "PUT":
            client.send(alterar_monolitica(ModoPersistencia, int(parametro1), parametro2))
        elif comando == "DELETE":
            client.send(excluir_monolitica(ModoPersistencia, int(parametro1)))
        elif comando == "OPTIONS":
            client.send(listar_monolitica(ModoPersistencia))
        elif comando == "HEAD":
            client.send(limpar_monolitica(ModoPersistencia))
        else:
            client.send("Comando invalido:"+Mensagem)
    client.close()
