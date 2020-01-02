import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


class Player(pygame.sprite.Sprite):
    pass


class Enemy(pygame.sprite.Sprite):
    pass


class Let(pygame.sprite.Sprite):
    pass


class Bonus(pygame.sprite.Sprite):
    pass


player_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
let_sprites = pygame.sprite.Group()
bonus_sprites = pygame.sprite.Group()
run = True
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()
