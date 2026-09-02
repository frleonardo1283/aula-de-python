import os
os.system("cls || clear")

peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))
os.system("cls || clear")
imc = peso / (altura *2)

print(f"Peso: {peso:.2f} kg")
print(f"Altura: {altura:.2f} m")
if imc < 18.5:
    print(f"Seu IMC é: {imc:.2f}. Você está abaixo do peso")
elif 18.5 <= imc < 25:
    print(f"Seu IMC é: {imc:.2f}. Você está com o peso normal")
elif 25 <= imc < 30:
    print(f"Seu IMC é: {imc:.2f}. Você está com sobrepeso")
else:
    print(f"Seu IMC é: {imc:.2f}. Você está obeso")