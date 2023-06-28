"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

def soma(list1, list2):
    sum_lists =[]
    lengh1 = len(list1)
    lengh2 = len(list2)
    min_lengh = min(lengh1, lengh2) 

    for i in range(min_lengh):
        sum_lists.append((list1[i]+list2[i]))
    

    if lengh1 > min_lengh: 
        for i in range(min_lengh, lengh1):
            sum_lists.append((list1[i]))
    elif lengh2 > min_lengh:
        for i in range(min_lengh,lengh2):
            sum_lists.append((list2[i]))

    return sum_lists

result = soma(lista_a,lista_b)

print(result)

#outra solução 

def somar(list1, list2):
  list1_and_list2 =[]
  for number1, number2 in zip_longest(list1, list2):
      somar = number1 + number2 if number1 and number2 else number1 or number2
      list1_and_list2.append(somar)
  return list1_and_list2

print(somar(lista_a,lista_b))

#SOLUÇÃO PROFESSOR
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)


