import pygame
from pygame.locals import *
from collections import deque

size = (800,400)
gameList = ["streetFighter","pacman","digDug","iceClimbers","donkeyKong","contra"]

class game(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.name = image
        self.image = pygame.image.load(image + ".png")
        self.size = (int(size[0] / 2), int(size[1] / 5))
        self.image = pygame.transform.scale(self.image,self.size)
        self.rect = pygame.Rect(self.image.get_rect(topleft = (0,0)))

    def setPos(self,pos):
        self.rect = pygame.Rect(self.image.get_rect(topleft = pos))

class gameDisplay(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.name = image
        self.image = pygame.image.load(image + ".png")
        self.size = (int(size[0] / 2), size[1])
        self.image = pygame.transform.scale(self.image,self.size)
        self.rect = pygame.Rect(self.image.get_rect(topleft = (int(size[0]/2),0)))
    
    def setPicture(self,image):
        self.image = pygame.image.load(image + ".png")
        self.image = pygame.transform.scale(self.image,self.size)
        self.rect = pygame.Rect(self.image.get_rect(topleft = (int(size[0]/2),0)))

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)#,pygame.FULLSCREEN)
    index = 0
    games = deque([])

    for g in gameList:
        new = game(g)
        games.append(new)
       
    display = gameDisplay(games[2].name+"T")

    while True:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > size[0] / 2: #right
                    print("selectGame")
                elif pygame.mouse.get_pos()[0] < size[0] / 2: #left
                    if pygame.mouse.get_pos()[1] < size[1] / 2: #above
                        games.rotate(-1)
                    else:
                        games.rotate(1)
        
        pos = [0,0]
        for i in range(5):
            games[i].setPos(pos)
            pos[1] += games[i].size[1]
            screen.blit(games[i].image,games[i].rect)
        
        pygame.draw.rect(screen,(0,255,0),games[2].rect,10)
        display.setPicture(games[2].name+"T")
        screen.blit(display.image,display.rect)
    
        pygame.display.flip()

if __name__ == '__main__':
    main()