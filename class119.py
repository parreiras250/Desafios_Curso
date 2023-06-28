# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

#solução pessoal 
import os
import json

task_board = []
action_stack = []
current_action_index = -1

def show_taskboard():
  print()
  print('TASKS:')
  print(*task_board, sep='\n')
  print()

def list_tasks(task, list1=None):
  if list1 == None: 
      list1 = []
  list1.append(task)
  action_stack.append(('add', task))
  return list1

def analysis(input): 
  global current_action_index
  actions = ['list', 'redo', 'undo', 'cls', 'exit']
  if input not in actions:
      list_tasks(input, task_board)
      current_action_index = len(action_stack) - 1
      show_taskboard()
  elif input == 'list':
    if task_board:
      os.system('cls')
      show_taskboard()
    else:
      os.system('cls')
      print('Nothing on your list yet!')
      print()
  elif input == 'redo': 
# Geralmente esse comando causa alguma confusão, basicamente ele esta aqui para definir a posição do indice atual.  
# Se ele for menor e não igual ao tamanho da lista, definida por len(action_stack) -1 (valor que será refeito), 
# podemos seguir com a operação, pois existe um valor valido que será refeito. Quando somamos o + 1 na sequencia
# estamos buscando justamente esse ultimo valor. Pense que, o valor do indice atual (current_action_index) não pode ser igual 
# ao tamanho da lista - 1, ele deve ser menor, pois só assim poderemos somar +1. 
# imagine que, o tamanho da lista - 1 seja 3, se o valor do indice for 3, não podemos seguir com a operação 
# pois o retorno quando somarmos +1 não será um indice valido na lista (action_stack)
    if current_action_index < len(action_stack) - 1:  
        current_action_index += 1 
        action = action_stack[current_action_index]
        if action[0] == 'add': 
          task_board.append(action[1])
        show_taskboard()
    else:
      print('Nothing to redo')
  elif input == 'undo': #Reescrever lógica
    if current_action_index >= 0: #se o index for maior ou igual a zero, logo, temos um indice valido para os valores armazenados
      action =  action_stack[current_action_index]
      if action[0] == 'add':
        task_board.remove(action[1])
        current_action_index -= 1
      show_taskboard()
    else: 
      print('Nothing to undo!')
  elif input == 'cls':
       return os.system('cls')
  
  
if os.path.isfile('tasks.json'):
    with open('tasks.json', 'r+', encoding='utf8') as file:
        # Carrega os dados do arquivo JSON para a variável task_board
        task_board = json.load(file)
        for task in task_board:
          action_stack.append(('add', task))
        if action_stack:
           current_action_index = len(action_stack) - 1

while True: 
    print('Commands: list, undo, redo')

    user_input=input('Type one task or command:')
    analysis(user_input)
    if user_input == 'exit':
       break

with open('tasks.json', 'w', encoding='utf8') as file:
    json.dump(
        task_board,
        file,
        ensure_ascii=False,
        indent=2,
    )




