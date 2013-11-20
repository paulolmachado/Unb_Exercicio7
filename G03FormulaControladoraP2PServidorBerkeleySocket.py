from G03Persistencia_SGBD import *
import sys

comando = ""
opcoes = ["GET","POST","PUT","DELETE","OPTIONS","HEAD","TRACE","CONNECT","QUIT"]

while comando != "QUIT":
    opcao = raw_input("Entre com a opcao: ")
    argumentos = opcao.split() # Separa argumentos
    comando = argumentos[0].upper() # Obtem primeiro argumento: comando
    
    if not any(comando in s for s in opcoes):
        print """
            Sintaxe:
                GET <codigo>           # Recuperar
                POST <formula>         # Incluir
                PUT <codigo> <formula> # Alterar
                DELETE <codigo>        # Excluir
                OPTIONS                # Listar todas
                HEAD                   # Limpar todas
                TRACE <codigo>         # Executar formula da base
                CONNECT <formula>      # Executar formula
                QUIT 
        """
    
    if comando == "GET":
        codigo = argumentos[1]
        formula = recuperar(int(codigo))
        if formula == None:
            print "Registro nao existe."
        else:
            print "Formula:",formula
    if comando == "POST":
        codigo = incluir(opcao[len(comando)+1:])
        print "Registro incluido. Codigo:", codigo
    if comando == "PUT":
        codigo = argumentos[1]
        formula = opcao[len(comando)+1:][len(codigo)+1:]
        codigo = alterar(int(codigo), formula)
        if codigo == None:
            print "Registro nao existe."
        else:
            print "Registro alterado. Codigo:", codigo
    if comando == "DELETE":
        codigo = argumentos[1]
        codigo = excluir(int(codigo))
        if codigo == None:
            print "Registro nao existe."
        else:
            print "Registro deletado. Codigo:", codigo
    if comando == "OPTIONS":
        formulas = listar() 
        if (formulas): 
            for formula in formulas:
                print str(formula[0])+"="+formula[1]
        else:
            print "Lista vazia"
    if comando == "HEAD":
        formulas = limpar()
        print "Lista de formulas eliminada."
    if comando == "TRACE":
        codigo = argumentos[1]
        formula = recuperar(int(codigo))
        if formula == None:
            print "Registro nao existe."
        else:
            if (formula): 
                try:  
                    resultado = eval(formula)
                except:
                    print "Formula invalida:",formula
                else:
                    print resultado
    if comando == "CONNECT":
        formula = opcao[len(comando)+1:]
        if (formula): 
            try:  
                resultado = eval(formula)
            except:
                print "Formula invalida:",formula
            else:
                print resultado
                
print "Fim do Programa"
