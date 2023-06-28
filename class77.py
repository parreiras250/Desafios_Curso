# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
#solução pessoal
corretas = 0
erradas = 0

for pergunta in perguntas: 
    print(f"Pergunta: {pergunta['Pergunta']} \n")
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice}) {opcao}')
        if pergunta['Resposta'] in opcao:
            resposta_correta_indice = indice 
    resposta_ususario = input('Escolha uma opção:')

    if resposta_ususario.isdigit():
        resposta_int = int(resposta_ususario)

    if resposta_int == resposta_correta_indice:
        print('Você acertou \n')
        corretas += 1
    else:
        print('Você errou \n')
        erradas += 1  
print(f'Você acertou {corretas} perguntas e errou {erradas}')
         




