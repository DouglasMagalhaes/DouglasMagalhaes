# O for em Python é usado para percorrer itens de uma sequência 
# (como listas, strings, tuplas, dicionários ou um range de números).

# Lista de nomes
familiares = ['Joelma', 'Larissa', 'Douglas', 'Lara']

# Criando um laço for para mostrar os nomes de uma lista
# enumerate() retorna tanto o índice (i) quanto o valor (name) de cada item da lista
# O parâmetro start=1 faz com que a contagem comece em 1, em vez de 0
for i, name in enumerate(amigos, start=1):  
    # Exibe o número e o nome correspondente
    print(f"{i}. {name}")
