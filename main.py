import pygame
from sys import exit

"""This section sets up the needed variables, modules, etc
that will be called in the functional part of the program"""
pygame.init()
display = pygame.display.set_mode((1000, 600))
pygame.display.set_icon(pygame.image.load('graphics/player.png').convert_alpha())
pygame.display.set_caption('Gravkitty')
clock = pygame.time.Clock()
game_active = False
game_music = pygame.mixer.Sound('audio/gamemusic.mp3')
game_music.set_volume(0.2)
game_music.play(loops=-1)


def surfaces(screen):
    """Initializes and places surfaces"""
    background_surface = pygame.image.load('graphics/background1.jpg').convert()
    floor_surface = pygame.image.load('graphics/floor.jpg').convert()
    ceiling_surface = pygame.image.load('graphics/ceiling.jpg').convert()
    screen.blit(background_surface, (0, 0))
    screen.blit(floor_surface, (0, 547))
    screen.blit(ceiling_surface, (0, 0))


# def music(state):
#     title_music = pygame.mixer.Sound('audio/titletheme.mp3')
#     game_music = pygame.mixer.Sound('audio/gamemusic.mp3')
#     if state is False:
#         title_music.play()
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_RETURN]:
#         game_music.play(loops=-1)


def intro_screen(screen):
    font = pygame.font.Font('freesansbold.ttf', 70)
    font2 = pygame.font.Font('freesansbold.ttf', 32)
    game_title = font.render('Gravkitty', False, 'gold')
    game_title_rect = game_title.get_rect(center=(475, 100))
    title_message = font2.render('Press enter to start game', False, 'gold')
    title_message_rect = title_message.get_rect(center=(475, 450))
    title_background = pygame.image.load('graphics/stars.png').convert_alpha()
    title_image = pygame.image.load('graphics/titlescreen.png').convert()
    title_image = pygame.transform.smoothscale(title_image.convert_alpha(), (260, 346))
    title_image_rect = title_image.get_rect(center=(485, 280))
    screen.blit(title_background, (0, 0))
    screen.blit(title_image, title_image_rect)
    screen.blit(title_message, title_message_rect)
    screen.blit(game_title, game_title_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(100, 470))
        self.switchsound = pygame.mixer.Sound('audio/gravityswitch.mp3')
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
                self.switchsound.play()
                self.gravity = -10
                self.direction = -1
            if event.key == pygame.K_SPACE and self.rect.top <= 53 and self.direction == -1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.switchsound.play()
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

    def restart(self):
        self.rect = self.image.get_rect(topleft=(100, 470))

    def update(self, state):
        """Function for adding player input to game loop"""
        if state is True:
            self.player_input()
            self.set_gravity()
        else:
            self.restart()


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, types):
        super().__init__()
        if types == 'spikes1':
            self.image = pygame.image.load('graphics/spikes.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=(310, 517))
        if types == 'spikes2':
            self.image = pygame.image.load('graphics/spikes.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=(750, 53))
            self.image = pygame.transform.flip(self.image, False, True)
        if types == 'blackhole':
            self.image = pygame.image.load('graphics/blackhole.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=(450, 250))


def collisions():
    if pygame.sprite.spritecollide(player.sprite, obstacles, False):
        return False
    else:
        return True


player = pygame.sprite.GroupSingle()
player.add(Player())
obstacles = pygame.sprite.Group()
obstacles.add(Obstacle('spikes1'))
obstacles.add(Obstacle('spikes2'))
obstacles.add(Obstacle('blackhole'))


while True:

    for event in pygame.event.get():
        pygame.key.set_repeat(10, 10)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        surfaces(display)
        player.draw(display)
        obstacles.draw(display)
        player.update(game_active)
        game_active = collisions()
    else:
        intro_screen(display)
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            player.update(game_active)
            game_active = True

    pygame.display.update()
    clock.tick(60)
