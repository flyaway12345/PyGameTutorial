import pygame
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png').convert()

ground_surface = pygame.image.load('graphics/ground.png').convert()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = test_font.render('Bongwater',False,'Black')

snail_surface = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(0,0))
    
    if(snail_x_pos <= -100):
        snail_x_pos = 900
    else:
        snail_x_pos -= 4

    screen.blit(snail_surface,(snail_x_pos,280))
    pygame.display.update()
    clock.tick(60)