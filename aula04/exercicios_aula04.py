### 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
"""numeros: int = range(1, 11)
for numero in numeros:
    print(numero ** 2)"""

### 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
"""linguagens: list = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.insert(2, "Ruby")
print(linguagens)"""

### 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
"""from typing import Dict, Any

livro_1: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 1996
}

livro_2: Dict[str, Any] = {
    "Titulo": "Game of Thrones 2",
    "Autor": "George R. R. Martin",
    "Ano": 2000
}
lista_de_elementos: list = livro_1.items()
for elemento in lista_de_elementos:
    print(elemento)
print("\n")

#########
lista_de_livros: list = []
lista_de_livros.append(livro_1)
lista_de_livros.append(livro_2)
print(lista_de_livros)
print("\n")

#########
lista_de_livros_usando_dict: dict = {
    "livro_01": {
        "Titulo": "Game of Thrones",
        "Autor": "George R. R. Martin",
        "Ano": 1996},

    "livro_02": {
        "Titulo": "Game of Thrones 2",
        "Autor": "George R. R. Martin",
        "Ano": 2000},
}
print(lista_de_livros_usando_dict)
print(lista_de_livros_usando_dict["livro_01"])
print(lista_de_livros_usando_dict["livro_01"]["Titulo"])"""

### 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
"""texto: str = "Codigo em python para contagem de caracteres"
ocorrencias: dict[str, int] = {}
for caractere in texto:
    if caractere in ocorrencias:
        ocorrencias[caractere] += 1
    else:
        ocorrencias[caractere] = 1

print(ocorrencias)"""

### 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
"""frutas: list = ["maçã", "banana", "cereja"]
precos: dict[str, float] = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
preco_total: float = 0
for fruta in frutas:
    preco_total += precos[fruta]
print(f"O preço total da lista de compras é R$ {preco_total:.2f}")

##### OU
# frutas: list = ["maçã", "banana", "cereja"]
# precos: dict[str, float] = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# preco_total: float = sum([precos[fruta] for fruta in frutas])
# print(f"O preço total da lista de compras é R$ {preco_total:.2f}")"""


### 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
"""emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos: list = list(set(emails))
print(emails_unicos)
print(type(emails_unicos))"""

### 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
"""idades: list = [12, 15, 18, 21, 30, 40, 50]
idades_maior_igual_18: list = [idade for idade in idades if idade >= 18]
print(idades_maior_igual_18)"""

### 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
"""from typing import Dict, Any
pessoas: list[Dict[str, Any]] = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Eve", "idade": 25},
    {"nome": "Carol", "idade": 20},
    {"nome": "Hugo", "idade": 28},
    {"nome": "Alice", "idade": 22},
    {"nome": "Alice", "idade": 38},
    {"nome": "Bob", "idade": 25}    
]
pessoas_ordenadas: list[Dict[str, Any]] = sorted(pessoas, key=lambda x: (x["nome"], x["idade"]))
print(pessoas_ordenadas)"""

### 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
"""numeros: list[int] = [10, 20, 30, 40, 50]
media: float = sum(numeros) / len(numeros)
print(f"A média dos números é {media}")"""

### 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
"""valores: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_pares: list[int] = [valor for valor in valores if valor % 2 == 0]
valores_impares: list[int] = [valor for valor in valores if valor % 2 != 0]

print(f"Valores pares: {valores_pares}")
print(f"Valores ímpares: {valores_impares}")
"""
### 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

produtos[1]["preço"] = 90
print(produtos)

### 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

### 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

### 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

### 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.