import pygame
import os
import random
import sys
from random import choice

pygame.init()

FPS = 50
WIDTH = 1000
HEIGHT = 800
GRAVITY = 0.5
screen_rect = (0, 0, WIDTH, HEIGHT)
CAR_TIMER = 1
pygame.time.set_timer(CAR_TIMER, 1000)

image = pygame.Surface([100, 100])
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

bot = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
buttons_group = pygame.sprite.Group()


all_sprites1 = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
sprite_group = pygame.sprite.Group()
carrot_group = pygame.sprite.Group()

bullets = []


def terminate():
    pygame.quit()
    sys.exit()


def load_music(name):
    fullname = os.path.join('data', name)
    music = pygame.mixer.Sound(fullname)
    return music


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            pygame.display.flip()
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


class Particle(pygame.sprite.Sprite):
    fire = [pygame.transform.scale(load_image("c05a5db323550c763f1f8088674bbd03.png", -1), (50, 50))]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(carrot_group)
        self.image = choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


class Menu:
    def __init__(self, pos):
        self.fonpause = pygame.transform.scale(load_image('fonpause.jpg'), (1000, 800))
        self.fonpause1 = pygame.transform.scale(load_image('fonpause1.jpg'), (1000, 800))
        self.fonpause2 = pygame.transform.scale(load_image('fonpause2.jpg'), (1000, 800))
        self.fonpause3 = pygame.transform.scale(load_image('fonpause3.jpg'), (1000, 800))
        self.fonpause4 = pygame.transform.scale(load_image('fonpause4.jpg'), (1000, 800))
        self.pos = pos
        self.running = True
        self.cursor = load_image("arrow.png", pygame.Color('white'))
        self.cursor = pygame.transform.scale(self.cursor, (50, 50))
        self.curpos = [0, 0]
        self.FPS = 50

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    terminate()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

                elif pygame.MOUSEBUTTONDOWN == event.type and 254 < pygame.mouse.get_pos()[0] < 502 and \
                         239 > pygame.mouse.get_pos()[1] > 197:
                    return

                elif 254 < pygame.mouse.get_pos()[0] < 502 and \
                         239 > pygame.mouse.get_pos()[1] > 197:
                    screen.blit(self.fonpause1, (0, 0))
                    self.curpos = pygame.mouse.get_pos()


                elif pygame.MOUSEBUTTONDOWN == event.type and 254 < pygame.mouse.get_pos()[0] < 502 and \
                         293 > pygame.mouse.get_pos()[1] > 255:
                    screen.blit(self.fonpause1, (0, 0))
                    crosh_bot.life = 100
                    self.curpos = pygame.mouse.get_pos()
                    return

                elif 254 < pygame.mouse.get_pos()[0] < 502 and \
                         293 > pygame.mouse.get_pos()[1] > 255:
                    screen.blit(self.fonpause2, (0, 0))
                    self.curpos = pygame.mouse.get_pos()

                elif 254 < pygame.mouse.get_pos()[0] < 502 and \
                         293 > pygame.mouse.get_pos()[1] > 255:
                    screen.blit(self.fonpause2, (0, 0))
                    self.curpos = pygame.mouse.get_pos()

                elif pygame.MOUSEBUTTONDOWN == event.type and 261 < pygame.mouse.get_pos()[0] < 480 and \
                        361 > pygame.mouse.get_pos()[1] > 313:
                    pygame.quit()
                    terminate()

                elif 261 < pygame.mouse.get_pos()[0] < 480 and \
                        361 > pygame.mouse.get_pos()[1] > 313:
                    screen.blit(self.fonpause3, (0, 0))
                    self.curpos = pygame.mouse.get_pos()

                elif pygame.MOUSEBUTTONDOWN == event.type and 261 < pygame.mouse.get_pos()[0] < 480 and \
                        427 > pygame.mouse.get_pos()[1] > 382:
                    self.curpos = pygame.mouse.get_pos()
                    start_screen()

                elif 261 < pygame.mouse.get_pos()[0] < 480 and \
                        427 > pygame.mouse.get_pos()[1] > 382:
                    screen.blit(self.fonpause4, (0, 0))
                    self.curpos = pygame.mouse.get_pos()

                elif event.type == pygame.MOUSEMOTION:
                    self.curpos = event.pos
                    screen.blit(self.fonpause, (0, 0))

                else:
                    screen.blit(self.fonpause, (0, 0))

            screen.blit(self.cursor, self.curpos)
            pygame.display.flip()
            clock.tick(self.FPS)


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)

        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)

        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Bullet(pygame.sprite.Sprite):
    bullet = load_image("bullet.png", -1)
    bullet = pygame.transform.scale(bullet, (50, 50))

    def __init__(self, x, y):
        super().__init__(bullet_group, all_sprites)
        self.startX = x
        self.startY = y
        self.speed = 15
        self.c = 0
        self.image = Bullet.bullet
        self.xv = self.speed
        self.rect = self.image.get_rect().move(x, y)

    def update(self):
        self.rect.x += self.xv


