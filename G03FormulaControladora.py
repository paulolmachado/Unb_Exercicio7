#!/usr/bin/env python
#
# Modulo: Controladora Geral
# Descricao: Seleciona, baseado no tipo de controladora e no modo de persistencia
#            a funcao adequada para tratamento da solicitacao. Desta forma, em uma
#            mesma camada controladora, pode-se optar por diversos tipos de
#            persistencia ou de comunicacao de dados.
#

from G03FormulaControladoraMonolitica import *

def recuperar (TipoControladora, ModoPersistencia, codigo):
    if TipoControladora == "Monolitica":
        return recuperar_monolitica(ModoPersistencia, codigo)
    elif TipoControladora == "Berkeley":
        return recuperar_berkeley(ModoPersistencia, codigo)
    elif TipoControladora == "FTP":
        return recuperar_ftp(ModoPersistencia, codigo)

def incluir (TipoControladora, ModoPersistencia, formula):
    if TipoControladora == "Monolitica":
        return incluir_monolitica(ModoPersistencia, formula)
    elif TipoControladora == "Berkeley":
        return incluir_berkeley(ModoPersistencia, formula)
    elif TipoControladora == "FTP":
        return incluir_ftp(ModoPersistencia, formula)

def alterar(TipoControladora, ModoPersistencia, codigo, formula):
    if TipoControladora == "Monolitica":
        return alterar_monolitica(ModoPersistencia, codigo, formula)
    elif TipoControladora == "Berkeley":
        return alterar_berkeley(ModoPersistencia, codigo, formula)
    elif TipoControladora == "FTP":
        return alterar_ftp(ModoPersistencia, codigo, formula)

def excluir(TipoControladora, ModoPersistencia, codigo):
    if TipoControladora == "Monolitica":
        return excluir_monolitica(ModoPersistencia, codigo)
    elif TipoControladora == "Berkeley":
        return excluir_berkeley(ModoPersistencia, codigo)
    elif TipoControladora == "FTP":
        return excluir_ftp(ModoPersistencia, codigo)

def listar(TipoControladora, ModoPersistencia):
    if TipoControladora == "Monolitica":
        return listar_monolitica(ModoPersistencia)
    elif TipoControladora == "Berkeley":
        return listar_berkeley(ModoPersistencia)
    elif TipoControladora == "FTP":
        return listar_ftp(ModoPersistencia)

def limpar(TipoControladora, ModoPersistencia):
    if TipoControladora == "Monolitica":
        return limpar_monolitica(ModoPersistencia)
    elif TipoControladora == "Berkeley":
        return limpar_berkeley(ModoPersistencia)
    elif TipoControladora == "FTP":
        return limpar_ftp(ModoPersistencia)

def validar(formula):
    try:
        resultado = eval(formula)
    except:
        return "erro"
    else:
        return str(resultado)

