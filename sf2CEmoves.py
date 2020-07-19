import pygame
from pygame.locals import *

charList = ["ryu","ken","chunLi"]
size = (1300,1000)

class move(pygame.sprite.Sprite):
    def __init__(self,image,screen):
        pygame.sprite.Sprite.__init__(self)
        self.changeImage(image,screen)

    def changeImage(self,image,screen):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,size)
        self.rect = pygame.Rect(self.image.get_rect(center = (size[0] / 2, size[1] / 2)))

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
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
