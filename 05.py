#Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso, faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.

ano_nascimento = int(input("Digite o ano que você nasceu: "))

ano_atual = 2023

idade = ano_atual - ano_nascimento

if idade == 18:
    print("Você faz 18 anos este ano!")
elif idade > 18:
    print("Você já completou 18 anos.")
else:
    print("Você ainda não completou 18 anos.")
