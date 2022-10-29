import pygame
from sys import exit 

pygame.init()
#creates a Screen
screen = pygame.display.set_mode((800,400))

while True:
    #this for loop allows you to close the window without task manager
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #this line is the oppisite of pygame.init()
            pygame.quit()
            #this line cleanly closes pygame
            exit()
    #updates the screen
    pygame.display.update()