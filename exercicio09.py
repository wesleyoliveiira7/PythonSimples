"""
Escreva um programa que:
Leia o nome de três produtos e seus respectivos preços.
Armazene os dados em um dicionário, onde a chave é o nome do produto e o valor é o preço (float).
Imprima:
O dicionário completo.
O produto mais caro.
A média dos preços.
Exemplo
Entrada: Arroz: 15.50, Feijão :8.90, Macarrão: 6.75
Saída:{'Arroz': 15.5, 'Feijão': 8.9, 'Macarrão': 6.75}
Arroz
10.38
"""

produtos = {
    "Arroz": 15.50,
    "Feijão": 8.90,
    "Macarrão": 6.75
}

print(produtos)

produto_mais_caro = max(produtos, key=produtos.get)
print(produto_mais_caro)


media = sum(produtos.values()) / len(produtos)
print(f"{media:.2f}")
