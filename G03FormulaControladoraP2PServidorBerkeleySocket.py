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
        if data.count("|") < 4: # Se nao foram passados os 5 parametros, entao mensagem esta fora do padrao necessario.
            client.send("Mensagem com quantidade de parametros invalida: "+data)

        # Desencapsula a mensagem
        ModoPersistencia=data.split("|")[0]
        ValidacaoFormula=data.split("|")[1]
        comando=data.split("|")[2]
        if (data.split("|")[3] == None) or (data.split("|")[3] == "None"):
            codigo = None
        else:
            codigo=int(data.split("|")[3])
        formula=data.split("|")[4]

        # Debug :D
        print "ModoPersistencia:",ModoPersistencia
        print "ValidacaoFormula:",ValidacaoFormula
        print "comando:",comando
        print "codigo:",str(codigo)
        print "formula:",formula
        print "\n"

        if comando == "GET":
            client.send(recuperar_monolitica(ModoPersistencia, codigo))
        elif comando == "POST":
            client.send(incluir_monolitica(ModoPersistencia, formula))
        elif comando == "PUT":
            client.send(alterar_monolitica(ModoPersistencia, codigo, formula))
        elif comando == "DELETE":
            client.send(excluir_monolitica(ModoPersistencia, codigo))
        elif comando == "OPTIONS":
            client.send(listar_monolitica(ModoPersistencia))
        elif comando == "HEAD":
            client.send(limpar_monolitica(ModoPersistencia))
        elif comando == "TRACE":
            client.send(valida_monolitica(ModoPersistencia, ValidacaoFormula, codigo))
        elif comando == "CONNECT":
            client.send(executa_monolitica(ValidacaoFormula, formula))
        else:
            client.send("Comando invalido:"+comando)
    client.close()
