#Faça um programa que solicite a idade do usuário, verifique se o texto informado só contém números. Caso contenha somente números exiba a mensagem: "Você tem {idade digitada} anos.", caso contrário exiba a mensagem: "Você digitou uma idade inválida".

idade = (input("digite a sua idade: "))

if idade.isdigit():
    
    print(f"voce tem {idade} anos!")
else:
    print("Digite uma idade válida")
    
    