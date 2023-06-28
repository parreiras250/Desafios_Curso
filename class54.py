""" Faça uma lista de compras 
O usuario deve ter a possibilidade de inserir, apagar e listar valores 
da sua lista 
Não é permita que o programa quebre com erros de indices inexistentes na lista """


#Codigo --> tentativa pessoal

import os
lista_compras = []
letras_permitidas = 'ial'

while True:
  print('Selecione uma opção')
  comandos = input('[i]serir [a]pagar [l]istar [s]air:').lower()
  if comandos == 's':
     break
  
  if len(comandos) > 1:
      print('Digite apenas [i] [a] [l]')
      continue
      
  if comandos not in letras_permitidas:
      print('Você não digitou uma opção valida')
      continue
  
  if comandos == 'i':
     os.system('cls')
     inserir = input('Item: ')
     lista_compras.append(inserir)
     print('item adicionado')

  elif comandos == 'l':
     os.system('cls')
     print('Aqui está sua lista de compras atualizada: ')
     for indice, nome in enumerate(lista_compras):
        print(indice, nome)

  if comandos == 'a':
    apagar = input('Apagar? ')
    if apagar.isdigit():
        apagar = int(apagar)
        if apagar in range(len(lista_compras)):
            del lista_compras[apagar]
        else:
            print('Índice inválido')
    

    
 
        

    


     


