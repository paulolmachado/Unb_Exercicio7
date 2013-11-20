#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

def validar_eval(formula):
    try:
        resultado = eval(formula)
    except:
        return "formula invalida"
    finally:
        return resultado