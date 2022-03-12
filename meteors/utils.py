import pygame as pg
from settings import *

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.mixer.init()
        pg.mixer.music.load('sounds/music.wav')
        pg.mixer.music.set_volume(MUSIC_VOLUME)
        pg.mixer.music.play(loops=-1)
        self.sprites = pg.sprite.Group()
        self.lasers = pg.sprite.Group()
        self.meteors = pg.sprite.Group()
        self.pills = pg.sprite.Group()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.running = True
        self.state = 'play' # 'pause', 'play', 'game over'
        self.score = 0
        self.meteors_freq = 3000
        self.meteors_speed = METEOR_SPEED
        pg.time.set_timer(ADD_METEOR, self.meteors_freq)
        pg.time.set_timer(ADD_PILL, POWERUP_COOLDOWN)

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
    images['laser'] = load_image('images/laser.png', LASER_SCALE)
    images['pill'] = load_image('images/pill.png', PILL_SCALE)
    images['ship'] = load_image('images/ship.png', SHIP_SCALE)
    images['meteor'] = load_image('images/meteor.png', METEOR_SCALE)
    images['heart'] = load_image('images/heart.png', HEART_SCALE)
    images['backgroung'] = load_image('images/background.png', BACKGROUND_SCALE)
    return images

def load_sounds():
    sounds = {}
    sounds['explosion'] = pg.mixer.Sound('sounds/explosion.wav')
    sounds['laser'] = pg.mixer.Sound('sounds/laser.wav')
    sounds['pill'] = pg.mixer.Sound('sounds/pill.wav')
    return sounds


game = Game()
images = load_images()
sounds = load_sounds()
