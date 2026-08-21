import os
os.system("cls || clear")

print("solicitação de dados")
valor = float(input("Digite um valor: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
desconto = valor * (percentual_desconto / 100)
valor_final = valor - desconto

print("\n= resultados =")
print(f"valor: {valor:.2f}")
print(f"desconto: {desconto:.2f}")
print(f"valor final: {valor_final:.2f}")