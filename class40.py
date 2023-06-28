#Codigo de autoria propria
while True:
    number_1 = input("Type your first number: ")
    number_2 = input("type your second number: ")
    operator = input("type your operator (+  - * /): ")
    try:
      new_number1 = float(number_1)
      new_number2 = float(number_2)

      if operator == '+':
        operator = new_number1 + new_number2
      elif operator == '-':
        operator = new_number1 - new_number2
      elif operator =='*':
        operator = new_number1 * new_number2
      elif operator == '/':
        operator = new_number1 / new_number2
      else:
        print('Your operator in not valid')
        break
    except:
      print("you didn't provide the right information ")

       
    # elif operator is not '+' or '-' or '*' or '/':
    #   print('Operator invalid')
    print(operator)

    quit = input('Do you want to leave? [y]es: ').lower().startswith('y')
    
    if quit is True:
        break