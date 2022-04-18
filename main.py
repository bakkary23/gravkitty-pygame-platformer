import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Gravkitty')
clock = pygame.time.Clock()
test_font = pygame.font.SysFont('font/Pixeltype.ttf', 70)

player_sprite_x = 98
player_sprite_y = 479
title_x = 500
title_y = 30
direction = 0
background_surface = pygame.image.load('graphics/lab.jpg').convert()
title_text = test_font.render('Gravkitty', False, 'Black').convert()
title_rect = title_text.get_rect(midtop=(title_x, title_y))

player_sprite = pygame.image.load('graphics/player.png').convert_alpha()
player_rect = player_sprite.get_rect(topleft=(player_sprite_x, player_sprite_y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0, 0))
    screen.blit(title_text, title_rect)
    screen.blit(player_sprite, player_rect)
    if player_rect.left <= 819 and direction == 0:
        player_rect.left += 7
        if player_rect.left == 819:
            direction = 1
            player_sprite = pygame.image.load('graphics/player1.png')
    if player_rect.left >= 98 and direction == 1:
        player_rect.left -= 7
        if player_rect.left == 98:
            direction = 0
            player_sprite = pygame.image.load('graphics/player.png')

    pygame.display.update()
    clock.tick(60)
