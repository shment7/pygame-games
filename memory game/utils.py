import pygame as pg
from settings import *
from os import listdir
from random import uniform, randint, choice, shuffle

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.mixer.init()
        pg.mixer.music.load('sounds/music.wav')
        pg.mixer.music.set_volume(MUSIC_VOLUME)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT + SCORE_SIZE])
        self.running = True
        self.state = 'play' # 'game over', 'play'
        self.score = 0
        self.guess = 0
        self.first_flip = None
        self.second_flip = None
        self.third_flip = None

    def write_text(self, text, pos, size, color):
        font = pg.font.SysFont('Arial', size)
        textSurface = font.render(text, True, color)
        self.screen.blit(textSurface, pos)


def load_image(path, scale):
    image = pg.image.load(path)
    w, h = image.get_size()
    return pg.transform.scale(image, (w * scale, h * scale))

def load_images():
    images = {}
    files = [f for f in listdir('images')]
    for f in files:
        images[f] = load_image('images/' + f, CARD_SCALE)

    return images

def load_sounds():
    sounds = {}
    sounds['pair'] = pg.mixer.Sound('sounds/pair.wav')
    sounds['fail'] = pg.mixer.Sound('sounds/fail.wav')
    return sounds


game = Game()
images = load_images()
sounds = load_sounds()
