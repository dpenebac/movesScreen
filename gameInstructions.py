import pygame
from pygame.locals import *
import time
import os

charList = ["sfcontrols","ryu","chunLi","dhalsim"]
size = (800,400)

class move(pygame.sprite.Sprite):
    def __init__(self,image,screen):
        pygame.sprite.Sprite.__init__(self)
        self.changeImage(image,screen)

    def changeImage(self,image,screen):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,size)
        self.rect = pygame.Rect(self.image.get_rect(center = (size[0] / 2, size[1] / 2)))

def send(cmd,*args):
    pid, fd = os.forkpty()
    if pid==0: # child
        os.execlp(cmd,*args)
    while True:
        data = os.read(fd,1024)
        if "password:" in data:    # ssh prompt
            os.write(fd,"UHfamily21\n")
        elif data.endswith("$ "):  # bash prompt for input
            os.write(fd,"/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ snes '/home/pi/RetroPie/roms/snes/The Legend of Zelda - A Link to the Past (U) [!].smc'\n")
            os.write(fd,"exit\n")
    #/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ snes '/home/pi/RetroPie/roms/snes/The Legend of Zelda - A Link to the Past (U) [!].smc'
    #send("ssh", "ssh", "user@remote")

def sf2CE():
    pygame.init()
    screen = pygame.display.set_mode(size)
    background = move("sf2CEmoveList/" + charList[0] + ".png",screen)
    index = 0
    background.changeImage("sf2CEmoveList/" + charList[0] + ".png",screen)

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
                background.changeImage("sf2CEmoveList/" + charList[index] + ".png",screen)

        screen.blit(background.image,background.rect)
        pygame.display.flip()

def Games(game):
    pygame.init()
    pass
