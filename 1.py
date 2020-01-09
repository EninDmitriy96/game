import pygame
from random import randrange

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
pygame.display.set_caption('Game')
fon = pygame.image.load('data/fon.png')
fon = pygame.transform.scale(fon, (WIDTH, HEIGHT))
bullets_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
FPS = 60


class Menu:
    def __init__(self):
        self.start_btn = pygame.Surface((300, 200))
        self.exit_btn = pygame.Surface((200, 100))
        self.records_btn = pygame.Surface((299, 100))
        self.fon = pygame.image.load('data/menu_fon.png')
        self.fon = pygame.transform.scale(self.fon, (WIDTH, HEIGHT))
        self.start = pygame.image.load('data/start.png')
        self.exit = pygame.image.load('data/exit.png')
        self.records = pygame.image.load('data/records.png')
        self.start_btn.set_colorkey((0, 0, 0))
        self.exit_btn.set_colorkey((0, 0, 0))
        self.records_btn.set_colorkey((0, 0, 0))
        self.exit_btn_d = False
        self.start_btn_d = False
        self.records_btn_d = False
        self.k_n_s = False
        self.k_n_e = False
        self.k_n_r = False

    def start_btn_check(self, x, y):
        return x in [i for i in range(100, 400)] and \
               y in [i for i in range(350, 550)]

    def exit_btn_check(self, x, y):
        return x in [i for i in range(500, 700)] and \
               y in [i for i in range(650, 750)]

    def records_btn_check(self, x, y):
        return x in [i for i in range(100, 399)] and \
               y in [i for i in range(620, 720)]

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
                    elif self.records_btn_check(x, y):
                        self.k_n_r = True
                    else:
                        self.k_n_s = False
                        self.k_n_e = False
                        self.k_n_r = False
            if self.k_n_s:
                self.start = pygame.image.load('data/start1.png')
            elif self.k_n_e:
                self.exit = pygame.image.load('data/exit1.png')
            elif self.k_n_r:
                self.records = pygame.image.load('data/records1.png')
            else:
                self.start = pygame.image.load('data/start.png')
                self.exit = pygame.image.load('data/exit.png')
                self.records = pygame.image.load('data/records.png')
            screen.blit(self.fon, (0, 0))
            win.blit(screen, (0, 0))
            screen.blit(self.start, (100, 350))
            screen.blit(self.exit, (500, 650))
            screen.blit(self.records, (100, 620))
            pygame.display.update()


class PauseMenu:
    def __init__(self):
        self.continue_btn = pygame.Surface((300, 200))
        self.mainmenu_btn = pygame.Surface((200, 100))
        self.newgame_btn = pygame.Surface((200, 100))
        self.fon = pygame.image.load('data/pause_fon.png')
        self.fon = pygame.transform.scale(self.fon, (WIDTH, HEIGHT))
        self.continuebtn = pygame.image.load('data/continue.png')
        self.mainmenu = pygame.image.load('data/main_menu.png')
        self.newgame = pygame.image.load('data/newgame.png')
        self.continue_btn.set_colorkey((0, 0, 0))
        self.mainmenu_btn.set_colorkey((0, 0, 0))
        self.newgame_btn.set_colorkey((0, 0, 0))

    def mainmenu_btn_check(self, x, y):
        return x in [i for i in range(100, 400)] and \
               y in [i for i in range(350, 550)]

    def continue_btn_check(self, x, y):
        return x in [i for i in range(500, 700)] and \
               y in [i for i in range(650, 750)]

    def newgame_btn_check(self, x, y):
        return x in [i for i in range(100, 399)] and \
               y in [i for i in range(620, 720)]

    def draw(self, x, y):
        if self.mainmenu_btn_check(x, y):
            self.mainmenu = pygame.image.load('data/main_menu1.png')
        elif self.continue_btn_check(x, y):
            self.continuebtn = pygame.image.load('data/continue1.png')
        elif self.newgame_btn_check(x, y):
            self.newgame = pygame.image.load('data/newgame1.png')
        else:
            self.continuebtn = pygame.image.load('data/continue.png')
            self.mainmenu = pygame.image.load('data/main_menu.png')
            self.newgame = pygame.image.load('data/newgame.png')
        screen.blit(self.fon, (0, 0))
        win.blit(screen, (0, 0))
        screen.blit(self.mainmenu, (100, 350))
        screen.blit(self.continuebtn, (500, 650))
        screen.blit(self.newgame, (100, 620))