class Crosh_bot(pygame.sprite.Sprite):

    image2 = load_image("crosh.png", -1)
    image2 = pygame.transform.scale(image2, (200, 200))

    def __init__(self, x, y):
        super().__init__(bot, all_sprites)
        self.image = Crosh_bot.image2
        self.rect = self.image.get_rect().move(x, y)
        self.life = 100
        self.FPS = 10
        self.vx = 0
        self.vy = 15
        self.bullets = []
        self.all_bullets = []

    def collide(self, bullet):
        if pygame.sprite.collide_rect(self, bullet) and bullet not in self.bullets:
            self.life -= 10
            self.bullets.append(bullet)
            bullet.image = pygame.transform.scale(load_image('boom.png', (0, 0, 0)), (50, 50))
            if self.life < 0:
                Win()
        elif pygame.sprite.collide_rect(self, bullet):
            bullet.c += 1
        else:
            self.rect = self.rect.move(self.vx, self.vy)
        self.all_bullets.append(bullet)
        if bullet.c == 8:
            bullet_group.remove(bullet)
            all_sprites.remove(bullet)

        if pygame.sprite.spritecollideany(self, horizontal_borders):
            if self.rect.y < 100:
                self.rect.y += 20
            else:
                self.rect.y -= 20

        if pygame.sprite.spritecollideany(self, vertical_borders):
            if self.rect.x < 100:
                self.rect.x += 20
            else:
                self.rect.x -= 20

    def update(self):
        self.crosh2()
        self.rect = self.rect.move(self.vx, self.vy)

    def crosh2(self):
        self.direction = random.choice(['DOWN', 'UP', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN',
                                        'UP', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'UP',
                                        'LEFT', 'RIGHT', 'DOWN', 'UP', 'DOWN', 'UP', 'LEFT',
                                        'RIGHT', 'DOWN', 'UP', 'LEFT', 'RIGHT'])
        if self.direction == 'DOWN':
            self.vx, self.vy = 0, 10

        elif self.direction == 'UP':
            self.vx, self.vy = 0, -10

        elif self.direction == 'LEFT':
            self.vx, self.vy = -10, 0

        elif self.direction == 'RIGHT':
            self.vx, self.vy = 10, 0


Border(5, 5, WIDTH - 5, 5)
Border(5, HEIGHT - 5, WIDTH - 5, HEIGHT - 5)
Border(5, 5, 5, HEIGHT - 5)
Border(WIDTH - 5, 5, WIDTH - 5, HEIGHT - 5)

crosh_bot = Crosh_bot(500, 100)


def create_particles(position):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, choice(numbers), choice(numbers))


