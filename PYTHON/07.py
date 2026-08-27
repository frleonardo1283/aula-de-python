import os
os.system("cls || clear")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

if a > b:
    print(f"O valor de a ({a}) é maior que o valor de b ({b}).")
elif b > a:
    print(f"O valor de b ({b}) é maior que o valor de a ({a}).")
else:
    print(f"Os valores de a ({a}) e b ({b}) são iguais.")