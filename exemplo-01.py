from ast import arg
import collections
from pymongo import MongoClient

uri = 'mongodb://root:example@localhost:27017/'

client = MongoClient(uri)

database = client['curso_python']
collection = database['pessoas']

'''
# Jeito Moderno
   database = client.curso_python
   collection = database.pessoas
'''

def read(**args): 
   try:
      return collection.find()
   except:
      print("ERROR!")

#print(list(read()))

'''
O op é referente aos operadores de Query, e pode receber os seguintes valores: 

$eq -> (==)
$ne -> (!=)
$gt -> (>)
$qte -> (>=)
$lt -> (<)
$lte -> (<=)
$in / $nin -> (igual / diferente) a um array
'''
def busca_com_filtro(field, op, value): 
   try:
      return collection.find({ 
         field: { 
            op: value 
         } 
      })
   except: 
      print("ERROR!")

# print(list(busca_com_filtro('idade', '$eq', 20)))
# print(list(busca_com_filtro('idade', '$lt', 23)))
# print(list(busca_com_filtro('idade', '$in', [15, 20, 23])))
# print(list(busca_com_filtro('nome', '$regex', '^G')))

def inserir(**args):
   try:
      collection.insert_one(args)
      print(list(collection.find()))
   except:
      print("ERROR!")

# inserir(nome="José", idade=18)

'''
Operadores de update

$set -> Faz o Update
$unset -> Remove o campo
$rename -> Renomeia o campo
'''
def atualizar(myQuery, op, FieldNewValue, newValue):
   try: 
      collection.update_one(
         myQuery, # Busca
         { op: {FieldNewValue: newValue}} # A substituicao
      )   
      print("Dados atualizado!")
   except:
      print("ERROR!")

# atualizar({'nome': 'Gabriel'}, '$set', 'idade', 23)

def remover(field, myQuery):
   try:
      collection.delete_one({field: myQuery})
      print("Dados removidos")
   except:
      print("ERROR")

# remover('nome', 'José')
# remover('nome', {'$regex': '^G'})
