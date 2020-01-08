import pygame
import os
import random
import sys
pygame.init()
FPS = 50

pygame.init()
image = pygame.Surface([100, 100])
size = 1000, 800
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

def load_image(name, colorkey=0, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None: 
        if colorkey == 0:
            color_key = image.get_at((0, 0))
            pygame.display.flip()
        image.set_colorkey(color_key)
    elif colorkey == 2:
        pass
    else:
        image = image.convert_alpha()

    return image


def start_screen():
    WIDTH = 1000
    HEIGHT = 800
    curpos = [0, 0]
    cursor = load_image("arrow.png")
    cursor = pygame.transform.scale(cursor, (50, 50))
    intro_text = ["Здравствуйте!", "",
                  "Для начала игры",
                  "Нажмите любую клавишу"]

    fon = pygame.transform.scale(load_image('fon.jpg', 1), (WIDTH, HEIGHT))
    foneg = pygame.transform.scale(load_image('foneg.jpg', 1), (WIDTH, HEIGHT))
    fonlosash = pygame.transform.scale(load_image('fonlosash.jpg', 1), (WIDTH, HEIGHT))
    foncrosh = pygame.transform.scale(load_image('foncrosh.jpg', 1), (WIDTH, HEIGHT))
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 388 and event.pos[0] < 577 and event.pos[1] < 711 and event.pos[1] > 431:
                Crosh()
            elif pygame.mouse.get_pos()[0] > 388 and pygame.mouse.get_pos()[0] < 577 and pygame.mouse.get_pos()[1] < 711 and pygame.mouse.get_pos()[1] > 431:
                screen.blit(foncrosh, (0, 0))
                curpos = pygame.mouse.get_pos()
            elif pygame.mouse.get_pos()[0] > 183 and pygame.mouse.get_pos()[0] < 348 and pygame.mouse.get_pos()[1] < 672 and pygame.mouse.get_pos()[1] > 386:
                screen.blit(fonlosash, (0, 0))
                curpos = pygame.mouse.get_pos()
            elif pygame.mouse.get_pos()[0] > 626 and pygame.mouse.get_pos()[0] < 822 and pygame.mouse.get_pos()[1] < 688 and pygame.mouse.get_pos()[1] > 450:
                screen.blit(foneg, (0, 0))
                curpos = pygame.mouse.get_pos()

            elif event.type == pygame.MOUSEMOTION:
                curpos = event.pos
                screen.blit(fon, (0, 0))
            else:
                screen.blit(fon, (0, 0))
        screen.blit(cursor, curpos)
        pygame.display.flip()
        clock.tick(FPS)


class Crosh():
    def __init__(self, pos=[100,100], pos2=[500, 100]):
        self.image = self.load_image("creature.png", 0)
        self.image2 = self.load_image("crosh.png", 0)
        self.image2 = pygame.transform.scale(self.image2, (200, 200))
        self.running = True
        self.pos = pos
        self.pos2 = pos2
        self.motion = 0
        self.size = 1000, 800
        self.FPS = 10
        self.screen = pygame.display.set_mode(size)
        pygame.mouse.set_visible(False)
        clock = pygame.time.Clock()
        fon = pygame.transform.scale(load_image('secondfon.jpg', 1), (1000, 800))

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

            self.crosh2()

            if self.motion == 'DOWN':
                self.pos = [self.pos[0], self.pos[1] + 5]
            elif self.motion == 'UP':
                self.pos = [self.pos[0], self.pos[1] - 5]
            elif self.motion == 'LEFT':
                self.pos = [self.pos[0] - 5, self.pos[1]]
            elif self.motion == 'RIGHT':
                self.pos = [self.pos[0] + 5, self.pos[1]]

            screen.blit(self.image, self.pos)

            pygame.display.flip()


    def crosh2(self):
        global pos2
        ch = random.choice(['DOWN', 'UP', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'UP', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'UP', 'DOWN', 'UP', 'LEFT', 'RIGHT', 'DOWN', 'UP', 'LEFT', 'RIGHT'])
        if self.pos2[0] < 1000 and self.pos2[1] < 500 and self.pos2[0] > 0 and self.pos2[1] > 0:
            if ch == 'DOWN':
                self.pos2 = [self.pos2[0], self.pos2[1] + 15]
                screen.blit(self.image2, self.pos2)

            elif ch == 'UP':
                self.pos2 = [self.pos2[0], self.pos2[1] - 15]
                screen.blit(self.image2, self.pos2)

            elif ch == 'LEFT':
                self.pos2 = [self.pos2[0] - 15, self.pos2[1]]
                screen.blit(self.image2, self.pos2)

            elif ch == 'RIGHT':
                pos2 = [self.pos2[0] + 15, self.pos2[1]]
                screen.blit(self.image2, self.pos2)


        elif self.pos2[0] >= 1000 or self.pos2[1] >= 500:
            self.pos2 = [self.pos2[0] - 20, self.pos2[1] - 20]
        elif self.pos2[0] <= 0 or self.pos2[1] <= 0:
            self.pos2 = [self.pos2[0] + 20, self.pos2[1] + 20]
        else:
            self.pos2 = [self.pos2[0] + 20, self.pos2[1] + 20]
        screen.blit(self.image2, self.pos2)
        clock.tick(self.FPS)

    def load_image(self, name, colorkey=0, color_key=None):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname).convert()
        if colorkey is not None:
            if colorkey == 0:
                color_key = image.get_at((0, 0))
                pygame.display.flip()
            image.set_colorkey(color_key)
        elif colorkey == 2:
            pass
        else:
            image = image.convert_alpha()

        return image

class Menu:
    def __init__(self, pos, pos2):
        self.fonpause = pygame.transform.scale(load_image('fonpause.jpg', 1), (1000, 800))
        self.pos = pos
        self.pos2 = pos2
        self.running = True
        self.cursor = load_image("arrow.png")
        self.cursor = pygame.transform.scale(self.cursor, (50, 50))
        self.curpos = [0, 0]
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





start_screen()
