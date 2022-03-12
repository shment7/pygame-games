from sprites import *


bird = Bird( )
w = images['background'].get_rect().width
rect1 = pg.Rect(0, 0, w, HEIGHT)
rect2 = pg.Rect(w, 0, w, HEIGHT)

while game.running:
    game.clock.tick(FPS)

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            game.running = False
        if event.type == ADD_PIPE:
            game.pipes.add(Pipe())
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                if game.state == 'pause':
                    game.state = 'play'
                    pg.mixer.music.unpause()
                else:
                    game.state = 'pause'
                    pg.mixer.music.pause()
            if game.state != 'play' and event.key == pg.K_RETURN:
                if game.state == 'game over':
                    game.score = 0

                game.state = 'play'

    pressed_keys = pg.key.get_pressed()
    if game.state == 'play':
        if pressed_keys[pg.K_SPACE]:
            bird.jump()

    if game.state == 'play':
        if bird.rect.top < 0 or bird.rect.bottom > HEIGHT:
            game.state = 'game over'
            sounds['explosion'].play()
            bird.rect.midleft = (100, HEIGHT / 2)
            bird.speed = 0
            game.scroll_speed = 5
            game.pipes = pg.sprite.Group()

        bird_pipe_collision = pg.sprite.spritecollide(bird, game.pipes, True)
        if len(bird_pipe_collision) > 0:
            game.state = 'game over'
            sounds['explosion'].play()
            bird.rect.midleft = (100, HEIGHT / 2)
            bird.speed = 0
            game.scroll_speed = 5
            game.pipes = pg.sprite.Group()

        bird.update()
        for pipe in game.pipes:
            pipe.update()

    if rect1.right < 0:
        rect1.left = WIDTH
    if rect2.right < 0:
        rect2.left = WIDTH

    rect1.x -= game.scroll_speed
    rect2.x -= game.scroll_speed
    game.screen.blit(images['background'], rect1)
    game.screen.blit(images['background'], rect2)
    game.write_text(str(game.score), (WIDTH / 10, HEIGHT / 10), 100, (255, 0, 0))
    if game.state == 'start':
        game.write_text('PRESS ENTER TO START', (WIDTH / 4, HEIGHT / 4), 50, (50, 50, 50))
        game.write_text('SPACE TO JUMP', (WIDTH / 3, HEIGHT / 2), 50, (50, 50, 50))
    if game.state == 'pause':
        game.write_text('PAUSE', (WIDTH / 4, HEIGHT / 4), 100, (150, 150, 150))
    if game.state == 'game over':
        game.write_text('GAME OVER - PRESS ENTER TO START', (WIDTH / 4, HEIGHT / 4), 40, (50, 50, 50))
        game.write_text('SPACE TO JUMP', (WIDTH / 3, HEIGHT / 2), 50, (50, 50, 50))

    bird.draw()
    for pipe in game.pipes:
        pipe.draw()

    pg.display.flip()

pg.mixer.quit()
pg.quit()
