import pygame as pg
from utils import *
from random import uniform, randint, choice
from math import sqrt
from time import time

class BaseSprite(pg.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()

    def draw(self):
        if game.state != 'game over':
            game.screen.blit(self.image, self.rect)

    def update(self):
        pass

class Ship(BaseSprite):
    def __init__(self, image):
        super().__init__(image)
        self.rect.midbottom = (WIDTH / 2, HEIGHT)
        self.last_shot = 0
        self.cooldown = 0.3
        self.hearts = 5

    def update(self):
        super().update()

    def draw(self):
        super().draw()
        for i in range(self.hearts):
            game.screen.blit(images['heart'], pg.Rect(WIDTH - 50 * (i + 1), 20, 20, 20))

    def move(self, dir):
        if dir == 'up' and self.rect.top > 0:
            self.rect.top -= SHIP_SPEED
        elif dir == 'down' and self.rect.bottom < HEIGHT:
            self.rect.bottom += SHIP_SPEED

        if dir == 'left' and self.rect.left > 0:
            self.rect.left -= SHIP_SPEED
        elif dir == 'right' and self.rect.right < WIDTH:
            self.rect.right += SHIP_SPEED

    def shoot(self):
        if time() - self.last_shot >= self.cooldown:
            sounds['laser'].play()
            self.last_shot = time()
            game.lasers.add(Laser(images['laser'], self.rect.midtop))


class Laser(BaseSprite):
    def __init__(self, image, pos):
        super().__init__(image)
        self.rect.midbottom = pos

    def update(self):
        if game.state == 'play':
            self.rect.top -= LASER_SPEED
            if self.rect.top < 0:
                self.kill()


class Pill(BaseSprite):
    def __init__(self, image):
        super().__init__(image)
        self.rect.midbottom = (randint(20, WIDTH - 20), -20)

    def update(self):
        if game.state == 'play':
            self.rect.top += PILL_SPEED
            if self.rect.top > HEIGHT:
                self.kill()


class Meteor(BaseSprite):
    def __init__(self, image, speed):
        super().__init__(image)
        self.speed = speed
        self.rect.center = (randint(0, WIDTH), -100)
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

        self.dir = pg.math.Vector2((uniform(-2, 2), 1)).normalize()
        self.entered = False

    def update(self):
        if game.state == 'play':
            if self.rect.top > 0:
                self.entered = True

            self.rect.x += self.dir.x * self.speed
            self.rect.y += self.dir.y * self.speed
            if self.rect.right > WIDTH or self.rect.left < 0:
                self.dir.x *= -1
                if self.dir.y < 0:
                    self.dir.y *= -1
            elif self.entered and (self.rect.top < 0 or self.rect.bottom > HEIGHT):
                self.dir.y *= -1

            if self.rect.top > HEIGHT:
                self.kill()
