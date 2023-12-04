# Faça um programa que inicialize uma lista vazia e a preencha com 5 nomes diferentes digitados pelo usuário, depois disso solicite um número de 0 até 4 e remova o elemento desta posição.

nomes = []

nomes.append(input("Digite o primeiro nome: "))
nomes.append(input("Digite o segundo  nome: "))
nomes.append(input("Digite o terceiro nome: "))
nomes.append(input("Digite o quarto nome: "))
nomes.append(input("Digite o quinto nome: "))

excluir = int(input(" escolha uma posição de 0 até 4 para excluir:"))

del nomes[excluir]
print(nomes)