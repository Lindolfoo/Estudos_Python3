#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
''' Descobri o problema, a versão do meu python não é compatível com a biblioteca pygame.
import pygame
pygame.mixer.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
input("Pressione Enter para encerrar o programa.")
pygame.mixer.music.stop() '''

import os
os.startfile("Smiling.mp3")
