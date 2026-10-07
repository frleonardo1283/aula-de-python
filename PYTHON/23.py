import os
os.system ("clear")

while True:
    print("1 - cadastrar familia \n2 - sair e exibir resultado")
    opção= input("Digite a opção desejada: ").strip()

match opção:
        case "1":
            print("Cadastro de familia")
            nome= input("Digite o nome da familia: ")
            quantidade= int(input("Digite a quantidade de pessoas na familia: "))
            renda= float(input("Digite a renda da familia: "))
            print(f"Familia cadastrada: {nome}, {quantidade} pessoas, renda de R${renda:.2f}")
        case "2":
            print("Saindo do programa...")
            break