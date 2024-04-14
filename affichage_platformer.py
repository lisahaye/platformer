import pygame
pygame.init()
screen = pygame.display.set_mode((600,800))
LIGHT_BLUE = pygame.Color(110,193,248)
BLACK = pygame.Color(0,0,0)
BLUE = pygame.Color(0,0,255)
#coords = [(14.5,33),(14.5,32),(14.5,31)]
world = pygame.Surface((600,800))
world = pygame.image.load("Background_coblestone.png")
cadre_haut = pygame.Surface((600,125))
cadre_haut.fill(BLACK)
cadre_lvl = pygame.Surface((100,75))
cadre_lvl.fill(BLUE)

#for x,y in coords:
#    pygame.draw.rect(world,LIGHT_BLUE,(x*20,y*20,20,20))

licorne = True
while licorne:
    screen.blit(world,(0,125))
    screen.blit(cadre_haut,(0,0))
    screen.blit(cadre_lvl,(250,25))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit
                licorne = False
