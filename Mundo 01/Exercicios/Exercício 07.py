#Programa que leia as notas de um aluno, calcule e mostre a sua média.

np1 = float(input(print("Digite a nota da NP1: ")))
np2 = float(input(print("Digite a nota da NP2: ")))
pim = float(input(print("Digite a nota do PIM: ")))
media = (np1 * 4 + np2 * 4 + pim * 2) / 10
print("A sua média desse semestre é: ", media)