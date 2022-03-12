from sprites import *

paddle1, paddle2 = Paddle(images['red paddle'], 'right'), Paddle(images['green paddle'], 'left')
ball = Ball(images['ball'])

while game.running:
    game.clock.tick(FPS)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            game.running = False

    pressed_keys = pg.key.get_pressed()
    if pressed_keys[pg.K_UP]:
        paddle1.move('up')
    if pressed_keys[pg.K_DOWN]:
        paddle1.move('down')
    if pressed_keys[pg.K_w]:
        paddle2.move('up')
    if pressed_keys[pg.K_s]:
        paddle2.move('down')
    if pressed_keys[pg.K_ESCAPE]:
        game.state = 'pause'
        pg.mixer.music.pause()
    if pressed_keys[pg.K_SPACE]:
        game.state = 'play'
        pg.mixer.music.unpause()

    ball.update()
    paddle1.update()
    paddle2.update()

    if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
        sounds['paddle hit'].play()
        ball.dir[0] *= -1
        ball.dir[1] = choice([-1, 1]) * uniform(0.5, 1)

    game.screen.blit(images['background'], images['background'].get_rect())
    game.write_text(str(game.score[0]), (WIDTH / 4 , HEIGHT / 5), 70, (0, 0, 0))
    game.write_text(str(game.score[1]), (WIDTH * 3 / 4 , HEIGHT / 5), 70, (0, 0, 0))
    if game.state == 'pause':
        game.write_text('PAUSE', (WIDTH / 4 , HEIGHT / 3), 200, (150, 150, 150))
    elif game.state == 'serve':
        game.write_text('PRESS SPACE TO SERVE', (WIDTH / 4 , HEIGHT / 3), 50, (150, 150, 150))
        game.write_text('ARROWS AND W,S TO MOVE', (WIDTH / 4 , HEIGHT / 2), 50, (150, 150, 150))

    ball.draw()
    paddle1.draw()
    paddle2.draw()
    pg.display.flip()

pg.mixer.quit()
pg.quit()
