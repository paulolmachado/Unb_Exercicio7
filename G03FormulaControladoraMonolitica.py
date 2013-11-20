#!/usr/bin/env python
#
# Modulo de Interface de usuario.
# Descricao: Seleciona, baseado no tipo de controladora e no modo de persistencia
#            a funcao adequada para tratamento da solicitacao. Desta forma, em uma
#            mesma camada controladora, pode-se optar por diversos tipos de
#            persistencia ou de comunicacao de dados.
#

from G03FormulaPersistenciaTextual import *
from G03FormulaPersistenciaSGBD import *

def recuperar_monolitica(ModoPersistencia, codigo):
    if ModoPersistencia == "Textual":
        return textual_recuperar(codigo)
    elif ModoPersistencia == "SGBD":
        return sgbd_recuperar(codigo)

def incluir_monolitica(ModoPersistencia, formula):
    if ModoPersistencia == "Textual":
        return textual_incluir(formula)
    elif ModoPersistencia == "SGBD":
        return sgbd_incluir(formula)

def alterar_monolitica(ModoPersistencia, codigo, formula):
    if ModoPersistencia == "Textual":
        return textual_alterar(codigo, formula)
    elif ModoPersistencia == "SGBD":
        return sgbd_alterar(codigo, formula)

def excluir_monolitica(ModoPersistencia, formula):
    if ModoPersistencia == "Textual":
        return textual_excluir(formula)
    elif ModoPersistencia == "SGBD":
        return sgbd_excluir(formula)

def listar_monolitica(ModoPersistencia):
    if ModoPersistencia == "Textual":
        return textual_listar()
    elif ModoPersistencia == "SGBD":
        return sgbd_listar()

def limpar_monolitica(ModoPersistencia):
    if ModoPersistencia == "Textual":
        return textual_limpar()
    elif ModoPersistencia == "SGBD":
        return sgbd_limpar()



