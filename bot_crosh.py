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
