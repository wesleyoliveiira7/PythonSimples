"""
1- Escreva uma programa que lê dois nomes e retorne uma string formatada no formato "ÚltimoNome, PrimeiroNome".
2- Inverta a ordem das palavras em uma string fornecida.
3-Verifique se uma string fornecida é um palíndromo (pode ser lida da mesma forma de trás para frente).
"""
#1
primeiroNome = input("Digite o nome:\n")
segundoNome = input("Digite o sobrenome:\n")

nomeFormatado = f"{segundoNome} {primeiroNome}"
print (nomeFormatado)

#2
texto = "Brasil é Penta"
palavras = texto.split()
textoInvertido = " ".join(palavras[::-1])
print(textoInvertido)

#3
texto1 = "Champions"
texto2 = "Real Madrid"

#Remove espaço e deixe nome em minúsculo
texto1_format = texto1.lower().replace(" ", "")
texto2_format = texto2.lower().replace(" ", "")

#Verificar se o texto original é igual ao reverso

palindromo1 = texto1_format == texto1 [::-1]
palindromo2 = texto2_format == texto1 [::-1]

print(palindromo1)
print(palindromo2)