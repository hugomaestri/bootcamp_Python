# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, 
# então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor 
# do salário em comparação com o bônus recebido.

BONUS_FIXO = 1000

nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while nome_valido is not True:
    try:
        nome: str = input("Digite seu nome: ")
        if nome == "":
            raise ValueError("Nome não pode estar em branco")
        elif nome.isnumeric():
            raise ValueError("Nome não pode ser numérico")
        elif any(letra.isdigit() for letra in nome):
            raise ValueError("Nome não pode conter números")
        elif nome.isspace():
            raise ValueError("Nome não pode ser apenas espaços")
        else:
            nome_valido = True
    except ValueError as e:
        print(e)

while salario_valido is not True:
    try:
        salario: float = float(input("Digite o valor do seu salário mensal: "))
        if salario < 0:
            raise ValueError("Salário não pode ser negativo")
        if salario == 0:
            raise ValueError("Salário não pode ser zero")
        else:
            salario_valido = True
    except ValueError as e:
        print(e)

while bonus_valido is not True:
    try:
        bonus: float = float(input("Digite o valor do seu bonus mensal: "))
        if bonus < 0:
            raise ValueError("Bonus não pode ser negativo")
        else:
            bonus_valido = True
    except ValueError as e:
        print(e)
        
kpi_bonus: float = BONUS_FIXO + salario * bonus

print(f"Olá, {nome}. Seu salário é de R$ {salario:.2f} e o seu bônus recebido foi de R$ {kpi_bonus:.2f}")
