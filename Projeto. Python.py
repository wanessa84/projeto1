
#Projeto 01 - Calculadora Interativa
#Criar uma calculadora que realiza as 4 operações básicas (+, -, *, /) e aceita
#múltiplos cálculos em sequência.
#Habilidades trabalhadas:
#• Manipulação de entrada de usuário (input( ))
#• Uso de funções para organizar o código
#• Laços (while) e condicionais (if)

#Função para realizar a adição
def adição(num1, num2):
    return num1 + num2

#Função para realizar a subtração
def subtração(num1, num2):
    return num1 - num2

#Função para realizar a multiplição
def multiplicação(num1, num2):
    return num1 * num2

#Função para realizar a divisão
def divisão (num1, num2):
    if num2 !=0:
       return num1 / num2
    else: 
        print("Erro: Divisão por zero!")
        return 0
    
num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))

operacao = input("Escolha a operação (+,-,*,/): ")

if operacao == '+':
    print("Resultado:", adição (num1 , num2))
    





