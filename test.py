import pygame
import os
import time

pygame.init()
screen = pygame.display.set_mode((600,950))
world = pygame.Surface((600,800))
world = pygame.image.load('images\\lvl 1\\background_stone.png')
cadre_haut = pygame.Surface((600,150))
cadre_haut.fill((0,0,0))
#cadre_lvl = pygame.Surface((100,75))
#cadre_lvl.fill((0,0,255))
img_fin = pygame.Surface((600,950))
img_fin = pygame.image.load('images\\lvl 1\\background_stone.png')

time_debut = time.time()
police_timer = pygame.font.SysFont("monospace" ,20)
police_lvl = pygame.font.SysFont("monospace" ,40)
level = 1
licorne = True
while licorne:
    screen.blit(world,(0,150))
    screen.blit(cadre_haut,(0,0))
    #screen.blit(cadre_lvl,(250,37.5))
    affichage_lvl = police_lvl.render(str(level) , 1 , (255,0,0))
    screen.blit(affichage_lvl, (290,55))
    timer = time.time() - time_debut
    affichage_timer = police_timer.render(time.strftime('%M:%S',time.gmtime(timer)), 1 , (255,0,0))
    screen.blit(affichage_timer, (480,65))
    time.sleep(1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                screen.blit(img_fin,(0,0))
                pygame.quit
                licorne = False# Ecrit ton programme ici ;-)
