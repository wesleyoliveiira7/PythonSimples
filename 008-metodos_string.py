movieName = "Top Gun"
movieDescripton = """
Narra a história de Pete "Maverick" Mitchell, 
um talentoso e rebelde piloto da Marinha dos EUA que busca superar traumas pessoais e se tornar o melhor caça na escola.
"""
print(movieName.upper()) #TUDO MAIÚSCULO
print(movieName.lower()) #tudo minúsculo
print(movieName.capitalize()) #Primeira letra maiúscula
print(movieName.title()) #Primeira Letra Maiúscula
print(movieName.center(10, '-')) # Retorna a string centralizada com caractere de preenchimento
print(movieName.find("u")) #Retorna a posição de um determinado caractere
print(movieName.find("o")) # Conta caracteres
print(movieName.replace("Top", "Shot")) #Altera elemento por outro
print(movieName.split(','))