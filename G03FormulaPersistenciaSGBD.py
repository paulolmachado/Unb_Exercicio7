#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Modulo: Persistencia em banco de dados
# Descricao: Persiste e recupera as formulas em bancos de dados MySQL.
#            A criação da tabela para armazenar as formulas foi criada a partir dos
#            comandos abaixo (conectado no banco de dados como root):
#
#            create database appdist;
#            use appdist
#            create table formula (codigo integer, valor varchar(250), primary key (codigo));
#            use mysql
#            create user 'appdist'@'%' identified by 'appdist';
#            grant all on appdist.* to 'appdist'@'%';
#            flush privileges;
#

import mysql.connector
from mysql.connector import errorcode
import sys

cnx=""
cursor=""

def __conectar():
  global cnx
  global cursor
  try:
    cnx = mysql.connector.connect(user='appdist', password='appdist', database='appdist', host='10.5.1.187')
    cursor = cnx.cursor()
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Senha ou usuario invalidos.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database nao existe")
    else:
      print(err)
    sys.exit()

def __desconectar():
  global cnx
  global cursor
  cursor.close()
  cnx.commit()
  cnx.close()

def __nextval():
  global cursor
  __conectar()
  cursor.execute("select coalesce(max(codigo),0)+1 as codigo from formula")
  result = cursor.fetchone()
  __desconectar()
  for codigo in result:
    return codigo

def sgbd_recuperar(chave):
  global cursor
  __conectar()
  cursor.execute("select valor from formula where codigo = %s",(str(chave),))
  result = cursor.fetchone()
  __desconectar()
  if result == None:
    return None
  for valor in result:
    return valor

def sgbd_incluir(formula):
  global cursor
  proximo=__nextval()
  __conectar()
  cursor.execute("insert into formula (codigo, valor) values (%s,%s)",(str(proximo),formula))
  __desconectar()
  return proximo

def sgbd_excluir(chave):
  global cursor
  if sgbd_recuperar(chave) == None: # Testa primeiro pra ver se a chave existe
    return None
  else:
    __conectar()
    #cursor.execute("delete from formula where codigo = %s",str(chave))
    cursor.execute("update formula set valor='' where codigo = %s",str(chave))
    __desconectar()
    return chave

def sgbd_alterar(chave,formula):
  global cursor
  if sgbd_recuperar(chave) == None: # Testa primeiro pra ver se a chave existe
    return None
  else:
    __conectar()
    cursor.execute("update formula set valor = %s where codigo = %s",(formula,str(chave)))
    __desconectar()
    return chave

def sgbd_listar():
  global cursor
  __conectar()
  cursor.execute("select codigo,valor from formula")
  result = [item[0] for item in cursor.fetchall()]
  ##result = cursor.fetchall()
  __desconectar()
  return result

def sgbd_limpar():
  global cursor
  __conectar()
  cursor.execute("select codigo,valor from formula")
  result = cursor.fetchall()
  cursor.execute("delete from formula")
  #cursor.close()
  #cnx.commit()
  __desconectar()
  return result

