#Faça um programa que inicialize uma lista com vários números diferentes, depois disso, solicite ao usuário um número, verifique se o número está ou não na lista e exiba uma mensagem notificando o usuário do resultado.

numeros = [1,5,6,7,8,9]

numero_digitados = int(input("Digite um numero: "))

if numero_digitados in numeros:
    print(f"o numero {numero_digitados} está na lista ")
else:
    print(f"infelizmente o numero {numero_digitados} não está na lista ")
    
    