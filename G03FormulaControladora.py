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

    if TipoControladora == "Monolitica": # Se a controladora eh monolitica, ou seja, grava local,
                                         # entao chama a funcao apropriada na controladora monolitica.

        if comando == "GET":
            return recuperar_monolitica(ModoPersistencia, codigo)
        elif comando == "POST":
            return incluir_monolitica(ModoPersistencia, formula)
        elif comando == "PUT":
            return alterar_monolitica(ModoPersistencia, codigo, formula)
        elif comando == "DELETE":
            return excluir_monolitica(ModoPersistencia, codigo)
        elif comando == "OPTIONS":
            return listar_monolitica(ModoPersistencia)
        elif comando == "HEAD":
            return limpar_monolitica(ModoPersistencia)
        elif comando == "TRACE":
            return valida_monolitica(ModoPersistencia, ValidacaoFormula, codigo)
        elif comando == "CONNECT":
            return executa_monolitica(ValidacaoFormula, formula)

    elif TipoControladora == "Berkeley": # Se a controladora eh Berkeley Socket, chama funcao
                                         # apropriada pra enviar o comando pela rede.
        return envia_comando_berkeley(ModoPersistencia,ValidacaoFormula,comando,codigo,formula)

    elif TipoControladora == "FTP":      # Se a controladora eh FTP, chama funcao
                                         # apropriada pra enviar o comando pela rede.
        return envia_comando_ftp(ModoPersistencia,ValidacaoFormula,comando,codigo,formula)



