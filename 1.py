import pygame
from time import monotonic
from random import randrange

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
pygame.display.set_caption('Game')
fon = pygame.image.load('data/fon.png')
fon = pygame.transform.scale(fon, (WIDTH, HEIGHT))
bullets_sprites = pygame.sprite.Group()
health_sprites = pygame.sprite.Group()
health_bonus_sprites = pygame.sprite.Group()
shield_bonus_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
points = 0
FPS = 100


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
        font = pygame.font.Font(None, 200)
        string_rendered = font.render('Очки: ' + str(points), 1, pygame.Color('yellow'))
        intro_rect = string_rendered.get_rect()
        intro_rect.x = WIDTH // 2 - 10
        intro_rect.y = HEIGHT // 3
        screen.blit(string_rendered, intro_rect)
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
        self.image = pygame.image.load('data/player_p.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 70)
        self.mask = pygame.mask.from_surface(self.image)
        self.start = monotonic()
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
        if round(monotonic() - self.start) < 3:
            self.image = pygame.image.load('data/player_p.png')
        else:
            self.image = pygame.image.load('data/player.png')
        if pygame.sprite.spritecollideany(self, health_bonus_sprites):
            self.lives += 1
            for i in health_bonus_sprites:
                health_bonus_sprites.remove(i)

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

    def shot(self):
        shot = Bullet(self.rect.x, self.rect.y, -50, 22.5)
        bullets_sprites.add(shot)

    def draw_health(self):
        current_y = 40
        current_x = 40
        for i in health_sprites:
            health_sprites.remove(i)
        for i in range(self.lives):
            heart = Health(current_x, current_y)
            health_sprites.add(heart)
            current_x += 70


class Health(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/live.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_lives):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, -90)
        self.rect.y = -90
        self.mask = pygame.mask.from_surface(self.image)
        self.appearence = True
        self.lives = enemy_lives
        self.shot_time = monotonic()

    def update(self):
        if self.appearence:
            print(self.rect.y)
            self.rect.y += 10
            if self.rect.y == 90:
                self.appearence = False
        else:
            b_in_let = False
            for i in let_sprites:
                if pygame.sprite.collide_mask(self, i):
                    b_in_let = True
            if not b_in_let:
                self.rect.center = (player.rect.x + 10, player.rect.y // 4 - 40)
                self.rect.x = player.rect.x
                self.rect.y = player.rect.y // 4 - 40
            if round(monotonic() - self.shot_time) % 2 == 0:
                shot = Bullet(self.rect.x, self.rect.y, 50, 50)
                enemy_bullets_sprites.add(shot)


class Let(pygame.sprite.Sprite):
    def __init__(self, group, speed):
        pygame.sprite.Sprite.__init__(self, group)
        w = randrange(30, 100)
        h = randrange(30, w + 10)
        w = randrange(20, 100)
        h = randrange(20, w + 10)
        self.image = pygame.image.load('data/let.png')
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = randrange(10, WIDTH - w)
        self.rect.y = randrange(-HEIGHT, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed

    def update(self):
        if pygame.sprite.collide_mask(self, player) and round(monotonic() - player.start) > 3:
            player.lives -= 1
            player.start = monotonic()
            player.rect.center = (WIDTH / 2, HEIGHT - 70)
            self.kill()
        if self.rect.y > HEIGHT:
            self.kill()
        else:
            self.rect = self.rect.move(0, self.speed)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, s, x_s):
        pygame.sprite.Sprite.__init__(self)
        self.s = s
        if s == -50:
            self.image = pygame.image.load('data/bullet_p.png')
        else:
            self.image = pygame.image.load('data/bullet_e.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x + x_s, y)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global points
        b_in_let = False
        for i in let_sprites:
            if pygame.sprite.collide_mask(self, i):
                b_in_let = True
                self.kill()
                i.kill()
                points += 1
                break
        if pygame.sprite.collide_mask(self, player) and self.s == 50:
            if round(monotonic() - player.start) > 3:
                player.lives -= 1
                player.start = monotonic()
                self.kill()
        if enemy_live:
            if pygame.sprite.collide_mask(self, enemy) and self.s == -50:
                enemy.lives -= 1
                self.kill()
        if not b_in_let:
            self.rect.y += self.s
        if self.rect.y < 0 or self.rect.y > HEIGHT:
            self.kill()


class Bonus(pygame.sprite.Sprite):
    def __init__(self, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        if type == 1:
            self.image.fill((255, 255, 255))
        elif type == 2:
            self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = randrange(10, WIDTH - 10)
        self.rect.y = 0

    def update(self):
        self.rect.y += 15

    pass


def new_game():
    global player_sprites, enemy_sprites, let_sprites, bonus_sprites, player, points
    global player_sprites, enemy_sprites, let_sprites, bonus_sprites, player
    global enemy_bullets_sprites, pause, game_over, run, enemy_live, player_sprites, fon_y, fon_y1
    global lets_c, lets, start_t, time_without_enemy, live_im, speed, enemy_lives
    player_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    let_sprites = pygame.sprite.Group()
    bonus_sprites = pygame.sprite.Group()
    enemy_bullets_sprites = pygame.sprite.Group()
    pause = False
    game_over = False
    run = True
    enemy_live = False
    player = Player()
    player_sprites.add(player)
    fon_y = 0
    fon_y1 = -HEIGHT
    lets_c = 10
    lets = 0
    start_t = monotonic()
    time_without_enemy = monotonic()
    live_im = pygame.image.load('data/live.png')
    speed = 8
    enemy_lives = 5
    points = 0


def draw_points():
    font = pygame.font.Font(None, 50)
    string_rendered = font.render('Очки: ' + str(points), 1, pygame.Color('yellow'))
    intro_rect = string_rendered.get_rect()
    intro_rect.x = WIDTH - 150
    intro_rect.y = HEIGHT - 50
    screen.blit(string_rendered, intro_rect)


def draw_enemy_live(lives):
    if lives != 0:
        pygame.draw.rect(screen, (0, 255, 0), (WIDTH - lives * 20 - 10, 10, lives * 20, 20))


menu = Menu()
pause_menu = PauseMenu()
running = True
while running:
    menu.draw()
    if menu.start_btn_d:
        new_game()
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pause = not pause
                if not pause and not game_over:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        player.shot()
                elif pause and not game_over:
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
                            new_game()
                    pause_menu.draw(x, y)
            if not pause and not game_over:
                keys = pygame.key.get_pressed()
                if not enemy_live:
                    print(monotonic() - time_without_enemy)
                    if round(monotonic() - time_without_enemy) % 30 == 0 and \
                            round(monotonic() - time_without_enemy) != 0:
                        enemy_live = True
                        enemy = Enemy(enemy_lives)
                        enemy_sprites.add(enemy)
                player.move(keys)
                player_sprites.update()
                player.draw_health()
                bullets_sprites.update()
                enemy_sprites.update()
                enemy_bullets_sprites.update()
                health_bonus_sprites.update()
                shield_bonus_sprites.update()
                screen.blit(fon, (0, fon_y))
                screen.blit(fon, (0, fon_y1))
                fon_y += speed
                fon_y1 += speed
                if fon_y > HEIGHT:
                    fon_y = -HEIGHT
                elif fon_y1 > HEIGHT:
                    fon_y1 = -HEIGHT
                let_sprites.draw(screen)
                let_sprites.update()
                player_sprites.draw(screen)
                bullets_sprites.draw(screen)
                enemy_bullets_sprites.draw(screen)
                health_sprites.draw(screen)
                enemy_sprites.draw(screen)
                health_bonus_sprites.draw(screen)
                shield_bonus_sprites.draw(screen)
                draw_points()
                if not enemy_live and not round(monotonic() - time_without_enemy) % 28 == 0:
                    if round(monotonic() - start_t) % 4 == 0:
                        Let(let_sprites, speed)
                        for i in range(2):
                            Let(let_sprites, speed)
                elif enemy_live:
                    if enemy.lives == 0:
                        enemy_live = False
                        points += enemy_lives
                        bonus_type = 1
                        if bonus_type == 1:
                            health_bonus_sprites.add(Bonus(1))
                        elif bonus_type == 2:
                            shield_bonus_sprites.add(Bonus(2))
                        time_without_enemy = monotonic()
                        enemy.kill()
                        if speed < 32:
                            speed += 4
                            FPS += 4
                        if enemy_live < 10:
                            enemy_lives += 1
                    draw_enemy_live(enemy.lives)
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
                        new_game()
                gameover.draw(x, y)
            pygame.display.flip()
    else:
        running = False
pygame.quit()
