#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

#from calculadora import *

numeros   = ["0","1","2","3","4","5","6","7","8","9","10"]
operacoes = ["/","*","+","-"]

def testarFormula(formula, vaziook=False):
    estado,parenteses = 0, 0
    if (formula==""):
        return vaziook
    formula = formula.replace(" ", "")
    for caracter in formula:
        if (estado==0): #start
            if (caracter=="("):
                estado = 1
            elif (caracter.isdigit()):
                estado = 2
            else:
                return False
        elif (estado==1): # (
            if (caracter=="("):
                estado = 1
            elif (caracter.isdigit()):
                estado = 2
            else:
                return False
        elif (estado==2): # numero
            if (caracter==")"):
                estado = 4
            elif (caracter.isdigit()):
                estado = 2
            elif (caracter in operacoes):
                operacao=caracter
                estado = 3
            else:
                return False
        elif (estado==3): # operacao
            numero = ""
            if (caracter.isdigit()):
                estado = 2
            elif (caracter=="("):
                estado = 1
            else:
                return False
        elif (estado==4): # )
            numero = ""
            if (caracter==")"):
                estado = 4
            elif (caracter in operacoes):
                operacao=caracter
                estado = 3
            else:
                return False
        else:
            return False
        if (estado == 1):
            parenteses = parenteses + 1
        if (estado == 4):
            parenteses = parenteses - 1
    return (parenteses==0)

def contaOperacoes(formula):
    quantidade = 0
    for caracter in formula:
        if (caracter in operacoes):
            quantidade = quantidade + 1
    return quantidade

def retiraNumero(formula):
    numero = ""
    for caracter in formula:
        if (caracter in numeros):
            numero = numero + caracter
        else:
            break
    return numero

def posicaoParentesesAbertura(formula):
    return formula.find("(")

def posicaoParentesesFechamento(formula):
    idx,parenteses = 0, 0
    for caracter in formula:
        if (caracter=="("):
            parenteses = parenteses + 1
        if (caracter==")"):
            parenteses = parenteses - 1
            if (parenteses==0):
                return idx
        idx = idx+1
    return 0

def temParentesesExternosAlinhados(formula):
    idx,parenteses = 0, 0
    for caracter in formula:
        if (caracter=="("):
            parenteses = parenteses + 1
        if (caracter==")"):
            parenteses = parenteses - 1
            if (parenteses==0):
                return ((formula[0]=="(") and ((idx+1)==len(formula)))
        idx = idx+1
    return False

def voltaAtrasUmaOperacao(formula, idx1):
    idx = idx1 - 1
    while ((idx>0) and (formula[idx-1] in numeros)):
        idx = idx - 1
    if (idx > 0):
        return idx
    return idx1

def montaArvoreRecursivo(formula):
    noh = [None, None, None, None]
    if ((formula=="") or (formula==None)):
        return None
## Obs: O parametro formula pode ser uma fracao (subformula) da formula original em funcao da natureza recusiva de resolucao da formula.

## Enquanto houver parenteses cercando a formula (primeiro caracter a esquerda e ultimo caracter a direita) ...
##   entao elimina tais parenteses da formula.
    while (temParentesesExternosAlinhados(formula)):
        formula = formula[1:-1]

## Localiza o primeiro parentese da esquerda para direita na formula e coloca a posicao na variavel idx1.
    idx1 = posicaoParentesesAbertura(formula)
## Localiza o parentese que encerra o primeiro parentese encontrado na formula e coloca a posicao na variavel idx2.
    idx2 = posicaoParentesesFechamento(formula)

## Se o parentese for encontrado na primeiro posicao da formula ...
##   retorna uma lista de 4 elementos:
##   1. lista resultado da funcao montaArvoreRecursivo passando a primeira parte da formula identificada entre as posicoes idx1 e idx2.
##   2. operador matematico (/,*,+,-) depois da primeira formula.
##   3. lista resultado da funcao montaArvoreRecursivo passando o restante da formula depois do operador matematico.
##   4. Preserva o None, para utilizacao na execucao/calculo da formula.
    if (idx1==0):
        noh = [montaArvoreRecursivo(formula[idx1:idx2+1]), formula[idx2+1], montaArvoreRecursivo(formula[idx2+2:]), None]

## Se o parentese foi encontrado alem da primeira posicao da formula (idx1>0), ou seja ha numeros/operadores antes da formula entre parenteses ...
    elif (idx1>0):

##   Se o elemento anterior eh uma operacao de * ou / entao reduz idx1 para contemplar operando anterior (precedencia entre operadores)
        if (formula[idx1-1] in operacoes[0:2]):
            idx1 = voltaAtrasUmaOperacao(formula, idx1)

