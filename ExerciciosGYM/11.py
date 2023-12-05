# Faça um programa que solicite o nome completo do usuário e exiba somente o seu segundo nome/primeiro sobrenome.

nome_completo = input("digite o seu nome completo: ")

nome_completo_dividido = nome_completo.split(" ")

print(nome_completo_dividido[1])