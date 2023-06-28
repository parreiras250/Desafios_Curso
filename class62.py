""" Esse codigo adiciona a logica anterior o calculo do segundo digito do cpf 
Vale destacar que, podemos brincar com esse codigo futuramente, tentar ajusta-lo para que o usuario 
imput apenas os 9 primeiros digitos do cpf, nada além disso, e dessa forma o programa irá calcular os 2 digitos
finais e retorna-los para o usuario """

numeros_multplicaveis = [10, 9, 8, 7, 6, 5, 4, 3, 2]
contador_regressivo = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

while True:
  cpf_digitado = input('Digite seu CPF, sem pontuações: ')
  multplicacao_cpf1 = []
  multplicacao_cpf2 = []
  cpf_coletado = []

  if len(cpf_digitado) != 11:
     print('Digite apenas 11 digitos')
     continue

  for caracter in cpf_digitado: 
    try:
      numero = int(caracter)
      cpf_coletado.append(caracter)
    except ValueError:
      print('Valor invalido, digite apenas numeros')

  for i in range(len(cpf_coletado)):
      cpf_coletado[i] = int(cpf_coletado[i])

  for i, j in enumerate(numeros_multplicaveis):
     j *= cpf_coletado[i]
     multplicacao_cpf1.append(j)

  somatorio = (sum(multplicacao_cpf1)*10)%11
  digito_1 = 0 if somatorio > 9 else somatorio

  print(f'O primeiro digito do seu cpf é: {digito_1}')

  for i, j in enumerate(contador_regressivo):
     j *= cpf_coletado[i]
     multplicacao_cpf2.append(j)
  somatorio_2 = (sum(multplicacao_cpf2)*10)%11 
  digito_2 = 0 if somatorio_2 > 9 else somatorio_2

  print (f'O segundo digito do seu cpf é: {digito_2}')

  sair = input('Deseja [s]air? ').lower().startswith('s')
  if sair:
     break
  else:
     continue