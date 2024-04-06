import pygame
from pygame.locals import *
from sys import exit 
from random import randint

pygame.init()


#Opcional
#pygame.mixer.mixer_music.set_volume(0.1)
#musica_de_fundo = pygame.mixer.music('')
#barulho_da_colisao = pygame.mixer.music('')
#pygame.mixer.music.play(-1)
fonte = pygame.font.SysFont('arial',40,bold=True,italic=True)
#Opcional

largura = 640
altura = 480
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((640,480))
pygame.display.set_caption("pong")

xraquete = 150
yraquete = 468

#Posição da Bolinha
x = 0
y = 0
#-------------#
#Direção da Bolinha
Direita = True
Subir = True 
#-------------#

velocidade = 10
pontos = 0


#Atualizar a tela
while True:
    relogio.tick(15)
    tela.fill((255,255,255))
    mensagem=f"Pontuação.: {pontos}"
    texto_formatado = fonte.render(mensagem, True,(0,0,0,0) ) 
    tela.blit(texto_formatado,(largura/2, altura/2))
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_a]:
            xraquete = xraquete - 15
        elif pygame.key.get_pressed()[K_l]:
            xraquete = xraquete + 15
    if xraquete + 100 >largura:
        xraquete = largura - 100
    elif xraquete < 0 : 
        xraquete = 0
    if not Subir:
        y = y + velocidade
    else:
        y = y - velocidade          
    if not Direita:
        x = x + velocidade
    else:
        x = x - velocidade 
    if x > largura:
        Direita = not Direita
    elif x < 0:
        Direita = not Direita 
    if y > altura:
        print("YOU FAIL!")
        exit()
    if(y < 0):
        Subir = not Subir
    
    raquete=pygame.draw.rect(tela,(255,0,0),(xraquete,yraquete,100,12))
    bola=pygame.draw.circle(tela,(0,0,255),(x,y),10)
    if bola.colliderect(raquete):
        pontos = pontos+1
        Subir = not Subir
        #barulho_da_colisao.play() #Opicional
        if Direita:
            x = x + randint(0,25)
        else:
            x = x - randint(0,25)
    pygame.display.update()