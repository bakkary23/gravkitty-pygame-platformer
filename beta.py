import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Gravkitty')
clock = pygame.time.Clock()

"""Player sprite position on coordinate system"""
player_sprite_x = 98
player_sprite_y = 470

"""Background surface, title text + rectangle initialization"""
background_surface = pygame.image.load('graphics/background1.jpg').convert()
floor_surface = pygame.image.load('graphics/floor.jpg').convert()
ceiling_surface = pygame.image.load('graphics/ceiling.jpg').convert()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(player_sprite_x, player_sprite_y))


cat = pygame.sprite.GroupSingle()
cat.add(Player())


def place_surfaces():
    """Places background, player, and title surfaces in game loop"""
    screen.blit(background_surface, (0, 0))
    screen.blit(floor_surface, (0, 547))
    screen.blit(ceiling_surface, (0, 0))
    screen.blit(player_sprite, player_rect)


"""Temporary player sprite and rectangle initialization"""
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
                    player_rect.left += 5
        if player_rect.left > 0:
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                player_sprite = pygame.image.load('graphics/player1.png')
                if pygame.key.get_pressed()[pygame.K_v]:
                    player_rect.left -= 8
                else:
                    player_rect.left -= 5

    place_surfaces()
    pygame.display.update()
    clock.tick(60)
