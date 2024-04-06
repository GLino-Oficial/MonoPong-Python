#INSTALAR 
#Python - Navegador
#Py Pack - Visual Studio Code
#Pygame -Via Terminal 
#--------------------------------------#

import pygame
from pygame.locals import * 
from sys import exit
from random import randint


#Opcional
#pygame.mixer_music.set_volume(0.1)
#musica_de_fundo = pygame.mixer.music('')
#barulho_da_colisao = pygame.mixer.music('')
#pygame.mixer.music.play(-1)
#--------------------------------
fonte = pygame.font.SysFont('arial',40,bold=True,italic=True)

#Janela/Tela do jogo
largura = 640
altura = 480
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((640,480))
pygame.display.set_caption("pong")

#Posição da raquete
xraquete = 150
yraquete = 468

#Posição da Bolinha
x = 0
y = 0

#Direção da Bolinha
Direita = True
Subir = True

#Referente a bolinha
velocidade = 10

#Pontuação Inicial
pontos = 0