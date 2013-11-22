#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Servidor FTP
# Descricao: Responsavel por desencapusular a mensagem e chamar a funcao apropriada na
#            camada de controle.
#

import sys
import G03FormulaControladoraMonolitica

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.handlers import BufferedIteratorProducer
from pyftpdlib.servers import FTPServer

class MyHandler(FTPHandler):
    def ftp_LIST(self, path):
        # Valida se a mensagem tem os 6 parametros.
        path = path.encode('ascii','ignore')
        if path.count("|") < 5: # Se nao foram passados os 5 parametros, entao mensagem esta fora do padrao necessario.
            retorno = "Mensagem com quantidade de parametros invalida: "+path
        else:
            # Desencapsula a mensagem
            Caminho = path.split("|")[0] # Caminho (path) que sempre vira por conta do protocolo FTP
            ModoPersistencia = path.split("|")[1]
            ValidacaoFormula = path.split("|")[2]
            comando = path.split("|")[3]
            if (path.split("|")[4] == None) or (path.split("|")[4] == "None"):
                codigo = None
            else:
                codigo = int(path.split("|")[4])
            formula = path.split("|")[5]

            # Debug :D
            print "ModoPersistencia:",ModoPersistencia
            print "ValidacaoFormula:",ValidacaoFormula
            print "comando:",comando
            print "codigo:",codigo
            print "formula:",formula
            print "\n"

            if comando == "GET":
                retorno = G03FormulaControladoraMonolitica.recuperar_monolitica(ModoPersistencia, codigo)
            elif comando == "POST":
                retorno = G03FormulaControladoraMonolitica.incluir_monolitica(ModoPersistencia, formula)
            elif comando == "PUT":
                retorno = G03FormulaControladoraMonolitica.alterar_monolitica(ModoPersistencia, codigo, formula)
            elif comando == "DELETE":
                retorno = G03FormulaControladoraMonolitica.excluir_monolitica(ModoPersistencia, codigo)
            elif comando == "OPTIONS":
                retorno = G03FormulaControladoraMonolitica.listar_monolitica(ModoPersistencia)
            elif comando == "HEAD":
                retorno = G03FormulaControladoraMonolitica.limpar_monolitica(ModoPersistencia)
            elif comando == "TRACE":
                retorno = G03FormulaControladoraMonolitica.valida_monolitica(ModoPersistencia, ValidacaoFormula, codigo)
            elif comando == "CONNECT":
                retorno = G03FormulaControladoraMonolitica.executa_monolitica(ValidacaoFormula, formula)
            else:
                retorno = "Comando invalido:"+comando

        producer = BufferedIteratorProducer(n for n in [retorno.encode('ascii','ignore')+"\n"])
        self.push_dtp_data(producer, isproducer=True, cmd="LIST")
        return path

p2p_server_port = 21
p2p_usuario="dummy"
p2p_senha="dummy"

authorizer = DummyAuthorizer()
authorizer.add_user(p2p_usuario, p2p_senha, "/", perm="elradfmw")
authorizer.add_anonymous("/")

handler =  MyHandler #FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", p2p_server_port), handler)

# set a limit for connections
server.max_cons = 256
server.max_cons_per_ip = 5

# start ftp server
server.serve_forever()
