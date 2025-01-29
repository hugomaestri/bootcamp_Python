# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, 
# então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor 
# do salário em comparação com o bônus recebido.
from typing import Dict, Any

BONUS_FIXO = 1000

def cadastrar_nome_usuario() -> str:
    nome_valido: bool = False    
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

    return nome

def cadastrar_salario() -> float:
    salario_valido: bool = False
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
    
    return salario

def cadastrar_bonus() -> float:
    bonus_valido: bool = False
    while bonus_valido is not True:
        try:
            bonus: float = float(input("Digite o valor do seu bonus mensal: "))
            if bonus < 0:
                raise ValueError("Bonus não pode ser negativo")
            else:
                bonus_valido = True
        except ValueError as e:
            print(e)

    return bonus

def calcular_kpi_bonus(salario: float, bonus: float) -> float:
    kpi_bonus: float = BONUS_FIXO + salario * bonus
    
    return kpi_bonus

def cadastrar_usuario() -> Dict[str, Any]:
    nome: str = cadastrar_nome_usuario()
    salario: float = cadastrar_salario()
    bonus: float = cadastrar_bonus()
    bonus_recebido: float = calcular_kpi_bonus(salario=salario, bonus=bonus)

    return {"nome": nome, "salario": salario, "bonus": bonus, "bonus_recebido": bonus_recebido}


banco_usuarios: list[Dict[str, Any]] = []

while True:
    banco_usuarios.append(cadastrar_usuario())

    continuar_cadastro = input("\nDeseja cadastrar outro usuário? (s/n): ")

    if continuar_cadastro.lower() == "n":
        break

print(banco_usuarios)