# Função para realizar a soma de dois números
def somar(a, b):
    return a + b

# Função para realizar a subtração de dois números
def subtrair(a, b):
    return a - b

# Função para realizar a multiplicação de dois números
def multiplicar(a, b):
    return a * b

# Função para realizar a divisão de dois números
def dividir(a, b):
    if b == 0:
        # Verifica se o divisor é zero e exibe uma mensagem de erro
        print("Não existe divisão por zero!")
        return None  # Retorna None para indicar erro
    return a / b  # Caso contrário, retorna o resultado da divisão

# Lista para armazenar o histórico de operações realizadas
operacao = []

# Função principal da calculadora
def Calculadora():
    # Laço infinito para manter a calculadora funcionando até o usuário decidir sair
    while True:
        # Exibição do menu de opções
        print("\nCalculadora Básica")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        print("6. Ver lista das operações já feitas")

        # Solicita ao usuário que escolha uma das opções
        escolha = input("Escolha uma operação matemática 1/2/3/4/5/6: ")

        # Mostra a lista de operações anteriores
        if escolha == '6':
            print(f"Lista das operações anteriores: {operacao}.")
            continue  # Volta para o início do laço

        # Encerra o programa
        if escolha == '5':
            print("\nVolte sempre!")
            break  # Sai do laço e encerra a função

        # Verifica se a escolha é válida
        if escolha in ['1', '2', '3', '4', '5', '6']:
            try:
                # Solicita ao usuário os dois números da operação
                num1 = float(input("Digite aqui o primeiro número: "))
                num2 = float(input("Digite aqui o segundo número: "))
            except ValueError:
                # Caso o usuário digite algo que não seja um número
                print("Entrada invalida!")
                continue  # Volta para o início do laço

            # Executa a operação escolhida e salva no histórico
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
                # Verifica se não houve erro na divisão (por zero)
                if resultado is not None:
                    operacao.append(f"Divisão: {num1} / {num2} = {resultado}")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(f"A divisão de {num1} / {num2} = {resultado}.")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            # Caso o usuário digite uma opção inválida
            print("Tente novamente!")

# Chamada da função para iniciar a calculadora
Calculadora()
