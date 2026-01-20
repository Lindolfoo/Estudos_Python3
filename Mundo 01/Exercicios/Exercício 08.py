#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input(print("Digite uma medida: ")))
km = medida / 1000
hm = medida / 100
dam = medida / 10
m = medida
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f"KM: {km} metros | HM: {hm} metros | DAM: {dam} metros | M: {m} metros | DM: {dm} metros | CM: {cm} metros | MM: {mm} metros")
