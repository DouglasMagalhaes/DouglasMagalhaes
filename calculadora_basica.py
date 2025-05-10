# Calculadora básica em python

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Não existe divisão por zero!")
        return None
    return a / b

# Lista para guardar as operações já feitas
operacao = []


def Calculadora():
    while True:

        print("\nCalculadora Básica")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        print("6. Ver lista das operações já feitas")

        escolha = input("Escolha uma operação matemática 1/2/3/4/5/6: ")

        if escolha == '6':
                print(f"Lista das operações anteriores: {operacao}.")
                continue

        if escolha == '5':
            print("\nVolte sempre!")
            break

        if escolha in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Digite aqui o primeiro número: "))
                num2 = float(input("Digite aqui o segundo número: "))
            except ValueError:
                print("Entrada invalida!")
                continue

            if escolha == '1':
                resultado = somar(num1, num2)
                operacao.append(f"Adição: {num1} + {num2} = {resultado}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"A soma de {num1} + {num2} = {resultado}.")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif escolha == '2':
                resultado = subtrair(num1, num2)
                operacao.append(f"Subtração: {num1} - {num2} = {resultado}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"A subtração de {num1} - {num2} = {resultado}.")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif escolha == '3':
                resultado = multiplicar(num1, num2)
                operacao.append(f"Multiplicação: {num1} * {num2} = {resultado}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"A multiplicação de {num1} * {num2} = {resultado}.")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                if resultado is not None:
                    operacao.append(f"Divisão: {num1} / {num2} = {resultado}")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(f"A divisão de {num1} / {num2} = {resultado}.")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("Tente novamente!")
        


Calculadora()
