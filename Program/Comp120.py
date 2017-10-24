"""
========================================================================================================================
    Program: Comp 120 - Contract #3 Unit Generation
    Purpose: To create many different types of enemies using various components.
    Author(s): Connor Sean Rodgers
    Organisation: Falmouth University - Games Academy - BSc Computing for Games
========================================================================================================================

"""

#imports
import pygame
import math
import random
from random import randint
#initiate pygame
pygame.init()
#screen setup
screen = pygame.display.set_mode((100,300))
screen.fill((255,255,255))
screen.blit(screen, (0,0))
def funRandomUnit():
    """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    This function of code will generate 3 random numbers one for each component of the sprite. The random numbers are
    generated from an inclusive range of 1 to 4 as this is the number I am testing with I have hard coded this into the
    system. It will then produce an image of these 3 components and export it as a raster image file as a portable
    network graphic (.PNG)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    intTopSection = randint(1,4)
    intCenterSection = randint(1,4)
    intBottomSelection = randint (1,4)

    if (intTopSection == 1):
        imgTop = pygame.image.load(("T1.png"))
    elif (intTopSection == 2):
        imgTop = pygame.image.load(("T2.png"))
    elif (intTopSection == 3):
        imgTop = pygame.image.load(("T3.png"))
    elif (intTopSection == 4):
        imgTop = pygame.image.load(("T4.png"))
    else:
        imgTop = pygame.image.load(("T1.png"))

    if (intCenterSection == 1):
        imgCenter = pygame.image.load(("M1.png"))
    elif (intCenterSection == 2):
        imgCenter = pygame.image.load(("M2.png"))
    elif (intCenterSection == 3):
        imgCenter = pygame.image.load(("M3.png"))
    elif (intCenterSection == 4):
        imgCenter = pygame.image.load(("M4.png"))
    else:
        imgCenter = pygame.image.load(("M1.png"))

    if (intBottomSelection == 1):
        imgBottom= pygame.image.load(("B1.png"))
    elif (intBottomSelection == 2):
        imgBottom = pygame.image.load(("B2.png"))
    elif (intBottomSelection == 3):
        imgBottom = pygame.image.load(("B3.png"))
    elif (intBottomSelection == 4):
        imgBottom = pygame.image.load(("B4.png"))
    else:
        imgBottom = pygame.image.load(("B1.png"))
    screen.blit(imgTop,(0,0))
    screen.blit(imgCenter,(0,100))
    screen.blit(imgBottom,(0,200))
    pygame.display.flip()
    pygame.image.save(screen, "random.png")
    return
done = False

##Keep window open until closed by user
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            funRandomUnit()
    pygame.display.flip()


