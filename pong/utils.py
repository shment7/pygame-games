from settings import *
import pygame as pg


class Game:
    def __init__(self):
        super().__init__()
        pg.init()
        pg.display.set_caption(TITLE)
        pg.mixer.init()
        pg.mixer.music.load('sounds/music.wav')
        pg.mixer.music.set_volume(MUSIC_VOLUME)
        pg.mixer.music.play(loops=-1)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.running = True
        self.score = [0, 0]
        self.state = 'serve' # 'serve', 'pause', 'play'

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
    images['ball'] = load_image('images/ball.png', BALL_SCALE)
    images['green paddle'] = load_image('images/green paddle.png', PADDLE_SCALE)
    images['red paddle'] = load_image('images/red paddle.png', PADDLE_SCALE)
    images['background'] = load_image('images/background.png', BACKGROUNG_SCALE)
    return images

def load_sounds():
    sounds = {}
    sounds['goal'] = pg.mixer.Sound('sounds/goal.wav')
    sounds['paddle hit'] = pg.mixer.Sound('sounds/paddle hit.wav')
    sounds['wall hit'] = pg.mixer.Sound('sounds/wall hit.wav')
    return sounds

game = Game()
images = load_images()
sounds = load_sounds()
