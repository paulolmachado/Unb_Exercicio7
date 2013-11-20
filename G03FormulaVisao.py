#!/usr/bin/env python
#
# Modulo: Visao
# Descricao: Recebe os comandos GET, POST, PUT, DELETE, OPTIONS, HEAD, TRACE e CONNECT
#            acompanhados dos respectivos parametros e chama as devidas funcoes na
#            camada da Controladora.
#            Junto com a chamada das funcoes na Controladora, tambem informa qual o
#            modo de persistencia (Textual ou SGBD) e qual o tipo de Controladora
#            (Monolitica, P2P com Berkeley Socket ou FTP).
#

from G03FormulaControladora import *
import sys

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
                QUIT
        """

    if comando == "GET":
        codigo = argumentos[1]
        formula = recuperar(TipoControladora, ModoPersistencia, int(codigo))
        if formula == None:
            return "Registro nao encontrado."
        else:
            return formula

    if comando == "POST":
        codigo = incluir(TipoControladora, ModoPersistencia, opcao[len(comando)+1:])
        return "Registro incluido. Codigo:"+str(codigo)

    if comando == "PUT":
        codigo = argumentos[1]
        formula = opcao[len(comando)+1:][len(codigo)+1:]
        codigo = alterar(TipoControladora, ModoPersistencia, int(codigo), formula)
        if codigo == None:
            return "Registro nao encontrado."
        else:
            return "Registro alterado. Codigo:"+str(codigo)

    if comando == "DELETE":
        codigo = argumentos[1]
        codigo = excluir(TipoControladora, ModoPersistencia, int(codigo))
        if codigo == None:
            return "Registro nao encontrado."
        else:
            return "Registro deletado. Codigo:"+str(codigo)

    if comando == "OPTIONS":
        formulas = listar(TipoControladora, ModoPersistencia)
        if (formulas):
            resultado = ""
            for formula in formulas:
                resultado = resultado + formula + "\n"
            return resultado
        else:
            return "Lista vazia"

    if comando == "HEAD":
        formulas = limpar(TipoControladora, ModoPersistencia)
        return "Lista de formulas eliminada."

    if comando == "TRACE":
        codigo = argumentos[1]
        formula = recuperar(TipoControladora, ModoPersistencia, int(codigo))
        if formula == None:
            return "Registro nao existe."
        else:
            if validar(ValidacaoFormula, formula) == "erro":
                return "Formula invalida:"+formula
            else:
                return validar(ValidacaoFormula, formula)

    if comando == "CONNECT":
        formula = opcao[len(comando)+1:]
        if validar(ValidacaoFormula, formula) == "erro":
            return "Formula invalida:"+formula
        else:
            return validar(ValidacaoFormula, formula)

    if comando == "PERSIST":
        if (argumentos[1] != "Textual") and (argumentos[1] != "SGBD"):
            return "Tipo de parametro invalido. Esperado Textual ou SGBD. Recebido:"+argumentos[1]
        else:
            ModoPersistencia = argumentos[1]
            return "Tipo de pesistencia alterada para "+ModoPersistencia

    if comando == "CONTROL":
        if (argumentos[1] != "Monolitica") and (argumentos[1] != "Berkeley") and (argumentos[1] != "FTP"):
            return "Tipo de parametro invalido. Esperado Monolitica ou Berkeley ou FTP. Recebido:"+argumentos[1]
        else:
            TipoControladora = argumentos[1]
            return "Tipo de controladora alterada para "+TipoControladora

    if comando == "VALID":
        if (argumentos[1] != "eval") and (argumentos[1] != "arvore"):
            return "Tipo de parametro invalido. Esperado eval ou arvore. Recebido:"+argumentos[1]
        else:
            ValidacaoFormula = argumentos[1]
            return "Tipo de validacao de formula alterada para "+ValidacaoFormula
