import sys

arq=''
registros=[]

def __abrir(modo):
    global arq
    try:
        arq = open('formulas.txt',modo)
    except:
        print('Nao foi possivel abrir o arquivo formulas.')
  
def __fechar():
    arq.close()

def __salvar_registros():
    global registros
    __abrir('w')
    for linha in registros:
        arq.write(linha+"\n") # Grava formulas em registros
    __fechar()

def __recuperar_registros():
    global registros
    __abrir('r')
    registros = arq.readlines()
    __fechar()



def textual_recuperar(chave):
    global registros
    __recuperar_registros()
    if chave > len(registros) or chave < 1:
        return None
    else:
        return registros[chave-1]

def textual_incluir(formula):
    global registros
    __recuperar_registros()
    registros += [formula] # Adiciona formula nos registros
    __salvar_registros()
    return len(registros)
  
def textual_excluir(chave):
    global registros
    __recuperar_registros()
    if chave > len(registros) or chave < 1:
        return None
    else:
        registros[chave-1]=''
        __salvar_registros()
        return chave

def textual_alterar(chave,formula):
    global registros
    __recuperar_registros()
    if chave > len(registros) or chave < 1:
        return None
    else:
        registros[chave-1]=formula
        __salvar_registros()
        return chave

def textual_listar():
    global registros
    __recuperar_registros()
    return registros

def textual_limpar():
    __abrir('w')
    arq.write('')
    __fechar()
    return registros

# Teste de chamadas as funcoes definidas acima

#print "Limpando tudo ..."
#print limpar() # Limpar todos os registros
#print "Adicinando uma formula (1 + 2) ..."
#print incluir('(1 + 2)') # Incluir uma formula
#print "Adicinando uma formula (4 / 2) ..."
#print incluir('(4 / 2)') # Incluir outra formula
#print "Adicinando uma formula (8 / 2) ..."
#print incluir('(8 / 2)') # Incluir outra formula
#print "Recuperando a primeira formula ..."
#print recuperar(1) # Recuperar a primeira formula inserida
#print "Listando as formulas ..."
#print listar() # Listar todas as formulas
#print "Alternado a primeira formula ..."
#print alterar(1,'(3 * 4)') # Alterar a primeira formula
#print "Listando as formulas ..."
#print listar() # Listar novamente todas as formulas
#print "Excluindo a segunda formula ..."
#print excluir(1) # Excluir a primeira formula
#print "Listando as formulas ..."
#print listar() # Listar novamente todas as formulas
#print "Fim"

