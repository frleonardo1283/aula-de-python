import os
os.system("cls || clear")

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
media = (primeiro_numero + segundo_numero) /2
produto = primeiro_numero * segundo_numero

if primeiro_numero > segundo_numero:
    print(f"O primeiro número ({primeiro_numero}) é maior que o segundo número ({segundo_numero}).")
elif segundo_numero > primeiro_numero:
    print(f"O segundo número ({segundo_numero}) é maior que o primeiro número ({primeiro_numero}).")
else:
    print(f"O número {primeiro_numero} é igual ao número {segundo_numero}.")

print(f"A média dos números é {media:.2f}.")
print(f"O produto dos números é {produto:.2f}.")