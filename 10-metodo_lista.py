filmsList = ["Inception", "The Shawshank Redemption",
             "The Dark Knight", "Pulp Fiction", "Interstellar"]

#1 - Tamanho da Lista
print(len(filmsList))

#2 - Recuperar um item da lista pelo nome
print(filmsList.index("Interstellar"))

#3 - Adicionar item ao final da Lista
filmsList.append("The Lord of the Rings")
print(filmsList)

#4 - Ordenar a Lista
filmsList.sort()
print(filmsList)

#5 - Copiar os itens de uma lista para outra
filmscopy = filmsList.copy()
filmscopy.remove("Pulp Fiction")
print(filmscopy)

#6 - Remove todos os itens da lista
filmsList.clear()
print(filmsList)