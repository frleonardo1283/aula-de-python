import os
os.system("cls || clear")

usuario = input("digite seu usuario: ")
media = float(input("digite sua media: "))
faltas = int(input("digite suas faltas: "))
os.system("cls || clear")

print(f"Aluno: {usuario}")
print(f"Media: {media}")
print(f"Faltas: {faltas}")

if media >= 7 and faltas <= 40:
    print(f"O aluno {usuario} esta aprovado")
elif media < 7 and faltas <= 40:
    print(f"O aluno {usuario} esta reprovado por nota")
elif media >= 7 and faltas > 40:
    print(f"O aluno {usuario} esta reprovado por faltas")
else:
    print(f"O aluno {usuario} esta reprovado por nota e faltas")