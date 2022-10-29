from itertools import count
import pygame
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png').convert()

ground_surface = pygame.image.load('graphics/ground.png').convert()


test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surf = test_font.render("Bongwater",False,'Black')
text_rect = text_surf.get_rect(center = (400,100))

snail_surf = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom =(700,300))

player_surf = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (100,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surf,text_rect)
    

    if snail_rect.right <=0: snail_rect.left = 800
    snail_rect.x -= 4
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)


    pygame.display.update()
    clock.tick(60)