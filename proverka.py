import pygame
import os
import random
import sys

pygame.init()

FPS = 50
WIDTH = 1000
HEIGHT = 800

image = pygame.Surface([100, 100])
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()


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


def start_screen():

    curpos = [0, 0]
    cursor = load_image("arrow.png", pygame.Color('white'))
    cursor = pygame.transform.scale(cursor, (50, 50))
    intro_text = ["Здравствуйте!", "",
                  "Для начала игры",
                  "Нажмите любую клавишу"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    foneg = pygame.transform.scale(load_image('foneg.jpg'), (WIDTH, HEIGHT))
    fonlosash = pygame.transform.scale(load_image('fonlosash.jpg'), (WIDTH, HEIGHT))
    foncrosh = pygame.transform.scale(load_image('foncrosh.jpg'), (WIDTH, HEIGHT))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    running = True

    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif pygame.MOUSEBUTTONDOWN == event.type and 388 < event.pos[0] < 577 and \
                    711 > event.pos[1] > 431:
                Crosh()

            elif 388 < pygame.mouse.get_pos()[0] < 577 and \
                    711 > pygame.mouse.get_pos()[1] > 431:
                screen.blit(foncrosh, (0, 0))
                curpos = pygame.mouse.get_pos()

            elif 183 < pygame.mouse.get_pos()[0] < 348 and \
                    672 > pygame.mouse.get_pos()[1] > 386:
                screen.blit(fonlosash, (0, 0))
                curpos = pygame.mouse.get_pos()

            elif 626 < pygame.mouse.get_pos()[0] < 822 and \
                    688 > pygame.mouse.get_pos()[1] > 450:

                screen.blit(foneg, (0, 0))
                curpos = pygame.mouse.get_pos()
            elif pygame.MOUSEBUTTONDOWN == event.type and 626 < pygame.mouse.get_pos()[0] < 822 and \
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


class Bullet(pygame.sprite.Sprite):
    bullet = load_image("bullet.png", -1)
    bullet = pygame.transform.scale(bullet, (70, 70))

    def __init__(self, x, y):
        super().__init__(bullet_group)
        self.startX = x
        self.startY = y
        self.speed = 15
        self.image = Bullet.bullet
        self.xv = self.speed
        self.rect = self.image.get_rect().move(x, y)

    def update(self):
        self.rect.x += self.xv


class Crosh_bot(pygame.sprite.Sprite):
    image2 = load_image("crosh.png", -1)
    image2 = pygame.transform.scale(image2, (200, 200))

    def __init__(self, x, y):
        super().__init__(bot)
        self.image = Crosh_bot.image2
        self.rect = self.image.get_rect().move(x, y)
        self.life = 100
        self.FPS = 10

    def collide(self, bullet):
        if pygame.sprite.collide_rect(self, bullet):
            self.life -= 1
            if self.life < 0:
                Win()

    def crosh2(self):
        ch = random.choice(['DOWN', 'UP', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN',
                            'UP', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'UP',
                            'LEFT', 'RIGHT', 'DOWN', 'UP', 'DOWN', 'UP', 'LEFT',
                            'RIGHT', 'DOWN', 'UP', 'LEFT', 'RIGHT'])
        if 1000 > self.rect.x > 0 and 500 > self.rect.y > 0:
            if ch == 'DOWN':
                self.rect.x, self.rect.y = self.rect.x, self.rect.y + 15
                screen.blit(self.image2, [self.rect.x, self.rect.y])

            elif ch == 'UP':
                self.rect.x, self.rect.y = self.rect.x, self.rect.y - 15
                screen.blit(self.image2, [self.rect.x, self.rect.y])

            elif ch == 'LEFT':
                self.rect.x, self.rect.y = self.rect.x - 15, self.rect.y
                screen.blit(self.image2, [self.rect.x, self.rect.y])

            elif ch == 'RIGHT':
                self.rect.x, self.rect.y = self.rect.x + 15, self.rect.y
                screen.blit(self.image2, [self.rect.x, self.rect.y])

        elif self.rect.x >= 1000 or self.rect.y >= 500:
            self.rect.x, self.rect.y = self.rect.x - 20, self.rect.y - 20

        elif self.rect.x <= 0 or self.rect.y <= 0:
            self.rect.x, self.rect.y = self.rect.x + 20, self.rect.y + 20

        else:
            self.rect.x, self.rect.y = self.rect.x + 20, self.rect.y + 20
        screen.blit(self.image2, [self.rect.x, self.rect.y])
        clock.tick(self.FPS)


bot = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
bullets = []
crosh_bot = Crosh_bot(500, 100)

class Crosh():
    def __init__(self, pos=(100, 100), pos2=(500, 100)):
        self.image = load_image("creature1.png", -1)
        self.running = True
        self.pos = pos
        self.pos2 = pos2
        self.motion = 0
        self.size = 1000, 800
        self.FPS = 10
        self.screen = pygame.display.set_mode(size)
        pygame.mouse.set_visible(False)
        fon = pygame.transform.scale(load_image('secondfon.jpg'), (1000, 800))

        while self.running:
            screen.blit(fon, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
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
                        Menu(self.pos, self.pos2)
                    if event.key == pygame.K_SPACE:
                        bullets.append(Bullet(self.pos[0] + 100, self.pos[1] + 100))

            crosh_bot.crosh2()
            for x in bullets:
                crosh_bot.collide(x)

            if self.motion == 'DOWN':
                self.pos = [self.pos[0], self.pos[1] + 5]
            elif self.motion == 'UP':
                self.pos = [self.pos[0], self.pos[1] - 5]
            elif self.motion == 'LEFT':
                self.pos = [self.pos[0] - 5, self.pos[1]]
            elif self.motion == 'RIGHT':
                self.pos = [self.pos[0] + 5, self.pos[1]]

            screen.blit(self.image, self.pos)

            for x in bullets:
                x.update()
            bullet_group.draw(screen)
            pygame.display.flip()




class Menu:
    def __init__(self, pos, pos2):
        self.fonpause = pygame.transform.scale(load_image('fonpause.jpg'), (1000, 800))
        self.pos = pos
        self.pos2 = pos2
        self.running = True
        self.cursor = load_image("arrow.png", pygame.Color('white'))
        self.cursor = pygame.transform.scale(self.cursor, (50, 50))
        self.curpos = [0, 0]
        self.FPS = 50

        while self.running:
            screen.blit(self.fonpause, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Crosh(self.pos, self.pos2)

                elif event.type == pygame.MOUSEMOTION:
                    self.curpos = event.pos

            screen.blit(self.cursor, self.curpos)
            pygame.display.flip()
            clock.tick(self.FPS)




class Win():
    def __init__(self):
        self.running =  True
        self.fonwin  = pygame.transform.scale(load_image('fonwin.jpg'), (1000, 800))
        self.fonwinbutton = pygame.transform.scale(load_image('fonwinbutton.jpg'), (1000, 800))
        self.FPS = 50
        self.cursor = load_image("arrow.png", pygame.Color('white'))
        self.cursor = pygame.transform.scale(self.cursor, (50, 50))
        self.curpos = [0, 0]
        while self.running:
            screen.blit(self.fonwin, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start_screen()
                # elif 602 < pygame.mouse.get_pos()[0] < 788 and 648 > pygame.mouse.get_pos()[1] > 701:
                #     screen.blit(self.fonwinbutton, (0, 0))
                #     curpos = pygame.mouse.get_pos()

                elif event.type == pygame.MOUSEMOTION:
                    self.curpos = event.pos
                    print(event.pos)
            screen.blit(self.cursor, self.curpos)
            pygame.display.flip()
            clock.tick(self.FPS)


# переделать
# class Tile(pygame.sprite.Sprite):
#     def __init__(self, tile_type, pos_x, pos_y):
#         super().__init__(tiles_group, all_sprites)
#         self.image = tile_images[tile_type]
#         self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
#         self.abs_pos = (self.rect.x, self.rect.y)
#
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self, pos_x, pos_y):
#         super().__init__(player_group, all_sprites)
#         self.image = player_image
#         self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)
#         self.pos = (pos_x, pos_y)
#
#     def move(self, x, y):
#         camera.dx -= tile_width * (x - self.pos[0])
#         camera.dy -= tile_height * (y - self.pos[1])
#         self.pos = (x, y)
#         for sprite in tiles_group:
#             camera.apply(sprite)
#
#
# class Camera:
#     def __init__(self):
#         self.dx = 0
#         self.dy = 0
#
#     def apply(self, obj):
#         obj.rect.x = obj.abs_pos[0] + self.dx
#         obj.rect.y = obj.abs_pos[1] + self.dy
#
#     def update(self, target):
#         self.dx = 0
#         self.dy = 0
#
#
# def move(hero, movement):
#     x, y = hero.pos
#     if movement == 'up':
#         if y > 0 and level_map[y - 1][x] in '.@':
#             hero.move(x, y - 1)
#     elif movement == 'down':
#         if y < 10 and level_map[y + 1][x] in '.@':
#             hero.move(x, y + 1)
#     elif movement == 'left':
#         if x > 0 and level_map[y][x - 1] in '.@':
#             hero.move(x - 1, y)
#     elif movement == 'right':
#         if x < 10 and level_map[y][x + 1] in '.@':
#             hero.move(x + 1, y)
#
#
# def generate_level(level):
#     new_player, x, y = None, None, None
#     for y in range(len(level)):
#         for x in range(len(level[y])):
#             if level[y][x] == '.':
#                 Tile('empty', x, y)
#             elif level[y][x] == '#':
#                 Tile('wall', x, y)
#             elif level[y][x] == '@':
#                 Tile('empty', x, y)
#                 new_player = Player(x, y)
#     # вернем игрока, а также размер поля в клетках
#     return new_player, x, y
#
#
# def load_level(filename):
#     filename = "data/" + filename
#     # читаем уровень, убирая символы перевода строки
#     try:
#         with open(filename, 'r') as mapFile:
#             level_map = [line.strip() for line in mapFile]
#
#         # и подсчитываем максимальную длину
#         max_width = max(map(len, level_map))
#
#         # дополняем каждую строку пустыми клетками ('.')
#         return list(map(lambda x: x.ljust(max_width, '.'), level_map))
#     except Exception:
#         return 'Error'
#
#
# def terminate():
#     pygame.quit()
#     sys.exit()
#
#
# file_name = ''
# a = load_level(file_name)
# camera = Camera()
# clock = pygame.time.Clock()
#
# player = None
# tile_images = {'wall': load_image('box.png'), 'empty': load_image('grass.png')}
# player_image = load_image('mar.png')
#
# tile_width = tile_height = 50
#
# all_sprites = pygame.sprite.Group()
# tiles_group = pygame.sprite.Group()
# player_group = pygame.sprite.Group()
# sprite_group = pygame.sprite.Group()
#
# level_map = load_level(file_name)
# # player, level_x, level_y = generate_level(a)
# running = True
# camera.update(player)
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 move(player, 'up')
#             elif event.key == pygame.K_DOWN:
#                 move(player, 'down')
#             elif event.key == pygame.K_LEFT:
#                 move(player, 'left')
#             elif event.key == pygame.K_RIGHT:
#                 move(player, 'right')
#
#     screen.fill((0, 0, 0))
#     all_sprites.draw(screen)
#     player_group.draw(screen)
#     clock.tick(FPS)
#     pygame.display.flip()



start_screen()


