print("\n ================= Python Calculadora ================= ")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

regra = 0

while (regra == 0):

    print("\nSelecione a operação desejada:\n")

    print("1 - soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("\n Digite sua opção: ")

    if escolha == '1' or escolha == '2' or escolha == '3' or escolha == '4':       #poderia ser somente    escolha <= '4'

        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))

        if escolha == '1':
            print("\n")
            print(num1, "+", num2, "=", add(num1, num2))
            print("\n")

            regra = 1

        elif escolha == '2':
            print("\n")
            print(num1, "-", num2, "=", subtract(num1, num2))
            print("\n")

            regra = 1

        elif escolha == '3':
            print("\n")
            print(num1, "*", num2, "=", multiply(num1, num2))
            print("\n")

            regra = 1

        elif escolha == '4':
            if num2 == 0:
                print("\n Não existe divisão por 0!")
                regra = 0

            else:
                print(num1, "/", num2, "=", divide(num1, num2))
                print("\n")
                regra = 1

    else:
        print("\nOpção Inválida!")
        regra = 0
