import os
os.system("cls || clear")

print("= solicitação de dados =")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
media = (primeira_nota + segunda_nota) / 2

print("\n= resultados =")
print("nome:", nome)
print("idade:", idade)
print("primeira nota:", primeira_nota)
print("segunda nota:", segunda_nota)
print("média:", media)