"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
int_number = input(" Type an int number: ")

try:
  typed_number = int(int_number)
  if typed_number and (typed_number % 2 == 0):
    print('This number is even')
  if typed_number and (typed_number % 2 == 1):
   print('This number is odd')
except:
    print("you didn't type a valid int")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
time = input('What time is it? ')
try:
  hour = int(time)
  morning = hour >= 0 and  hour <= 11
  afternon = hour >= 12 and hour <= 17
  evening = hour >= 18 and hour <= 23
  if morning:
    print('Good morning')
  elif afternon:
    print('Good afternoon')
  elif evening:
    print('Good evening')
  else:
     print("don't recognize this hour")
except:
  print("you didn't type a valid hour")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
name = input('Write down your name: ')

caracters = len(name)

Short = caracters <= 4
Medium = caracters >= 5 and caracters <= 6

if caracters > 1:
  if Short:
      print('Your name is short')
  elif Medium:
      print('Your name is normal')
  else:
      print('Your name is really big')
else: 
   print('Type a name larger than 1 caracter')