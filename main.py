import pygame
from player import Player
from map import Map
import os
import sys
import time

#pygame.init()
pygame.font.init()

def render_map(world,map):
    '''Affiche tout les blocs du niveau'''
    for x,y,image in map.render_map():
        world.blit(image,(x,y))


def main(level):
    '''boucle de jeu principale'''
    #initialise l'écran pour afficher le monde
    screen = pygame.display.set_mode((608,950))
    cadre_haut = pygame.image.load(os.path.join(os.getcwd(),'images','look_final.png'))
    world = pygame.Surface( (608,800) )
    #initialise le timer
    time_debut = time.time()
    police_lvl = pygame.font.SysFont("monospace" ,40)
    #initialise le joueur et la carte
    player = Player(4)
    player_list = pygame.sprite.Group()
    player_list.add(player)
    map = Map(level)
    #initialise la Clock qui va s'assurer que le jeu tourne à 60 fps constant
    clock = pygame.time.Clock()
    steps = 5
    fps = 60

    #Boucle de jeu principale
    while not player.is_arrived():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.control(-steps,0)
                if event.key == pygame.K_RIGHT:
                    player.control(steps,0)
                if event.key == pygame.K_UP: #le saut
                    player.jumping(steps)
                if event.key == pygame.K_DOWN: #dash buggué car pas le temps de faire du recasting
                    if player.vel_x > 0:
                        player.control(steps*30,0)
                        player.update(map)
                        player.control(-30*steps,0)
                    elif player.vel_x < 0:
                        player.control(-30*steps,0)
                        player.update(map)
                        player.control(30*steps,0)
            if event.type == pygame.KEYUP: #touche qui cesse d'être préssée
                if event.key == pygame.K_LEFT or event.key == ord('q'):
                    if player.is_moving_x():
                        player.control(steps,0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    if player.is_moving_x():
                        player.control(-steps,0)
        #Affichage des différents éléments à l'écran
        screen.blit(world,(0,150))
        screen.blit(cadre_haut,(0,0))
        render_map(world,map)
        player.update(map)
        player_list.draw(world)
        #affichage du timer et du niveau
        affichage_lvl = police_lvl.render(str(level) , 1 , (255,0,0))
        screen.blit(affichage_lvl, (290,55))
        timer = time.time() - time_debut
        affichage_timer = police_lvl.render(time.strftime('%M:%S',time.gmtime(timer)), 1 , (255,0,0))
        screen.blit(affichage_timer, (480,65))

        screen.blit(police_lvl.render(str(player.rect.x)+','+str(player.rect.y),1,(255,0,0)),(0,0))
        pygame.display.update()
        clock.tick(fps)#pour que les boucles se fasse sur un temps constant

def fin_level():
    '''Affichage à la fin du niveau, appuyer sur quitter pour quitter '''
    police_lvl = pygame.font.SysFont("monospace" ,40)
    screen = pygame.display.set_mode((608,950))
    clock = pygame.time.Clock()
    images = [pygame.transform.scale(pygame.image.load(os.path.join('images','licorne','frame'+str(i)+'.gif')),(608,608)) for i in range(1,20)]
    licorne = True
    frame = 0
    while licorne:
        screen.blit(images[frame%len(images)],(0,150))
        affichage_lvl = police_lvl.render('GG Tu as Gagné' , 1 , (255,0,0))
        screen.blit(affichage_lvl, (180,55))
        pygame.display.update()
        frame += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(19)


if __name__ == "__main__":
    level = 1
    while level <= 3: #boucle appelant main pour chaque niveau
        main(level)
        level += 1
    fin_level()#quand le jeu est fini
    pygame.quit()
