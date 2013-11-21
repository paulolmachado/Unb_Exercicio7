#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Persistencia Textual
# Descricao: Prover a persistencia das formulas em um arquivo local chamado "formulas.txt".
#            Cada linha do arquivo possui uma formula. A variavel "codigo" referenciado no
#            no programa corresponde ao numero da linha no arquivo.
#

import sys

arq=''
registros=[]

###################### Funcoes de apoio

def __abrir(modo):
    global arq
    try:
        arq = open('formulas.txt',modo)
    except:
        print('Nao foi possivel abrir o arquivo formulas.')

def __fechar():
    arq.close()

def __salvar_registros(): # Salva a lista de formulas no arquivo
    global registros
    __abrir('w')
    for linha in registros:
        arq.write(linha.replace("\n","")+"\n")
    __fechar()

def __recuperar_registros(): # Recupera as formulas do arquivo em uma lista
    global registros
    registros = []
    __abrir('r')
    for linha in arq:
        registros = registros + [linha.replace("\n","")]
    __fechar()

############################### Funcoes de Processamento

def textual_recuperar(chave):
    global registros
    __recuperar_registros()
    if chave > len(registros) or (chave < 1):
        return "Registro nao encontrado"
    else:
        return registros[chave-1]

def textual_incluir(formula):
    global registros
    __recuperar_registros()
    registros += [formula] # Adiciona formula nos registros
    __salvar_registros()
    return "Registro incluido:"+str(len(registros))

def textual_excluir(chave):
    global registros
    __recuperar_registros()
    if chave > len(registros) or chave < 1:
        return "Registro nao encontrado"
    else:
        registros[chave-1]=''
        __salvar_registros()
        return "Registro deletado. Codigo:"+str(chave)

def textual_alterar(chave,formula):
    global registros
    __recuperar_registros()
    if chave > len(registros) or chave < 1:
        return "Registro nao encontrado"
    else:
        registros[chave-1]=formula
        __salvar_registros()
        return "Registro alterado. Codigo:"+str(chave)

def textual_listar():
    global registros
    __recuperar_registros()
    return registros

def textual_limpar():
    __abrir('w')
    arq.write('')
    __fechar()
    return "Lista de formulas eliminada."


