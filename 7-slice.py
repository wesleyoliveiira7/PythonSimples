movieName = "Top Gun"

# string[inicio:fim] - índice começa na posição 0 / indice final - 1

#1 - Buscar toda a string a partir da primeira posição
print (movieName [0:])

#2 - Buscar toda a string até a ultima posição
print (movieName [:7])

#3 - Buscar toda a string da terceira até a ultima posição
print (movieName [2:])

"""
string[inicio:fim:passo]
indice começa na posição 0 / indice final - 1
passo - determina o incremento. Por padrão esse número é o 1.
"""

#4 - Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

#5 - Buscar toda a string nos indices ímpares
print(movieName[1::2])

#6 - Inverter uam string de trás para frente
print(movieName [::-1])