import os
os.system("cls || clear")

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: ")) 
terceira_nota = float(input("Digite a terceira nota: "))
media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    print(f"A média é {media:.2f}. Aprovado")
else:
    print(f"A média é {media:.2f}. Reprovado")