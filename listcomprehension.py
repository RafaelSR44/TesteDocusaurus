# Utilizando o recurso de list comprehensions:

# Lista base
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Criando uma lista de quadrados
## Estrutura: [expressão for item in lista]
quadrados = [x * x for x in lista]
print(quadrados)