##   retorna uma lista de 4 elementos:
##   1. lista resultado da funcao montaArvoreRecursivo passando a primeira parte da formula, antes do trecho entre idx1 e idx2 e antes do operador.
##   2. operador matematico (/,*,+,-) depois antes da formula identificada entre idx1 e idx2.
##   3. lista resultado da funcao montaArvoreRecursivo passando o restante da formula.
##   4. Preserva o None, para utilizacao na execucao/calculo da formula.
        noh = [montaArvoreRecursivo(formula[0:idx1-1]), formula[idx1-1], montaArvoreRecursivo(formula[idx1:]), None]

## Se nao encontrou parenteses na formula (idx1<0), entao efetua o calculo da subformula
    else:

## Para cada uma das quatro operacoes, faz o loop:
        for ope in operacoes:

## Para cada iteracao do loop, verifica se existe algum operador (+,-,*,/) na formula ...
            if (contaOperacoes(formula)>0):

## Se existe, entao atribui a idx1 a posicao da operacao encontrada na formula.
                idx1 = formula.find(ope)

## Se nao encontrou o operador da vez na formula ...
                if (idx1 != -1):

## Entao verifica novamente se ainda ha alguma operacao matematica por fazer ...
                    if (contaOperacoes(formula) > 1):

##   retorna uma lista de 4 elementos:
##   1. lista resultado da funcao montaArvoreRecursivo passando a primeira parte da formula, antes de idx1.
##   2. operador matematico (/,*,+,-) na posicao de idx1.
##   3. lista resultado da funcao montaArvoreRecursivo passando o restante da formula.
##   4. Preserva o None, para utilizacao na execucao/calculo da formula.
                        noh = [montaArvoreRecursivo(formula[0:idx1]), formula[idx1], montaArvoreRecursivo(formula[idx1+1:]), None] ## Comentar aqui ...
                    else:
##   se nao ha mais operacao matematica por fazer, entao retorna uma lista de 4 elementos:
##   1. o primeiro digito/numero da formula.
##   2. operador matematico (/,*,+,-) na posicao de idx1.
##   3. o segundo digito da formula.
##   4. Preserva o None, para utilizacao na execucao/calculo da formula.
                        noh = [retiraNumero(formula[0]), formula[idx1], retiraNumero(formula[idx1+1:]), None] ## Comentar aqui ...
## Se nao houver qualquer operacao (+,-,*,/) na formula, retorna a propria formula (fim do processo recursivo)
            else:
                noh = formula
    return noh

def montaArvore(formula):
    formula = formula.replace(" ", "") ## Elimina os espacos dentro da formula, deixando apenas os caracteres significativos.
    if (testarFormula(formula)): ## Se a formula estiver consistente ...
        return montaArvoreRecursivo(formula) ## retorna a arvore montada sobre a formula
    return [None, None, None, None] ## Se nao estiver consistente, retorna os 4 elementos nulos.

def executaCalculadora(operacao, primeiro, segundo):
    if (operacao=="+"):
        return somar(primeiro, segundo)
    elif (operacao=="-"):
        return subtrair(primeiro, segundo)
    elif (operacao=="*"):
        return multiplicar(primeiro, segundo)
    elif (operacao=="/"):
        return dividir(primeiro, segundo)
    else:
        return 0

def executaArvoreRecursivo(arvore):
    operacao = 0
    strprimeiro = 0
    strsegundo = 0
    if (arvore[3]!=None):
        return
    if ((type(arvore[0])==list) and (arvore[0][3]==None)):
        executaArvoreRecursivo(arvore[0])
    if ((type(arvore[2])==list) and (arvore[2][3]==None)):
        executaArvoreRecursivo(arvore[2])
    operacao    = arvore[1]
    strprimeiro = arvore[0]
    strsegundo  = arvore[2]
    if ((type(arvore[0])==list) and (arvore[0][3]!=None)):
        strprimeiro = arvore[0][3]
    if ((type(arvore[2])==list) and (arvore[2][3]!=None)):
        strsegundo = arvore[2][3]
    arvore[3] = executaCalculadora(operacao, int(strprimeiro), int(strsegundo))
    return

def apresentarArvore(formula, resultado):
    print formula + " = "

# Lista de formulas aonde lista = [nonono, nonono, nonono]
formulas  = [ "5 + ((4/2) + 1 + 3)/2", "(5+4/2)+(3+1*9)", "5+2+1*((4*3)+1+2)", "((3/3) + 4)", "7 + 4 / 2 + (5 * 1)"]

# Para cada formula dentro da lista formulas acima declarada
for f in formulas:
    print f,
    print "=",
    if (testarFormula(f)):
        arvore = montaArvore(f)
## Para cada iteracao do loop, chama executaArvoreRecursivo(arvore), funcao que resolve as operacoes matematicas da lista arvore.
## Se o 4o elemento for difrente de none (nada), ou seja, o calculo atingiu todas as listas internas chegando a um resultado final da formula, ...
##   entao imprime na tela o conteudo da lista resultante e sai do loop (break) interno voltando para o loop externo (f), passando para a proxima formula.
        while True:
            executaArvoreRecursivo(arvore)
            if (arvore[3] != None):
                print str(arvore[3])
                break

a = raw_input("espera ....")
exit()
