#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite o nome completo de uma pessoa: ").strip()
nome_dividido = nome.split()
print(f"Primeiro nome: {nome_dividido[0]}")
print(f"Último nome: {nome_dividido[-1]}")
