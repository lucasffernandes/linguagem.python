# Função para realizar a operação de subtração
def subtracao(a, b):
    return a - b

def adicao(a, b):
    return a + b

# Função para realizar a operação de multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a operação de divisão
def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    else:
        return a / b

# Função principal da calculadora
def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Solicita que o usuário escolha uma operação
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    # Solicita que o usuário insira dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza a operação selecionada com base na escolha do usuário
    if escolha == '1':
        print("Resultado: ", adicao(num1, num2))
    elif escolha == '2':
        print("Resultado: ", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado: ", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado: ", divisao(num1, num2))
    else:
        print("Opção inválida!")

# Chama a função da calculadora
calculadora()