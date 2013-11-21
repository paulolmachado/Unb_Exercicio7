#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Controladora Geral
# Descricao: Seleciona, baseada no tipo de controladora informada, a funcao adequada
#            para tratamento da solicitacao.
#

from G03FormulaControladoraMonolitica import *
from G03FormulaControladoraP2PClienteBerkeleySocket import *
#from G03FormulaControladoraP2PClienteFTP import *

def processa_comando(ModoPersistencia,TipoControladora,ValidacaoFormula,comando,codigo,formula):
    #print "ModoPersistencia:",ModoPersistencia
    #print "TipoControladora:",TipoControladora
    #print "ValidacaoFormula:",ValidacaoFormula
    #print "comando:",comando
    #print "codigo:",str(codigo)
    #print "formula:",formula

    if comando == "GET":

        if TipoControladora == "Monolitica":
            return recuperar_monolitica(ModoPersistencia, codigo)
        elif TipoControladora == "Berkeley":
            return recuperar_berkeley(ModoPersistencia, codigo)
        elif TipoControladora == "FTP":
            return recuperar_ftp(ModoPersistencia, codigo)

    elif comando == "POST":

        if TipoControladora == "Monolitica":
            return incluir_monolitica(ModoPersistencia, formula)
        elif TipoControladora == "Berkeley":
            return incluir_berkeley(ModoPersistencia, formula)
        elif TipoControladora == "FTP":
            return incluir_ftp(ModoPersistencia, formula)

    elif comando == "PUT":

        if TipoControladora == "Monolitica":
            return alterar_monolitica(ModoPersistencia, codigo, formula)
        elif TipoControladora == "Berkeley":
            return alterar_berkeley(ModoPersistencia, codigo, formula)
        elif TipoControladora == "FTP":
            return alterar_ftp(ModoPersistencia, codigo, formula)

    elif comando == "DELETE":

        if TipoControladora == "Monolitica":
            return excluir_monolitica(ModoPersistencia, codigo)
        elif TipoControladora == "Berkeley":
            return excluir_berkeley(ModoPersistencia, codigo)
        elif TipoControladora == "FTP":
            return excluir_ftp(ModoPersistencia, codigo)

    elif comando == "OPTIONS":

        if TipoControladora == "Monolitica":
            return listar_monolitica(ModoPersistencia)
        elif TipoControladora == "Berkeley":
            return listar_berkeley(ModoPersistencia)
        elif TipoControladora == "FTP":
            return listar_ftp(ModoPersistencia)

    elif comando == "HEAD":

        if TipoControladora == "Monolitica":
            return limpar_monolitica(ModoPersistencia)
        elif TipoControladora == "Berkeley":
            return limpar_berkeley(ModoPersistencia)
        elif TipoControladora == "FTP":
            return limpar_ftp(ModoPersistencia)

    elif comando == "TRACE":

        if TipoControladora == "Monolitica":
            return valida_monolitica(ModoPersistencia, ValidacaoFormula, codigo)
        elif TipoControladora == "Berkeley":
            return valida_berkeley(ModoPersistencia, ValidacaoFormula, codigo)
        elif TipoControladora == "FTP":
            return valida_ftp(ModoPersistencia, ValidacaoFormula, codigo)

    elif comando == "CONNECT":

        if TipoControladora == "Monolitica":
            return executa_monolitica(ValidacaoFormula, formula)
        elif TipoControladora == "Berkeley":
            return executa_berkeley(ValidacaoFormula, formula)
        elif TipoControladora == "FTP":
            return executa_ftp(ValidacaoFormula, formula)


