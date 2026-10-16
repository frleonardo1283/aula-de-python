import os
os.system ("cls")

livros = []
for i in range(3):
    livro = input(f"Digite o nome do livro {i+1}: ")
    livros.append(livro)

os.system("cls")

print("nome dos livros digitados:")
for livro in livros:
    print(livro)
