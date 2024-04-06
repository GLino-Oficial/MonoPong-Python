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

largura = 640
altura = 480
relogio = pygame.time.Clock()