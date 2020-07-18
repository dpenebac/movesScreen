import pygame
from pygame.locals import *

class scrollWheel(pygame.sprite.Sprite):
    def __init__(self,gameList,screen):
        pygame.sprite.Sprite.__init__(self)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,480))
    background = move(charList[0] + ".png",screen)
    index = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > size[0] / 2:
                    index += 1
                elif pygame.mouse.get_pos()[0] < size[0] / 2:
                    index -= 1

                if index > len(charList) - 1:
                    index = 0
                elif index < 0:
                    index = len(charList) - 1
                background.changeImage(charList[index] + ".png",screen)

        screen.blit(background.image,background.rect)
        pygame.display.flip()

if __name__ == '__main__':
    main()