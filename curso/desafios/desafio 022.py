print("""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
o nome com todas as letras minusculas
quantas letras ao todo(sem considerar espaços)
quantas letras tem o primeiro nome\n""")

nome = str(input("Digite o seu nome completo: ")).strip()

print("\nSeu nome com todas as letras maiúsculas: {}".format(nome.upper()))
print("Seu nome com todas as letras minusculas: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) -nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))