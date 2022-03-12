import pygame as pg
from utils import *
from random import uniform, randint, choice
from math import sqrt
from time import time


class Bird(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = images['bird']
        self.rect = self.image.get_rect()
        self.rect.midleft = (100, HEIGHT / 2)
        self.speed = 0

    def update(self):
        if game.state == 'play':
            self.speed += GRAVITY
            self.rect.y += self.speed

    def draw(self):
        game.screen.blit(self.image, self.rect)

    def jump(self):
        if game.state == 'play':
            self.speed -= JUMP_POWER
            if time() - game.last_jump > JUMP_SOUND_COOLDOWN:
                sounds['jump'].play()
                game.last_jump = time()


class Pipe(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = images['pipe']
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + 200
        y = randint(50, 150)
        if randint(0, 1) == 0:
            self.rect.y = HEIGHT + y - self.rect.height
        else:
            self.image = pg.transform.rotate(self.image, 180)
            self.rect.y = -y

    def update(self):
        self.rect.x -= game.scroll_speed
        if self.rect.right < 0:
            self.kill()
            game.score += 1
            sounds['score'].play()
            game.scroll_speed += 1

    def draw(self):
        game.screen.blit(self.image, self.rect)
