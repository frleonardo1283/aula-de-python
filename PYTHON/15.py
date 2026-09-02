import os
os.system("cls || clear")

aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
os.system("cls || clear")

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
else:
    conceito = "D"

print(f"Aluno: {aluno}")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
if conceito in ["A", "B", "C"]:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")