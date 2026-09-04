import os
os.system("cls || clear")

login = input("digite seu login: ")
senha = input("digite sua senha: ")
os.system("cls || clear")

if login == "Mist" and senha == "1283":
    print("Login bem-sucedido")
else:
    print("Login ou senha incorretos")