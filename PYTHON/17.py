import os
os.system("cls || clear")

matricula = int(input("Digite sua matrícula: "))
data_nascimento = int(input("Digite sua data de nascimento (ano): "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))
idade = 2026 - data_nascimento
os.system("cls || clear")

print(f"Matrícula: {matricula}")
print(f"Data de nascimento: {data_nascimento}")
print(f"Tempo de serviço: {tempo_servico} anos")
print(f"Idade: {idade} anos")

if idade >= 65 or tempo_servico >= 30:
    print("Você pode se aposentar")
else:
    print("Você não pode se aposentar pois não atende aos requisitos de idade ou tempo de serviço")