class Win:
    fonwin = load_image('fonwin.jpg')
    fonwin = pygame.transform.scale(fonwin, (1000, 800))
    fonwinbutton = load_image('fonwinbutton.jpg')
    fonwinbutton = pygame.transform.scale(fonwinbutton, (270, 80))
    cursor = load_image("arrow.png", pygame.Color('white'))
    cursor = pygame.transform.scale(cursor, (50, 50))

    def __init__(self):
        self.running = True
        self.fonwin = Win.fonwin
        self.fonwinbutton = Win.fonwinbutton
        self.FPS = 50
        self.cursor = Win.cursor
        self.curpos = [0, 0]
        crosh_bot.__init__(500, 100)

        while self.running:
            play = pygame.sprite.Sprite()
            buttons_group.add(play)

            play.image = Win.fonwinbutton
            play.rect = play.image.get_rect()
            play.rect.x = 620
            play.rect.y = 670

            screen.blit(self.fonwin, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start_screen()
                        self.running = False

                if event.type == pygame.MOUSEMOTION:
                    self.curpos = event.pos

                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    if play.rect.collidepoint(x, y):
                        start_screen()
                        break
                if event.type == CAR_TIMER:
                    create_particles((400, 0))
            carrot_group.update()
            carrot_group.draw(screen)
            buttons_group.draw(screen)
            screen.blit(self.cursor, self.curpos)
            pygame.display.flip()
            clock.tick(self.FPS)

        pygame.display.flip()


class Crosh:
    def __init__(self, pos=(100, 100)):
        self.image = load_image("creature1.png", -1)
        self.running = True
        self.pos = pos
        self.motion = 0
        self.size = 1000, 800
        self.FPS = 10
        self.screen = pygame.display.set_mode(size)
        pygame.mouse.set_visible(False)
        fon = pygame.transform.scale(load_image('secondfon.jpg'), (1000, 800))

        while self.running:
            clock.tick(self.FPS)
            screen.blit(fon, (0, 0))
            pygame.draw.line(screen, pygame.Color('green'), (600, 50), (600 + crosh_bot.life * 2, 50), 10)
            pygame.draw.rect(screen, pygame.Color('red'), (600, 40, 200, 20), 10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    start_screen()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.motion = 'DOWN'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.motion = 'UP'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.motion = 'LEFT'

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.motion = 'RIGHT'

                if event.type == pygame.KEYUP:
                    self.motion = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Menu(self.pos)

                    if event.key == pygame.K_SPACE:
                        bullets.append(Bullet(self.pos[0] + 100, self.pos[1] + 100))

            crosh_bot.update()

            for x in bullets:
                crosh_bot.collide(x)

            if self.motion == 'DOWN':
                self.pos = [self.pos[0], self.pos[1] + 10]

            elif self.motion == 'UP':
                self.pos = [self.pos[0], self.pos[1] - 10]

            elif self.motion == 'LEFT':
                self.pos = [self.pos[0] - 10, self.pos[1]]

            elif self.motion == 'RIGHT':
                self.pos = [self.pos[0] + 10, self.pos[1]]

            screen.blit(self.image, self.pos)

            for x in bullets:
                x.update()

            bullet_group.draw(screen)
            all_sprites.draw(screen)
            pygame.display.flip()


###########################################################
### Начало лабиринта Ежика
###########################################################
def hedgehog_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                return

        screen.fill((3, 157, 252))
        font = pygame.font.Font(None, 70)
        text = font.render('Для начала игры нажмите Tab', 1, pygame.Color('red'))
        intro_text = ["Передвигаясь с помощью стрелок,",
                      "найдите выход из лабиринта"]

        x, y = 50, 350

        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            y += 50
            screen.blit(string_rendered, (x, y))

        screen.blit(text, (160, 270))

        pygame.display.flip()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites1)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.abs_pos = (self.rect.x, self.rect.y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        global camera, tile_width, tile_height, player, tile_images, player_image, level_map
        super().__init__(player_group)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        global win
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(tile_width * self.pos[0], tile_height * self.pos[1])
        if any([self.pos == x for x in win]):
            Win()


class Camera(object):
    def __init__(self, camera_f, width, height):
        self.camera_f = camera_f
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, obj):
        return obj.rect.move(self.state.topleft)

    def update(self, obj):
        self.state = self.camera_f(self.state, obj.rect)


def camera_f(camera, obj_rect):
    left_board, top_board = obj_rect[0], obj_rect[1]
    w, h = camera[2], camera[3]
    left_board, top_board = -left_board + WIDTH / 2, -top_board + HEIGHT / 2

    left_board = min(0, left_board)
    left_board = max(-(camera.width - WIDTH), left_board)
    top_board = max(-(camera.height - HEIGHT), top_board)
    top_board = min(0, top_board)

    return pygame.Rect(left_board, top_board, w, h)


def move(hero, movement):
    x, y = hero.pos
    if movement == 'up':
        if y > 0 and level_map[y - 1][x] in '.@$':
            hero.move(x, y - 1)
    elif movement == 'down':
        if y < 44 and level_map[y + 1][x] in '.@$':
            hero.move(x, y + 1)
    elif movement == 'left':
        if x > 0 and level_map[y][x - 1] in '.@$':
            hero.move(x - 1, y)
    elif movement == 'right':
        if x < 44 and level_map[y][x + 1] in '.@$':
            hero.move(x + 1, y)


def generate_level(level):
    global camera, tile_width, tile_height, player, tile_images, player_image, level_map, win
    new_player, x, y, win = None, None, None, []
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == '$':
                Tile('empty', x, y)
                win.append((x, y))

    # вернем игрока, а также размер поля в клетках
    return new_player, x, y, win


def load_level(filename):
    global camera, tile_width, tile_height, player, tile_images, player_image, level_map
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    try:
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]

        # и подсчитываем максимальную длину
        max_width = max(map(len, level_map))

        # дополняем каждую строку пустыми клетками ('.')
        return list(map(lambda x: x.ljust(max_width, '.'), level_map))
    except Exception:
        return 'Error'


