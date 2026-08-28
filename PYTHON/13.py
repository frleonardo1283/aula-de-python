import os
os.system("cls || clear")

idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("menores de idade não votam")
elif idade >= 16 and idade < 18:
    print("voto opcional")
elif idade >= 18 and idade < 65:
    print("vota obrigatoriamente")
elif idade == 666:
    print("Oi Belzebu")
else:
    print("voto opcional")