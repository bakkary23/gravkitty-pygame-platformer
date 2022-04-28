import pygame
from sys import exit

"""This section sets up the needed variables, modules, etc
that will be called in the functional part of the program"""
pygame.init()
display = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Gravkitty')
clock = pygame.time.Clock()


def surfaces(screen):
    """Initializes and places surfaces"""
    background_surface = pygame.image.load('graphics/background1.jpg').convert()
    floor_surface = pygame.image.load('graphics/floor.jpg').convert()
    ceiling_surface = pygame.image.load('graphics/ceiling.jpg').convert()
    screen.blit(background_surface, (0, 0))
    screen.blit(floor_surface, (0, 547))
    screen.blit(ceiling_surface, (0, 0))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(100, 470))
        self.gravity = 0
        self.direction = 1
        self.flip = 1

    def player_input(self):
        """Function for manipulating player sprite with player inputs"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < 1000:
            if self.flip != 1:
                self.image = pygame.transform.flip(self.image, True, False)
            self.flip = 1
            self.rect.left += 6
            if keys[pygame.K_v]:
                self.rect.left += 4
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            if self.flip != 0:
                self.image = pygame.transform.flip(self.image, True, False)
            self.flip = 0
            self.rect.left -= 6
            if keys[pygame.K_v]:
                self.rect.left -= 4
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.rect.bottom >= 547 and self.direction == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.gravity = -10
                self.direction = -1
            if event.key == pygame.K_SPACE and self.rect.top <= 53 and self.direction == -1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.gravity = 10
                self.direction = 1

    def set_gravity(self):
        """Function that sets gravity for player sprite"""
        self.gravity += self.direction
        self.rect.y += self.gravity
        if self.rect.bottom >= 547:
            self.rect.bottom = 547
        if self.rect.top <= 53:
            self.rect.top = 53

    def update(self):
        """Function for adding player input to game loop"""
        self.player_input()
        self.set_gravity()


player = pygame.sprite.GroupSingle()
player.add(Player())

while True:

    for event in pygame.event.get():
        pygame.key.set_repeat(10, 10)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    surfaces(display)

    """Methods for adding and manipulating player"""
    player.draw(display)
    player.update()

    pygame.display.update()
    clock.tick(60)
