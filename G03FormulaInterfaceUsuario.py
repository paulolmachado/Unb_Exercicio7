#!/usr/bin/env python
#
# Modulo de Interface de usuario.
# Descricao: basicamente recebe o comando do usuario e submente a camada de Visao, e deixa
#            por conta desta ultima o tratamento do comando, com excecao dos comandos QUIT e HELP
#            que indica a opcao de sair do programa ou mostrar a sintaxe dos comandos possiveis,
#            respectivamente.
#            Teoricamente, essa camada de "Interface do Usuario" podera ser substituido por
#            qualquer outra, como por exemplo, um browser web. Por isso, foi mantida a sintaxe dos
#            comandos em uma unica linha como por exemplo "GET 1" ou "POST (1 + 2)"
# 

from G03FormulaVisao import *
import sys

opcao = ""

while opcao.upper() != "QUIT":
    
    opcao = raw_input("Entre com a opcao: ")

    if opcao.upper() != "QUIT":
        print VisaoEmiteComando(opcao)
        
print "Fim do programa"
