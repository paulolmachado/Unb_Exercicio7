#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

def validar_eval(formula):
    if formula == None:
        return "Formula vazia"
    try:
        resultado = eval(formula)
        return str(resultado)
    except:
        return "Formula invalida"
