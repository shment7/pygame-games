from utils import *
from math import sqrt
from time import time


class Card(pg.sprite.Sprite):
    def __init__(self, i, r, c):
        super().__init__()
        self.image = images[str(i) + '.png']
        self.image_num = i
        self.shown_image = images['back.png']
        self.rect = self.shown_image.get_rect()
        self.rect.topleft = (WIDTH * c / COLS, HEIGHT * r / ROWS)
        self.is_flipped = False
        self.is_paired = False

    def update(self):
        pass

    def draw(self):
        game.screen.blit(self.shown_image, self.rect)

    def flip(self):
        if self.shown_image == images['back.png']:
            self.shown_image = self.image
            self.is_flipped = True
        else:
            self.shown_image = images['back.png']
            self.is_flipped = False


def create_board():
    l = [i for i in range(ROWS * COLS // 2)] + [i for i in range(ROWS * COLS // 2)]
    shuffle(l)
    board = [[0 for c in range(COLS)] for r in range(ROWS)]
    i = 0
    for c in range(COLS):
        for r in range(ROWS):
            board[r][c] = Card(l[i], r, c)
            i += 1

    return board
