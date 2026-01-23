#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

print("=" *40)
print("Velocidade máxima permitida: 80 km/h")
print("=" *40)
velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("MULTADO! Você excedeu o limite de velocidade que é de 80 km/h")
    print("Você deve pagar uma multa de R$ {:.2f}".format(multa))
else:
    print("Tenha um bom dia! Dirija com segurança!")