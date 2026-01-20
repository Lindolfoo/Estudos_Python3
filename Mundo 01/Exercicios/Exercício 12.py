#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto: R$"))
novo_preco = preco - (preco * 5 / 100)
print(f"O preço do produto com 5% de desconto é R${novo_preco:.2f}")