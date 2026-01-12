# Exemplo para trabalhar com sets

amigos = {'João', 'Maria', 'José', 'Ana', 'João', 'Maria'}
amigos_fora = {'José', 'Ana', 'João'}

# Diferença entre sets
print("Diferença:" ,amigos.difference(amigos_fora))

# Total de elementos distintos - União dos sets
print("União:", amigos.union(amigos_fora))

# Interseção
print("Interseção:", amigos.intersection(amigos_fora))