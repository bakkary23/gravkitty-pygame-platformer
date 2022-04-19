import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Gravkitty')
clock = pygame.time.Clock()
test_font = pygame.font.SysFont('font/Pixeltype.ttf', 70)

"""Player sprite position on coordinate system"""
player_sprite_x = 98
player_sprite_y = 470
"""Title sprite position on coordinate system"""
title_x = 500
title_y = 30
# direction = 0


"""Background surface, title text + rectangle initialization"""
background_surface = pygame.image.load('graphics/background1.jpg').convert()
floor_surface = pygame.image.load('graphics/floor.jpg').convert()
ceiling_surface = pygame.image.load('graphics/cieling.jpg').convert()


# title_text = test_font.render('Gravkitty', False, 'Black').convert()
# title_rect = title_text.get_rect(midtop=(title_x, title_y))

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = sprite = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = rect = sprite.get_rect(topleft=(player_sprite_x, player_sprite_y))


cat = pygame.sprite.GroupSingle()
cat.add(Player())

"""Player sprite and rectangle initialization"""
player_sprite = pygame.image.load('graphics/player.png').convert_alpha()
player_rect = player_sprite.get_rect(topleft=(player_sprite_x, player_sprite_y))

while True:

    pygame.key.set_repeat(10, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if player_rect.right < 1000:
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                player_sprite = pygame.image.load('graphics/player.png')
                if pygame.key.get_pressed()[pygame.K_v]:
                    player_rect.left += 8
                else:
                    player_rect.left += 4
        if player_rect.left > 0:
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                player_sprite = pygame.image.load('graphics/player1.png')
                if pygame.key.get_pressed()[pygame.K_v]:
                    player_rect.left -= 8
                else:
                    player_rect.left -= 4

    """Places background, player, and title surfaces in game loop"""
    screen.blit(background_surface, (0, 0))
    screen.blit(floor_surface, (0, 547))
    screen.blit(ceiling_surface, (0, 0))
    # screen.blit(title_text, title_rect)
    screen.blit(player_sprite, player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_RIGHT]:
    #     print("right")

    # if player_rect.left <= 819 and direction == 0:
    #     player_rect.left += 7
    #     if player_rect.left == 819:
    #         direction = 1
    #         player_sprite = pygame.image.load('graphics/player1.png')
    # if player_rect.left >= 98 and direction == 1:
    #     player_rect.left -= 7
    #     if player_rect.left == 98:
    #         direction = 0
    #         player_sprite = pygame.image.load('graphics/player.png')

    pygame.display.update()
    clock.tick(60)
