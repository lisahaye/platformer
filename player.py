import os
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,ani):
        pygame.sprite.Sprite.__init__(self)#héritage de pygame.Sprite
        self.images = []
        for i in range(1,ani+1):
            img = pygame.image.load(os.path.join('images','player','player'+str(i)+'.png')).convert_alpha()
            img = pygame.transform.scale(img, (30,30))
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 576
        self.rect.y = 768
        self.vel_x = 0
        self.vel_y = 0
        self.frame = 0
        self.ani = ani
        self.jump = 0

    def control(self,x,y):
        self.vel_x += x
        self.vel_y += y

    def update(self,map):
        self.rect.x = self.rect.x + self.vel_x
        self._collisions_x(map)
        self.rect.y = self.rect.y + self.vel_y
        self._collisions_y(map)
        if self.vel_x < 0:
            self.frame += 1
            if self.frame > 3*self.ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // self.ani], True, False)
        if self.vel_x > 0:
            self.frame += 1
            if self.frame > 3*self.ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // self.ani], False,False)

    def _collisions_y(self,map):
            for rect in map.rects():
                if pygame.Rect.colliderect(rect,self.rect):
                    if self.vel_y > 0:
                        self.rect.bottom = rect.top
                        self.jump = 0
                        self.vel_y = 0
                    elif self.vel_y < 0:
                        self.rect.top = rect.bottom
                        self.vel_y = 0
            if self.rect.y < 0 :
                self.rect.y = 0
            if self.vel_y <= 9:
                self.vel_y += 0.5
                if self.jump == 0:
                    self.jump = 1

    def _collisions_x(self,map):
        for rect in map.rects():
            if pygame.Rect.colliderect(rect,self.rect):
                if self.vel_x < 0:
                    self.rect.left = rect.right
                elif self.vel_x > 0:
                    self.rect.right = rect.left
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > 568:
                self.rect.x = 568

    def jumping(self,steps):
        if self.jump <= 2:
            self.jump += 1
            self.control(0,-1.3*steps)

    def is_moving_x(self):
        return self.vel_x != 0

    def is_arrived(self):
        if 0 <= self.rect.x <= 64 and 0 <= self.rect.y <= 128:
            return True
        return False
