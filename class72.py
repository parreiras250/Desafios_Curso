"""  Exercicio
Crie uma função que multiplica todos os argumentos nao nomeados recebidos 
Retorne o total para uma variavel e mostre o valor da variavel

Crie uma função que fala se um numero é par ou impar, retorne se o numero é 
par ou impar  """

#Solução pessoal

def multiplication(*args):
    total = 1
    for i in args:
        total *= i
    return total

def even_or_odd(x):
    if x % 2 == 0: 
        return f'Number {x} is even'
    return f'Number {x} is odd'
    
var1 = multiplication(52,56)
var2 = even_or_odd(4856)
        
print(var1)
print(var2)