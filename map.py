import os
import pygame


class Map:
    def __init__(self,level):
        self.images = []
        for i in range(1,10):
                img = pygame.image.load(os.path.join(os.getcwd(),'images','lvl '+str(level),'bloc'+str(i)+'.png'))
                img = pygame.transform.scale(img, (32,32))
                self.images.append(img)

        self.dico={}
        for i in range(0,9):
            self.dico[i+1] = self.images[i]

        f = open(f'images//lvl {level}//lvl{level}.txt','r')
        map_txt = f.read()
        f.close()
        self.map = list()
        for ligne in map_txt.split(";\n"):
            self.map.append([char for char in ligne])

    def render_map(self):
        coords = []

        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                coords.append((x*32,y*32,self.dico[int(self.map[y][x])]))
        return coords

    def rects(self):
        coords = []
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == '5' or self.map[y][x] == '6':
                    coords.append(pygame.Rect(x*32,y*32,32,32))
        return coords

if __name__ == '__main__':
    map = Map(1)
    print(map.render_map())