def start_game_heg():
    global camera, tile_width, tile_height, player, tile_images, player_image, level_map, win
    file_name = 'map.txt'
    a = load_level(file_name)

    if a != 'Error':

        clock = pygame.time.Clock()
        pygame.init()
        size = WIDTH, HEIGHT
        screen = pygame.display.set_mode(size)

        FPS = 50

        player = None
        tile_images = {'wall': load_image('block.png'), 'empty': load_image('grass.png')}
        player_image = pygame.transform.scale(load_image('eg.png', pygame.Color('white')), (50, 50))

        tile_width = tile_height = 50

        hedgehog_game()
        level_map = load_level(file_name)
        player, level_x, level_y, win = generate_level(a)
        total_level_width = len(level_map[0]) * tile_width
        total_level_height = len(level_map) * tile_height
        all_sprites1.add(player)
        camera = Camera(camera_f, total_level_width, total_level_height)
        running = True
    else:
        running = False
    camera.update(player)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Menu(pygame.mouse.get_pos())

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    move(player, 'up')
                elif event.key == pygame.K_DOWN:
                    move(player, 'down')
                elif event.key == pygame.K_LEFT:
                    move(player, 'left')
                elif event.key == pygame.K_RIGHT:
                    move(player, 'right')

        screen.fill((0, 0, 0))
        camera.update(player)
        for e in all_sprites1:
            screen.blit(e.image, camera.apply(e))
        clock.tick(FPS)
        pygame.display.flip()


def crosh_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                start_screen()
                running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                Crosh()

        screen.fill((3, 157, 252))
        font = pygame.font.Font(None, 70)
        text = font.render('Для начала игры нажмите Tab', 1, pygame.Color('red'))
        intro_text = ["Нажимая на пробел ", "и передвигаясь с помощью стрелок,",
                      "постарайтесь попасть в Нового Кроша"]

        x, y = 50, 350

        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            y += 50
            screen.blit(string_rendered, (x, y))

        screen.blit(text, (160, 270))

        pygame.display.flip()


def start_screen():
    curpos = [0, 0]
    cursor = load_image("arrow.png", pygame.Color('white'))
    cursor = pygame.transform.scale(cursor, (50, 50))
    fon = load_image('fon.jpg')
    fon = pygame.transform.scale(fon, (WIDTH, HEIGHT))
    foneg = load_image('foneg.jpg')
    foneg = pygame.transform.scale(foneg, (WIDTH, HEIGHT))
    fonlosash = load_image('fonlosash.jpg')
    fonlosash = pygame.transform.scale(fonlosash, (WIDTH, HEIGHT))
    foncrosh = load_image('foncrosh.jpg')
    foncrosh = pygame.transform.scale(foncrosh, (WIDTH, HEIGHT))
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()

            elif pygame.MOUSEBUTTONDOWN == event.type and 388 < event.pos[0] < 577 and \
                    711 > event.pos[1] > 431:
                crosh_game()

            elif 388 < pygame.mouse.get_pos()[0] < 577 and \
                    711 > pygame.mouse.get_pos()[1] > 431:
                screen.blit(foncrosh, (0, 0))
                curpos = pygame.mouse.get_pos()

            elif 183 < pygame.mouse.get_pos()[0] < 348 and \
                    672 > pygame.mouse.get_pos()[1] > 386:
                screen.blit(fonlosash, (0, 0))
                curpos = pygame.mouse.get_pos()

            elif pygame.MOUSEBUTTONDOWN == event.type and 626 < pygame.mouse.get_pos()[0] < 822 and \
                    688 > pygame.mouse.get_pos()[1] > 450:
                screen.blit(foneg, (0, 0))
                curpos = pygame.mouse.get_pos()
                start_game_heg()

            elif 626 < pygame.mouse.get_pos()[0] < 822 and \
                    688 > pygame.mouse.get_pos()[1] > 450:
                screen.blit(foneg, (0, 0))
                curpos = pygame.mouse.get_pos()

            elif event.type == pygame.MOUSEMOTION:
                curpos = event.pos
                screen.blit(fon, (0, 0))

            else:
                screen.blit(fon, (0, 0))

        screen.blit(cursor, curpos)
        pygame.display.flip()

start_screen()
