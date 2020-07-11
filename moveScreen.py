import pygame
from pygame.locals import *

charList = ["ryu","ken","chunLi"]

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,480))
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
    
        pygame.display.flip()

if __name__ == '__main__':
    main()