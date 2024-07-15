import os
from art import logo
#Calculator
#Add
def add(n1, n2):
  return n1 + n2
#Subtract
def subtract(n1, n2):
  return n1 - n2
#Multiply
def multiply(n1, n2):
  return n1 * n2
#Divide
def divide(n1, n2):
  return n1 / n2
#Dictionary operation
operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}
def Calculator():
  print(logo)
  should_continue = True
  
  number1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  while should_continue:
    operation_symbol = input("Pick an operation : ")
    number2 = float(input("What's the next number?: "))
    ans = operations[operation_symbol](number1, number2)
    print(f"{number1} {operation_symbol} {number2} = {ans}")
    choice = input(f"Type 'y' to continue calculating with {ans} or type 'n' to start new Caculator \n")
    if (choice == 'n'):
      should_continue = False
      os.system('clear')
      Calculator()
    elif(choice == 'y'):
      number1 = ans

Calculator()
