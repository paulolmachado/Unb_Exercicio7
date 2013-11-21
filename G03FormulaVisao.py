#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Visao
# Descricao: Recebe os comandos GET, POST, PUT, DELETE, OPTIONS, HEAD, TRACE, CONNECT, PERSIST, CONTROL e VALID
#            acompanhados dos respectivos parametros e chama a funcao para processamento na camada da Controladora.
#            Junto com a chamada das funcoes na Controladora, tambem processa e informa qual o modo de
#            persistencia (Textual ou SGBD), qual o tipo de Controladora (Monolitica, P2P com Berkeley Socket
#            ou FTP) e também o tipo de validação de fórmula (eval ou arvore).
#

from G03FormulaControladora import *

opcoes = ["GET","POST","PUT","DELETE","OPTIONS","HEAD","TRACE","CONNECT","PERSIST","CONTROL","VALID"]
TipoControladora = "Monolitica" # Valores possiveis: Monolitica | Berkeley | FTP
ModoPersistencia = "Textual" # Valores possiveis: Textual | SGBD
ValidacaoFormula = "eval" # Valores possiveis: eval | arvore

def VisaoEmiteComando(opcao):
    global opcoes
    global TipoControladora
    global ModoPersistencia
    global ValidacaoFormula

    argumentos = opcao.split() # Separa argumentos
    comando = argumentos[0].upper() # Obtem primeiro argumento: comando

    # Se o comando for HELP ou for um comando fora da lista, entao mostra sintaxe geral.
    if (comando == "HELP") or (not any(comando in s for s in opcoes)):
        return """
            Sintaxe:
                GET <codigo>           # Recuperar
                POST <formula>         # Incluir
                PUT <codigo> <formula> # Alterar
                DELETE <codigo>        # Excluir
                OPTIONS                # Listar todas
                HEAD                   # Limpar todas
                TRACE <codigo>         # Executar formula da base
                CONNECT <formula>      # Executar formula
                PERSIST <tipo>         # Tipo de Persistencia (Textual ou SGBD) - Default: Textual
                CONTROL <tipo>         # Tipo de Controladora (Monolitica ou Berkeley ou FTP) - Defaul: Monolitica
                VALID <tipo>           # Tipo de validacao de formula (eval ou arvore) - Default: eval
                QUIT                   # Sai do programa (valido apenas na camada de interface do usuario)
        """

    # Define os parametros codigo (posicao da formula na base) e formula (formula propriamente dita)
    if comando == "GET":
        codigo = int(argumentos[1])
        formula = None

    elif comando == "POST":
        codigo = None
        formula = opcao[len(comando)+1:]

    elif comando == "PUT":
        codigo = int(argumentos[1])
        formula = opcao[len(comando)+len(argumentos[1])+2:]

    elif comando == "DELETE":
        codigo = int(argumentos[1])
        formula = None

    elif comando == "OPTIONS":
        codigo = None
        formula = None

    elif comando == "HEAD":
        codigo = None
        formula = None

    elif comando == "TRACE":
        codigo = int(argumentos[1])
        formula = None

    elif comando == "CONNECT":
        codigo = None
        formula = opcao[len(comando)+1:]

    elif comando == "PERSIST":
        if (argumentos[1] != "Textual") and (argumentos[1] != "SGBD"):
            return "Tipo de parametro invalido. Esperado Textual ou SGBD. Recebido:"+argumentos[1]
        else:
            ModoPersistencia = argumentos[1]
            return "Tipo de pesistencia alterada para "+ModoPersistencia

    elif comando == "CONTROL":
        if (argumentos[1] != "Monolitica") and (argumentos[1] != "Berkeley") and (argumentos[1] != "FTP"):
            return "Tipo de parametro invalido. Esperado Monolitica ou Berkeley ou FTP. Recebido:"+argumentos[1]
        else:
            TipoControladora = argumentos[1]
            return "Tipo de controladora alterada para "+TipoControladora

    elif comando == "VALID":
        if (argumentos[1] != "eval") and (argumentos[1] != "arvore"):
            return "Tipo de parametro invalido. Esperado eval ou arvore. Recebido:"+argumentos[1]
        else:
            ValidacaoFormula = argumentos[1]
            return "Tipo de validacao de formula alterada para "+ValidacaoFormula

    # Chama rotina para processamento dos comandos
    return processa_comando(ModoPersistencia,TipoControladora,ValidacaoFormula,comando,codigo,formula)

