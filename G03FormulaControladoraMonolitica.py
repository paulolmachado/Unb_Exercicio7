#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Controladora Monolitica
# Descricao: Seleciona, baseado no modo de persistencia (Textual ou SGBD), a funcao adequada para
#            tratamento da solicitacao. Para os casos de validacao e execucao de formula
#            considera o tipo: eval ou arvore.
#

from G03FormulaPersistenciaTextual import *
from G03FormulaPersistenciaSGBD import *
from G03FormulaModeloEval import *

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

def limpar_monolitica(ModoPersistencia):
    if ModoPersistencia == "Textual":
        return textual_limpar()
    elif ModoPersistencia == "SGBD":
        return sgbd_limpar()

def listar_monolitica(ModoPersistencia):
    if ModoPersistencia == "Textual":
        formulas = textual_listar()
    elif ModoPersistencia == "SGBD":
        formulas = sgbd_listar()
    if (formulas):
        resultado = ""
        for formula in formulas:
            resultado = resultado + formula + "\n"
        return resultado
    else:
        return "Lista vazia"

def valida_monolitica(ModoPersistencia, ValidacaoFormula, codigo):
    if ModoPersistencia == "Textual":
        formula = textual_recuperar(codigo)
    elif ModoPersistencia == "SGBD":
        formula = sgbd_recuperar(codigo)
    if formula == None:
        return "Formula nao encontrada"
    else:
        if ValidacaoFormula == "eval":
            return validar_eval(formula)
        elif ValidacaoFormula == "arvore":
            return validar_eval(formula)
        else:
            return "Tipo de validacao de formula invalido: "+ValidacaoFormula

def executa_monolitica(ValidacaoFormula, formula):
    if ValidacaoFormula == "eval":
        return validar_eval(formula)
    elif ValidacaoFormula == "arvore":
        return validar_eval(formula)
    else:
        return "Tipo de validacao de formula invalido: "+ValidacaoFormula
