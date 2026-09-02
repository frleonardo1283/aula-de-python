import os
os.system("cls || clear")

maca = int(input("Digite a quantidade de maçãs: "))
if maca < 12:
    preço = maca * 1.30
    print(f"O preço total é: R${preço:.2f}")
else:
    preço = maca * 1.00
    print(f"O preço total é: R${preço:.2f}")
print(f"quantidade de maçãs compradas: {maca}")