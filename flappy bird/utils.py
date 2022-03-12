import pygame as pg
from settings import *

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.mixer.init()
        pg.mixer.music.load('sounds/music.mp3')
        pg.mixer.music.set_volume(MUSIC_VOLUME)
        pg.mixer.music.play(loops=-1)
        self.pipes = pg.sprite.Group()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.running = True
        self.state = 'start' # 'pause', 'play', 'start'
        self.score = 0
        self.scroll_speed = 5
        self.last_jump = 0
        pg.time.set_timer(ADD_PIPE, PIPE_FREQ)

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
    images['pipe'] = load_image('images/pipe.png', PIPE_SCALE)
    images['bird'] = load_image('images/bird.png', BIRD_SCALE)
    images['background'] = load_image('images/background.png', 1)
    return images


def load_sounds():
    sounds = {}
    sounds['explosion'] = pg.mixer.Sound('sounds/explosion.wav')
    sounds['jump'] = pg.mixer.Sound('sounds/jump.wav')
    sounds['score'] = pg.mixer.Sound('sounds/score.wav')
    return sounds


game = Game()
images = load_images()
sounds = load_sounds()
