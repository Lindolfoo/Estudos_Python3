#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salário do funcionário: "))

if salario > 1850:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print(f"O valor do aumento é: R$ {aumento:.2f}")