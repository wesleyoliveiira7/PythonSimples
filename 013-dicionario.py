filmInception = {
    "title": "Inception",
    "yearRelease": 2010,
    "imdbRating":8.8,
    "genre":["Sci_fi", "Action", "Thriller"]
}
print(filmInception)
print(len(filmInception))
print(type(filmInception))

#1- Recuperar um elemento do dicionario
print(filmInception["genre"])
print(filmInception.get("imdRating"))

#2- Buscar apenas as chaves do dicionário
print(filmInception.keys())

#3- Buscar apenas os valores do dicionario
print(filmInception.values())

#4- Buscar itens do dicionario com chave e valor
print(filmInception.items())

#5- Adicionar itens no dicionario
filmInception["director"] = "Cristopher Nolan"
print(filmInception)

#6- Atualizar itens no dicionario
filmInception.update({"imdbRating": 8.7})
print(filmInception)

#7- Remover item no dicionario
filmInception.pop("director")
print(filmInception)