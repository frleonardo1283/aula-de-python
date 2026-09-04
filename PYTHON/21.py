import os
os.system("cls || clear")

nota = float(input("digite sua nota: "))
os.system("cls || clear")

print(f"Sua nota: {nota}")

if nota >= 0 and nota <= 10:
    print("Sua nota esta entre 0 e 10")
else:
    print("Sua nota não esta entre 0 e 10")
