import pygame
from random import randrange

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
pygame.display.set_caption('Game')
fon = pygame.image.load('data/fon.png')
fon = pygame.transform.scale(fon, (WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60


class Menu:
    def __init__(self):
        self.start_btn = pygame.Surface((300, 200))
        self.exit_btn = pygame.Surface((200, 100))
        self.fon = pygame.image.load('data/menu_fon.png')
        self.fon = pygame.transform.scale(self.fon, (WIDTH, HEIGHT))
        self.start = pygame.image.load('data/start.png')
        self.exit = pygame.image.load('data/exit.png')
        self.start_btn.set_colorkey((0, 0, 0))
        self.exit_btn.set_colorkey((0, 0, 0))
        self.exit_btn_d = False
        self.start_btn_d = False
        self.k_n_s = False
        self.k_n_e = False

    def start_btn_check(self, x, y):
        return x in [i for i in range(100, 400)] and \
               y in [i for i in range(350, 550)]

    def exit_btn_check(self, x, y):
        return x in [i for i in range(500, 700)] and \
               y in [i for i in range(650, 750)]

    def draw(self):
        run = True
        while run and not any([self.exit_btn_d, self.start_btn_d]):
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.exit_btn_check(x, y):
                        self.exit_btn_d = True
                    elif self.start_btn_check(x, y):
                        self.start_btn_d = True
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    if self.exit_btn_check(x, y):
                        self.k_n_e = True
                    elif self.start_btn_check(x, y):
                        self.k_n_s = True
                    else:
                        self.k_n_s = False
                        self.k_n_e = False
            if self.k_n_s:
                self.start = pygame.image.load('data/start1.png')
            elif self.k_n_e:
                self.exit = pygame.image.load('data/exit1.png')
            else:
                self.start = pygame.image.load('data/start.png')
                self.exit = pygame.image.load('data/exit.png')
            screen.blit(self.fon, (0, 0))
            win.blit(screen, (0, 0))
            screen.blit(self.start, (100, 350))
            screen.blit(self.exit, (500, 650))
            pygame.display.update()


class PauseMenu:
    def __init__(self):
        self.continue_btn = pygame.Surface((300, 200))
        self.mainmenu_btn = pygame.Surface((200, 100))
        self.fon = pygame.image.load('data/pause_fon.png')
        self.fon = pygame.transform.scale(self.fon, (WIDTH, HEIGHT))
        self.continuebtn = pygame.image.load('data/continue.png')
        self.mainmenu = pygame.image.load('data/main_menu.png')
        self.continue_btn.set_colorkey((0, 0, 0))
        self.mainmenu_btn.set_colorkey((0, 0, 0))

    def mainmenu_btn_check(self, x, y):
        return x in [i for i in range(100, 400)] and \
               y in [i for i in range(350, 550)]

    def continue_btn_check(self, x, y):
        return x in [i for i in range(500, 700)] and \
               y in [i for i in range(650, 750)]

    def draw(self, x, y):
        if self.mainmenu_btn_check(x, y):
            self.mainmenu = pygame.image.load('data/main_menu1.png')
        elif self.continue_btn_check(x, y):
            self.continuebtn = pygame.image.load('data/continue1.png')
        else:
            self.continuebtn = pygame.image.load('data/continue.png')
            self.mainmenu = pygame.image.load('data/main_menu.png')
        screen.blit(self.fon, (0, 0))
        win.blit(screen, (0, 0))
        screen.blit(self.mainmenu, (100, 350))
        screen.blit(self.continuebtn, (500, 650))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 50)

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.right = 0

    def move(self, i):
        if i[pygame.K_LEFT]:
            self.rect.x -= 5
        elif i[pygame.K_RIGHT]:
            self.rect.x += 5
        elif i[pygame.K_UP]:
            self.rect.y -= 5
        elif i[pygame.K_DOWN]:
            self.rect.y += 5


class Enemy(pygame.sprite.Sprite):
    pass


class Let(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self, group)
        w = randrange(50, 300)
        h = randrange(50, 300)
        self.image = pygame.image.load('data/let.png')
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = randrange(10, WIDTH)
        self.rect.y = randrange(-HEIGHT * 5, 0)

    def update(self):
        self.rect = self.rect.move(0, 10)


class Bonus(pygame.sprite.Sprite):
    pass


menu = Menu()
pause_menu = PauseMenu()
running = True
while running:
    menu.draw()
    if menu.start_btn_d:
        player_sprites = pygame.sprite.Group()
        enemy_sprites = pygame.sprite.Group()
        let_sprites = pygame.sprite.Group()
        bonus_sprites = pygame.sprite.Group()
        pause = False
        run = True
        player = Player()
        player_sprites.add(player)
        fon_y = 0
        fon_y1 = -HEIGHT
        lets_c = 10
        for i in range(lets_c):
            Let(let_sprites)
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pause = not pause
                if pause:
                    x, y = 0, 0
                    if event.type == pygame.MOUSEMOTION:
                        x, y = event.pos
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if pause_menu.mainmenu_btn_check(x, y):
                            run = False
                            menu.start_btn_d = False
                            break
                        elif pause_menu.continue_btn_check(x, y):
                            pause = False
                    pause_menu.draw(x, y)
            if not pause:
                keys = pygame.key.get_pressed()
                player.move(keys)
                player_sprites.update()
                screen.blit(fon, (0, fon_y))
                screen.blit(fon, (0, fon_y1))
                fon_y += 10
                fon_y1 += 10
                if fon_y > HEIGHT:
                    fon_y = -HEIGHT
                elif fon_y1 > HEIGHT:
                    fon_y1 = -HEIGHT
                let_sprites.draw(screen)
                let_sprites.update()
                player_sprites.draw(screen)
            pygame.display.flip()
    else:
        running = False
pygame.quit()
