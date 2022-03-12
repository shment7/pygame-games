from random import uniform, randint, choice
from math import sqrt
from utils import *


class Paddle(pg.sprite.Sprite):
    def __init__(self, image, side):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        if side == 'right':
            self.rect.right = WIDTH
        else:
            self.rect.left = 0

    def draw(self):
        game.screen.blit(self.image, self.rect)

    def update(self):
        pass

    def move(self, dir):
        if game.state == 'play' or game.state == 'serve':
            if dir == 'up' and self.rect.top > 0:
                self.rect.top -= PADDLE_SPEED
            elif dir == 'down' and self.rect.bottom < HEIGHT:
                self.rect.top += PADDLE_SPEED


class Ball(pg.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.dir = [choice([-1, 1]) * uniform(0.5, 1), choice([-1, 1]) * uniform(0.5, 1)]
        norm = sqrt(self.dir[0] ** 2 + self.dir[1] ** 2)
        self.dir[0] /= norm
        self.dir[1] /= norm

    def draw(self):
        game.screen.blit(self.image, self.rect)

    def update(self):
        if game.state == 'play':
            self.rect.move_ip(self.dir[0] * BALL_SPEED, self.dir[1] * BALL_SPEED)
            if self.rect.top < 0 or self.rect.bottom > HEIGHT:
                sounds['wall hit'].play()
                self.dir[1] *= -1
            elif self.rect.left > WIDTH:
                sounds['goal'].play()
                game.score[0] += 1
                game.state = 'serve'
            elif self.rect.right < 0:
                sounds['goal'].play()
                game.score[1] += 1
                game.state = 'serve'
        elif game.state == 'serve':
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
