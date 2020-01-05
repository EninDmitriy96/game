import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
FPS = 30


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.right = 0

    def move(self, i):
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                self.rect.x -= 5
            elif i.key == pygame.K_RIGHT:
                self.rect.x += 5
            elif i.key == pygame.K_UP:
                self.rect.y -= 5
            elif i.key == pygame.K_DOWN:
                self.rect.y += 5


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
player = Player()
player_sprites.add(player)
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        player.move(event)
    player_sprites.update()
    screen.fill((0, 0, 0))
    player_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