class GameOverMenu:
    def __init__(self):
        self.mainmenu_btn = pygame.Surface((200, 100))
        self.newgame_btn = pygame.Surface((200, 100))
        self.fon = pygame.image.load('data/pause_fon.png')
        self.fon = pygame.transform.scale(self.fon, (WIDTH, HEIGHT))
        self.mainmenu = pygame.image.load('data/main_menu.png')
        self.newgame = pygame.image.load('data/newgame.png')
        self.mainmenu_btn.set_colorkey((0, 0, 0))
        self.newgame_btn.set_colorkey((0, 0, 0))

    def mainmenu_btn_check(self, x, y):
        return x in [i for i in range(100, 400)] and \
               y in [i for i in range(350, 550)]

    def newgame_btn_check(self, x, y):
        return x in [i for i in range(100, 399)] and \
               y in [i for i in range(620, 720)]

    def draw(self, x, y):
        if self.mainmenu_btn_check(x, y):
            self.mainmenu = pygame.image.load('data/main_menu1.png')
        elif self.newgame_btn_check(x, y):
            self.newgame = pygame.image.load('data/newgame1.png')
        else:
            self.mainmenu = pygame.image.load('data/main_menu.png')
            self.newgame = pygame.image.load('data/newgame.png')
        screen.blit(self.fon, (0, 0))
        win.blit(screen, (0, 0))
        screen.blit(self.mainmenu, (100, 350))
        screen.blit(self.newgame, (100, 620))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/player_s.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 70)
        self.lives = 3

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - 70:
            self.rect.x = WIDTH - 70
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > HEIGHT - 70:
            self.rect.y = HEIGHT - 70
        if pygame.sprite.spritecollide(self, let_sprites, True):
            self.lives -= 1
            self.rect.center = (WIDTH / 2, HEIGHT - 70)

    def move(self, i):
        g = True
        if i[pygame.K_UP] and i[pygame.K_RIGHT]:
            self.rect.y -= 20
            self.rect.x += 20
        elif i[pygame.K_UP] and i[pygame.K_LEFT]:
            self.rect.y -= 20
            self.rect.x -= 20
        elif i[pygame.K_DOWN] and i[pygame.K_RIGHT]:
            self.rect.y += 20
            self.rect.x += 20
        elif i[pygame.K_DOWN] and i[pygame.K_LEFT]:
            self.rect.y += 20
            self.rect.x -= 20
        elif i[pygame.K_LEFT]:
            self.rect.x -= 20
        elif i[pygame.K_RIGHT]:
            self.rect.x += 20
        elif i[pygame.K_UP]:
            self.rect.y -= 20
        elif i[pygame.K_DOWN]:
            self.rect.y += 20
        else:
            g = False
            self.image = pygame.image.load('data/player_s.png')
        if g:
            self.image = pygame.image.load('data/player_g.png')

    def shot(self, event):
        if event[pygame.K_SPACE]:
            shot = Bullet(self.rect.x, self.rect.y)
            bullets_sprites.add(shot)


class Enemy(pygame.sprite.Sprite):
    pass


class Let(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self, group)
        w = randrange(50, 300)
        h = randrange(50, w + 10)
        self.image = pygame.image.load('data/let.png')
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = randrange(10, WIDTH - w)
        self.rect.y = randrange(-HEIGHT * 5, 0)

    def update(self):
        self.rect = self.rect.move(0, 10)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x + 35, y)

    def update(self):
        self.rect.y -= 50


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
        game_over = False
        run = True
        player = Player()
        player_sprites.add(player)
        fon_y = 0
        fon_y1 = -HEIGHT
        lets_c = 10
        lets = 0
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pause = not pause
                if pause and not game_over:
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
                        elif pause_menu.newgame_btn_check(x, y):
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
                            lets = 0
                        player.shot(event)
                    pause_menu.draw(x, y)
            if not pause and not game_over:
                keys = pygame.key.get_pressed()
                player.move(keys)
                player.shot(keys)
                player_sprites.update()
                bullets_sprites.update()
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
                bullets_sprites.draw(screen)
                if lets != lets_c:
                    for i in range(5):
                        Let(let_sprites)
                    lets += 5
                else:
                    enemy = Enemy()
                if player.lives == 0:
                    game_over = True
            if game_over:
                gameover = GameOverMenu()
                x, y = 0, 0
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if gameover.mainmenu_btn_check(x, y):
                        run = False
                        menu.start_btn_d = False
                        break
                    elif gameover.newgame_btn_check(x, y):
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
                        lets = 0
                gameover.draw(x, y)
            pygame.display.flip()
    else:
        running = False
pygame.quit()
