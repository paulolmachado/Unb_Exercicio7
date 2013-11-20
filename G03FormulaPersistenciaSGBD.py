import mysql.connector
from mysql.connector import errorcode
import sys

cnx=""

def __conectar():
  global cnx
  try:
    cnx = mysql.connector.connect(user='root', database='mysql')
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Senha ou usuario invalidos.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database nao existe")
    else:
      print(err)
    sys.exit()

def __desconectar():
  cnx.close()
      
def __nextval():
  __conectar()
  cursor = cnx.cursor()
  cursor.execute("select coalesce(max(codigo),0)+1 as codigo from formula")
  result = cursor.fetchone()
  cursor.close()
  __desconectar()
  for codigo in result:
    return codigo

def recuperar(chave):
  __conectar()
  cursor = cnx.cursor()
  cursor.execute("select valor from formula where codigo = %s",(str(chave),))
  result = cursor.fetchone()
  cursor.close()
  __desconectar()
  if result == None:
    return None
  for valor in result:
    return valor

def incluir(formula):
  proximo=__nextval()
  __conectar()
  cursor = cnx.cursor()
  cursor.execute("insert into formula (codigo, valor) values (%s,%s)",(str(proximo),formula))
  cursor.close()
  cnx.commit()
  __desconectar()
  return proximo

def excluir(chave):
  if recuperar(chave) == None: # Testa primeiro pra ver se a chave existe
    return None
  else:
    __conectar()
    cursor = cnx.cursor()
    #cursor.execute("delete from formula where codigo = %s",str(chave))
    cursor.execute("update formula set valor='' where codigo = %s",str(chave))
    cursor.close()
    cnx.commit()
    __desconectar()
    return chave

def alterar(chave,formula):
  if recuperar(chave) == None: # Testa primeiro pra ver se a chave existe
    return None
  else:
    __conectar()
    cursor = cnx.cursor()
    cursor.execute("update formula set valor = %s where codigo = %s",(formula,str(chave)))
    cursor.close()
    cnx.commit()
    __desconectar()
    return chave

def listar():
  __conectar()
  cursor = cnx.cursor()
  cursor.execute("select codigo,valor from formula")
  result = cursor.fetchall()
  cursor.close()
  __desconectar()
  return result

def limpar():
  __conectar()
  cursor = cnx.cursor()
  cursor.execute("select codigo,valor from formula")
  result = cursor.fetchall()
  cursor.execute("delete from formula")
  cursor.close()
  cnx.commit()
  __desconectar()
  return result

# Teste de chamadas das funcoes definidas acima

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

