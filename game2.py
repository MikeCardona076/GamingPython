import pygame, sys
from pygame.locals import *
pygame.init()
#Background
green = (  0, 255,   0)
light_Blue = (  20, 20,   175)
yellow = ( 155, 155, 0)
# SCREEN SETTINGS
size = 1000,700
width,height = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mikes's game")
mr_spy = pygame.image.load('MrSpy.png')
my_spy = mr_spy.get_rect()
speed = [2,2]

while True:# main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    my_spy = my_spy.move(speed) #Movimiento del objeto
    if my_spy.left <0 or my_spy.right > width:
        screen.fill(light_Blue)
        speed[0] = -speed[0]
    if my_spy.top <0 or my_spy.bottom > height:
        screen.fill(yellow)
        speed[1] = -speed[1]
        

    screen.fill(green)
    screen.blit(mr_spy,my_spy)
    pygame.display.update()