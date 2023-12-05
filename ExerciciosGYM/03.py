#3. Faça um algoritmo que solicite um número ao usuário, depois disso, escreva True no console, caso o número tenha dois dígitos (Esteja entre 10 e 99), caso contrário escreva False.

numero = int(input("digite um numero: "))

dois_numeros = numero >=10 and numero <= 99

print(dois_numeros)