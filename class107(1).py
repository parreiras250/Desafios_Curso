# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#Tentativa pessoal usando zip longest from itertools (sem ver a aula)
from itertools import zip_longest

cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']

def zipper (list1, list2):
  cities_and_states = list(zip_longest(list1, list2, fillvalue='N/A'))
  return cities_and_states

result = zipper(cities, states)

print(result)
