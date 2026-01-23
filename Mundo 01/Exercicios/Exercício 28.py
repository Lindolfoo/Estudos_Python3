#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

computador = random.randint(0, 5) 
print("=" *60)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("=" *60)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(1)
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}!".format(computador, jogador))
