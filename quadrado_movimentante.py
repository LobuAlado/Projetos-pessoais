import pygame
from pygame.locals import *

pygame.init()

tela = pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption("Quadrado Movimentante")
JogoAtivo = True
x = 20
y = 20
while JogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
          JogoAtivo = False

        if evento.type == KEYDOWN:
            if y > 0:
                if evento.key == K_UP:
                    y -= 20
            elif y <= 0:
                y = 480

            if y < 500:
                if evento.key == K_DOWN:
                    y += 20
            elif y >= 500:
                y = 10

            if x < 500:    
                if evento.key == K_RIGHT:
                     x += 20
            elif x >=500:
                x = 10

            if x > 0:    
                if evento.key == K_LEFT:
                    x -= 20
            elif x <= 0:
                x = 480

    tela.fill((255,255,255))
    pygame.draw.rect(tela,(255,0,0),(x,y,20,20),0)
    pygame.display.flip() 
    
