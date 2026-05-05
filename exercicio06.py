"""
Escreva um programa que:
Leia 3 números inteiros.
Armazene esses números em uma lista.
Imprima:
A lista completa.
O primeiro elemento da lista.
A soma de todos os elementos da lista.
Exemplo
Entrada:5,7,2
Saída:[5, 7, 2]
5
14
"""
# Passo 1: Ler os números do usuário
num1 = int(input("Digite um Número:\n"))
num2 = int(input("Digite um Número:\n"))
num3 = int(input("Digite um Número:\n"))

# Passo 2: Armazenar em uma lista
lista = [num1, num2, num3]

# Passo 3: Imprimir os resultados
print(lista)            # lista completa
print(lista[0])         # primeiro elemento
print(sum(lista))       # soma dos elementos