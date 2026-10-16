import os
os.system("cls")

cardapio = {
    1: ["Picanha", 25.00],
    2: ["Lasanha", 20.00],
    3: ["Strogonoff", 18.00],
    4: ["Bife Acebolado", 15.00],
    5: ["Pão com ovo", 5.00]
}

pratos_escolhidos = []
total_conta = 0.0

while True:
    os.system("cls" if os.name == "nt" else "clear")
    
    print("=== MENU DE OPÇÕES ===")
    print(f"{'Código':<8} | {'Proteina':<15} | {'Valor'}")
    print("-" * 38)
    
    for codigo, dados in cardapio.items():
        print(f"{codigo:<8} | {dados[0]:<15} | R$ {dados[1]:.2f}")
    
    print("-" * 38)
    
    try:
        opcao = int(input("Digite o código da proteina desejada: "))
        if opcao in cardapio:
            prato_nome = cardapio[opcao][0]
            prato_valor = cardapio[opcao][1]
            
            pratos_escolhidos.append((prato_nome, prato_valor))
            total_conta += prato_valor
            print(f"'{prato_nome}' adicionado com sucesso!")
        else:
            print("Código inválido! Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")
        
    continuar = input("\nDeseja escolher outra proteina? (s/n): ").strip().lower()
    if continuar != 's':
        break

os.system("cls")
print("=== RESUMO DO PEDIDO ===")
if pratos_escolhidos:
    print(f"{'Proteina':<15} | {'Valor'}")
    print("-" * 25)
    for nome, valor in pratos_escolhidos:
        print(f"{nome:<15} | R$ {valor:.2f}")
    print("-" * 25)
    print(f"Valor total da conta: R$ {total_conta:.2f}")
else:
    print("Nenhum prato foi escolhido.")