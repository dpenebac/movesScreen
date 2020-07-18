import pygame
from pygame.locals import *
from collections import deque

size = (1300,1000)
gameList = ["streetFighter.png","pacman.png","digDug.png","iceClimbers.png","donkeyKong.png","contra.png"]

class game(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.name = image
        self.image = pygame.image.load(image)
        self.size = (650,200) ##(size[0] / 2, size[1] / 5)
        self.image = pygame.transform.scale(self.image,self.size)
        self.rect = pygame.Rect(self.image.get_rect(topleft = (0,0)))

    def setPos(self,pos):
        self.rect = pygame.Rect(self.image.get_rect(topleft = pos))

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    index = 0
    games = deque([])

    for g in gameList:
        new = game(g)
        games.append(new)

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
    
        pygame.display.flip()

if __name__ == '__main__':
    main()