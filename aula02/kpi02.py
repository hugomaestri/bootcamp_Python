# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, 
# então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor 
# do salário em comparação com o bônus recebido.

BONUS_FIXO = 1000

try:
    nome = input("Digite seu nome: ")
    if nome == "":
        raise ValueError("Nome não pode estar em branco")
    elif nome.isnumeric():
        raise ValueError("Nome não pode ser numérico")
    elif any(letra.isdigit() for letra in nome):
        raise ValueError("Nome não pode conter números")
    elif nome.isspace():
        raise ValueError("Nome não pode ser apenas espaços")
except ValueError as e:
    print(e)
    exit()
    

try:
    salario = float(input("Digite o valor do seu salário mensal: "))
    if salario < 0:
        raise ValueError("Salário não pode ser negativo")
    if salario == 0:
        raise ValueError("Salário não pode ser zero")
except ValueError as e:
    print(e)
    exit()

try:
    bonus = float(input("Digite o valor do seu bonus mensal: "))
    if bonus < 0:
        raise ValueError("Bonus não pode ser negativo")
except ValueError as e:
    print(e)
    exit()
    
kpi_bonus = BONUS_FIXO + salario * bonus

print(f"Olá, {nome}. Seu salário é de R$ {salario:.2f} e o seu bônus recebido foi de R$ {kpi_bonus:.2f}")
