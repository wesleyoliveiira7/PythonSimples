"""
Escreva um programa que leia uma palavra e um número inteiro n.
O programa deve:
Imprimir a palavra duas vezes concatenada (sem espaço).
Imprimir a palavra repetida n vezes (usando multiplicação de string).
Exemplo
Entrada:
Python
3
Saída:
PythonPython
PythonPythonPython
"""

palavra = input("Digite uma palavra: ")
n = int(input("Digite um número: "))

print(palavra + palavra)
print(palavra * n)