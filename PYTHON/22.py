
import os
os.system("cls || clear")

nota = 0
soma = 0
while True:
    nota = float(input("Digite sua nota desejada: "))
    soma += nota
    escolha = input("Deseja colocar mais uma nota? (s/n): ").lower()

    if escolha == "n":
        break
media = soma / 2
clear = os.system("cls || clear")
print(f"Sua média é: {media}")