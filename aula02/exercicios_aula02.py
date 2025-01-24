import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
"""numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
soma = numero_01 + numero_02
print(f"A soma dos números é {soma}")"""

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
"""CONSTANTE = 5
numero = int(input("Digite um número: "))
resto = numero % CONSTANTE
print(f"O resto da divisão de {numero} por {CONSTANTE} é {resto}")"""

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
"""numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
multiplicacao = numero_01 * numero_02
print(f"A multiplicação dos números é {multiplicacao}")"""

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
"""numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print(resultado)"""

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
"""numero = int(input("Digite um número: "))
numero_ao_quadrado = numero ** 2
print(f"O número {numero} ao quadrado é {numero_ao_quadrado}")"""


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
"""numero_01 = float(input("Inserir um numero decimal: "))
numero_02 = float(input("Inserir outro numero decimal: "))
soma = numero_01 + numero_02
print(f"A soma dos números é {soma}")"""

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
"""numero_01 = float(input("Inserir um numero: "))
numero_02 = float(input("Inserir outro numero: "))
media = (numero_01 + numero_02) / 2
print(f"A média dos números é {media}")"""

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
"""base = float(input("Digite o número base: "))
expoente = float(input("Digite o número expoente: "))
potencia = base ** expoente
print(f"A potência de {base} elevado a {expoente} é {potencia}")"""

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
"""temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é {temperatura_fahrenheit:.2f}")"""

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
"""raio_circulo = float(input("Digite o raio do circulo: "))
area_circulo = math.pi * (raio_circulo ** 2)
print(f"A área do círculo é {area_circulo:.2f}")"""

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
"""data_usuario = input("Insira uma data no formad dd/mm/aaaa: ")
data_separada = data_usuario.split("/")

print(f"Dia: {data_separada[0]}\n"+
      f"Mês: {data_separada[1]}\n"+
      f"Ano: {data_separada[2]}")"""


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

# numero = int(input("Insira um numero: "))
# if isinstance(numero, int):
#     print("A variável é um inteiro")
# else:
#     print("A variável não é um inteiro")