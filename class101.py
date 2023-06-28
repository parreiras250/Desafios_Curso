# Exercício - Adiando execução de funções (solução pessoal)
def firstvalue(x):
    def secondvalue(y):
        return x + y
    return secondvalue


def multiplicator(x):
    def multplication (y):
      return x * y
    return multplication


def criar_funcao(funcao, *args):
    return funcao(*args)


soma_com_cinco = criar_funcao(firstvalue, 5)
multiplica_por_dez = criar_funcao(multiplicator, 10)

result1 = soma_com_cinco(2)
result2 = multiplica_por_dez(4)


print(result1)
print(result2)