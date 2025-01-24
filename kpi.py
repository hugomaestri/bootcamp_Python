# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, 
# então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor 
# do salário em comparação com o bônus recebido.

BONUS_FIXO = 1000
nome = input("Digite seu nome: ")
salario = float(input("Digite o valor do seu salário mensal: "))
bonus = float(input("Digite o valor do bônus que você recebeu: "))
kpi_bonus = BONUS_FIXO + salario * bonus

print(f"Olá, {nome}. Seu salário é de R$ {salario:.2f} e o seu bônus recebido foi de R$ {kpi_bonus:.2f}")
