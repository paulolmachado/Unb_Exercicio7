#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Interface de usuario.
# Descricao: basicamente recebe o comando do usuario e submente a camada de Visao, e deixa
#            por conta desta ultima o tratamento do comando, com excecao do comando QUIT
#            que indica a opcao de sair do programa.
#            Teoricamente, essa camada de "Interface do Usuario" podera ser substituido por
#            qualquer outra, como por exemplo um browser web. Por isso, foi mantida a sintaxe dos
#            comandos em uma unica linha como "GET 1" ou "POST (1 + 2)"
#

from G03FormulaVisao import *

opcao = ""

while opcao.upper() != "QUIT":

    opcao = raw_input("Entre com a opcao: ")

    if opcao.upper() != "QUIT":        # Se for diferente de QUIT,
        print VisaoEmiteComando(opcao) # envia comando para camada de Visao.

print "Fim do programa"
