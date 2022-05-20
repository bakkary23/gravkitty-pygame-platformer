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
mus = 0
stop = 0
title_music = pygame.mixer.Sound('audio/titletheme.mp3')
title_music.set_volume(0.1)
game_music = pygame.mixer.Sound('audio/gamemusic.mp3')
game_music.set_volume(0.1)


def surfaces(screen):
    """Initializes and places surfaces"""
    background_surface = pygame.image.load('graphics/background1.jpg').convert()
    floor_surface = pygame.image.load('graphics/floor.jpg').convert()
    ceiling_surface = pygame.image.load('graphics/ceiling.jpg').convert()
    screen.blit(background_surface, (0, 0))
    screen.blit(floor_surface, (0, 547))
    screen.blit(ceiling_surface, (0, 0))


def game_over(screen):
    font = pygame.font.Font('freesansbold.ttf', 100)
    game_over_message = font.render('GAME OVER', False, 'red')
    game_over_message_rect = game_over_message.get_rect(center=(500, 250))
    font2 = pygame.font.Font('freesansbold.ttf', 32)
    restart_message = font2.render('Press space to exit', False, 'red')
    restart_message_rect = restart_message.get_rect(center=(500, 400))
    title_background = pygame.image.load('graphics/stars.png').convert_alpha()
    screen.blit(title_background, (0, 0))
    screen.blit(game_over_message, game_over_message_rect)
    screen.blit(restart_message, restart_message_rect)


def win_screen(screen):
    font = pygame.font.Font('freesansbold.ttf', 100)
    win_message = font.render('YOU WIN!', False, 'green')
    win_message_rect = win_message.get_rect(center=(500, 250))
    font2 = pygame.font.Font('freesansbold.ttf', 32)
    restart_message = font2.render('Press space to exit', False, 'green')
    restart_message_rect = restart_message.get_rect(center=(500, 400))
    title_background = pygame.image.load('graphics/stars.png').convert_alpha()
    screen.blit(title_background, (0, 0))
    screen.blit(win_message, win_message_rect)
    screen.blit(restart_message, restart_message_rect)


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


def collisions():
    if pygame.sprite.spritecollide(player.sprite, obstacles, False):
        return 1
    if pygame.sprite.spritecollide(player.sprite, end, False):
        return 2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(100, 490))
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
        self.rect = self.image.get_rect(topleft=(100, 490))
        if self.direction == -1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.gravity = 0
            self.direction = 1
        if self.flip == 0:
            self.flip = 1
            self.image = pygame.transform.flip(self.image, True, False)

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
            self.rect = self.image.get_rect(topleft=(700, 53))
            self.image = pygame.transform.flip(self.image, False, True)
        if types == 'blackhole':
            self.image = pygame.image.load('graphics/blackhole.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=(450, 250))


class End(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/end.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(850, 458))


player = pygame.sprite.GroupSingle()
player.add(Player())
end = pygame.sprite.GroupSingle()
end.add(End())
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
        if mus == 1:
            title_music.stop()
            game_music.play()
            mus = 0
        surfaces(display)
        player.draw(display)
        obstacles.draw(display)
        end.draw(display)
        if stop != 1:
            player.update(game_active)
        if collisions() == 1:
            game_music.stop()
            game_over(display)
            if stop == 0:
                pygame.mixer.Sound('audio/win.mp3').play()
            stop = 1
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                stop = 0
                game_active = False
        if collisions() == 2:
            game_music.stop()
            win_screen(display)
            if stop == 0:
                pygame.mixer.Sound('audio/lose.mp3').play()
            stop = 1
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                stop = 0
                game_active = False
    else:
        if mus == 0:
            game_music.stop()
            title_music.play()
            mus = 1
        intro_screen(display)
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            player.update(game_active)
            game_active = True

    pygame.display.update()
    clock.tick(60)
