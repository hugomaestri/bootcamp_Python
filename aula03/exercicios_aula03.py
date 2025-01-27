### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
"""quantidade = 40
preco = 20

if quantidade > 0 and preco > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")"""

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
"""try:
    temperatura = float(input("Digite a temperatura: "))
except ValueError:
    print("Valor inválido. Digite um número.")
    exit()

if temperatura < 18:
    print("Temperatura Baixa")
elif temperatura >= 18 and temperatura <= 27:
    print("Temperatura Normal")
else:
    print("Temperatura Alta")"""

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
"""log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print(log['message'])"""

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
"""idade = 25
email = "seu_email@gmail.com"

if isinstance(idade, int) and 18 <= idade <= 65:
    if "@" in email and "." in email:
        print("Dados de usuário válidos")
    else:
        print("Email inválido")
else:
    print("Idade inválida, deve ser um número inteiro entre 18 e 65")"""

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
"""transacao = {"valor": 11000, "hora": 19}
if (transacao["valor"] < 10000 or 9 <= transacao["hora"] <= 18):
    print("Transação normal")
else:
    print("Transação suspeita")"""

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
"""texto = "Hoje é nossa terceira aula do bootcamp: bootcamp de Python"
novo_texto = texto.replace(":", "")
palavras = novo_texto.split(" ")
contagem_de_palavras = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] += 1
    else:
        contagem_de_palavras[palavra] = 1

print(contagem_de_palavras)"""


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
"""numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
numeros_normalizados = []
for numero in numeros:
    numero_normalizado = (numero - minimo) / (maximo - minimo)
    numeros_normalizados.append(numero_normalizado)

print(numeros_normalizados)"""

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico 
"""usuarios = [
    {"nome": "Hugo", "idade": 20, "email": "meu_email@exemplo.com"},
    {"nome": "José", "idade": 40, "email": ""},
    {"nome": "Carlos", "idade": 18, "email": "carlos@exemplo.com"},
]

usuarios_filtrado = [usuario for usuario in usuarios if usuario["email"] != ""]
print(usuarios_filtrado)"""

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
"""numeros = range(1, 21)
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros_pares)"""

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
"""vendas = [
    {"produto": "A", "categoria": "cat1", "valor": 10},
    {"produto": "B", "categoria": "cat3", "valor": 5},
    {"produto": "A", "categoria": "cat2", "valor": 20},
    {"produto": "C", "categoria": "cat1", "valor": 50},
    {"produto": "B", "categoria": "cat3", "valor": 10}
]
total_por_categoria = {}
for venda in vendas:
    if venda["categoria"] in total_por_categoria:
        total_por_categoria[venda["categoria"]] += venda["valor"]
    else:
        total_por_categoria[venda["categoria"]] = venda["valor"]

total_por_categoria = dict(sorted(total_por_categoria.items()))
print(total_por_categoria)"""

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
"""dados = []
flag = ""
while flag.lower().strip() != "sair":
    flag  = input("Digite um valor ou 'sair' para terminar: ")
    if flag.lower().strip() != "sair":
        dados.append(flag)
print(dados)"""

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
"""numero = int(input("Digite um número entre 1 e 100: "))
while numero < 1 or numero > 100:
    print("Número fora do intervalo!")
    numero = int(input("Digite um número entre 1 e 100: "))
print(f"Número {numero} válido!")"""

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
"""pagina_atual = 1
paginas_totais = 5

while pagina_atual <= paginas_totais:
    print(f"Processando {pagina_atual} de {paginas_totais}")
    pagina_atual += 1
print("Dados processados com sucesso!")"""

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
"""tentativas = 1
maximo_tentativas = 5
sucesso = True
while tentativas <= maximo_tentativas:
    if sucesso == True:
        print("Conexão estabelecida!")
        break
    print(f"Tentativa {tentativas} de {maximo_tentativas}")
    tentativas += 1
if tentativas > maximo_tentativas:
    print(f"Limite de tentativas atingiddo após {tentativas-1} tentativas.")"""

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
itens = [1, 2, 3, 4, 5, "abc", 6, "parar", 7, 8]
i = 0
while i < len(itens):
    if itens[i] == "parar":
        print(f"Condição de parada encontrada no elemento {i}")
        break
    print(f"Processando item {i} = {itens[i]}")
    i += 1