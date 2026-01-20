#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

real = float(input("Digite quantos reais você tem na carteira: R$"))
dolar = real / 5.40
print(f"Com R${real} você pode comprar US${dolar:.2f}")