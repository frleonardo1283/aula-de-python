import os
os.system("cls")

vetor_numeros = []
quantidade_notas = int(input("Digite a quantidade de notas: "))

for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    if nota < 0:
        nota = 0
    vetor_numeros.append(nota)
    
os.system("cls")

print("Notas digitadas:")
for nota in vetor_numeros:
    print(nota)