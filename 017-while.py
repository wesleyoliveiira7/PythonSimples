movieList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

#1-Interando valores de uma lista de filmes usando while
index = 0
while index < len (movieList):
    print(movieList[index])
    index += 1

#2- Quando a condição for atendida, o loop será encerrado
index = 0
while index < len (movieList):
    if movieList[index] == "Inception":
        break
    print(movieList[index])
    index += 1

#3 Quando a condição for atendida, o loop vai para a proxima interação
index = 0
while index < len (movieList):
    if movieList[index] == "Inception":
        index += 1
        continue
    print(movieList[index])
    index += 1

#4- Avaliação do Filme com while
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer?\n"))

total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filmes:\n"))
    total += note
    count += 1

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")
