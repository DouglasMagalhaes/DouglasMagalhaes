def celsius_fahrenheit1(c):
    f = (c * 9/5)+32
    return f

def celsius_kelvin2(c):
    k = c + 273.15
    return k

def fahrenheit_celsius3(f):
    c =  (f - 32) * 5/9
    return c

def kelvin_celsius4(k):
    c = k - 273.15
    return c

def fahrenheit_kelvin5(f):
    k = (f - 32) * 5/9 + 273.15
    return k

def kelvin_fahrenhiet6(k):
     f = (k - 273.15) * 9/5 + 32
     return f

def Calculadora():
    while True:

        print("-- Calculadora Convertora de Graus --")
        print("1. -Celsius para Fahrenheit;")
        print("2. -Celsius para Kelvin;")
        print("3. -Fahrenheit para Celsius;")
        print("4. -Kelvin para Celsius;")
        print("5. -Fahrenheit para Kelvin;")
        print("6. -Kelvin para fahrenheit.")
        print("------ 0 Para sair ------")

        escolha = input("Escolha uma das opções 1/2/3/4/5/6/0: ")

        if escolha in ['1','2', '3', '4', '5', '6', '0']:
            if escolha == '0':
                print("Obrigado por usar nossa calculadora!")
                break
            else:
                try:
                    entrada = float(input("Digite os graus: "))
                except ValueError:
                    print("Entrada Invalida!")
                    continue
        if escolha == '1':
            resultado = celsius_fahrenheit1(entrada)
            print(f"\n---{entrada}°C: {resultado:.2f}°F---\n")
        elif escolha == '2':
            resultado = celsius_kelvin2(entrada)
            print(f"\n---{entrada}°C: {resultado:.2f}°K---\n")
        elif escolha == '3':
            resultado = fahrenheit_celsius3(entrada)
            print(f"\n---{entrada}°F: {resultado:.2f}°C---\n")
        elif escolha == '4':
            resultado = kelvin_celsius4(entrada)
            print(f"\n---{entrada}°K: {resultado:.2f}°C---\n")
        elif escolha == '5':
            resultado = fahrenheit_kelvin5(entrada)
            print(f"\n---{entrada}°F: {resultado:.2f}°K---\n")
        elif escolha == '6':
            resultado = kelvin_fahrenhiet6(entrada)
            print(f"\n---{entrada}°K: {resultado:.2f}°F---\n")

Calculadora()
