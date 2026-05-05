"""
Escreva um programa que:
Leia cinco números inteiros (podendo haver repetidos).
Armazene-os em um set para eliminar duplicatas.
Imprima:
O set resultante.
A quantidade de elementos únicos.
O maior elemento do set.
Exemplo
Entrada: 4, 7, 4, 9, 7
Saída:
{9, 4, 7}
3
9
"""

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
num4 = int(input("Digite o 4º número: "))
num5 = int(input("Digite o 5º número: "))

numeros_set = {num1, num2, num3, num4, num5}
print(numeros_set)
print(len(numeros_set))
print(max(numeros_set))