from sprites import *


ship = Ship(images['ship'])

while game.running:
    game.clock.tick(FPS)
    if ship.hearts <= 0:
        game.state = 'game over'

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            game.running = False
        if event.type == ADD_METEOR:
            game.meteors.add(Meteor(images['meteor'], game.meteors_speed))
        if event.type == ADD_PILL:
            game.pills.add(Pill(images['pill']))
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                if game.state == 'pause':
                    game.state = 'play'
                    pg.mixer.music.unpause()
                else:
                    game.state = 'pause'
                    pg.mixer.music.pause()

    pressed_keys = pg.key.get_pressed()
    if game.state == 'play':
        if pressed_keys[pg.K_UP]:
            ship.move('up')
        if pressed_keys[pg.K_DOWN]:
            ship.move('down')
        if pressed_keys[pg.K_LEFT]:
            ship.move('left')
        if pressed_keys[pg.K_RIGHT]:
            ship.move('right')
        if pressed_keys[pg.K_SPACE]:
            ship.shoot()

    meteors_lasers_collision = pg.sprite.groupcollide(game.meteors, game.lasers, True, True)
    if len(meteors_lasers_collision) > 0:
        game.score += len(meteors_lasers_collision)
        sounds['explosion'].play()
        if game.score % 5 == 0:
            game.meteors_freq /= 1.1
            pg.time.set_timer(ADD_METEOR, int(game.meteors_freq))

    ship_meteor_collision = pg.sprite.spritecollide(ship, game.meteors, True)
    if len(ship_meteor_collision) > 0:
        ship.hearts -= 1
        sounds['explosion'].play()

    ship_pill_collision = pg.sprite.spritecollide(ship, game.pills, True)
    if len(ship_pill_collision) > 0:
        ship.hearts += 1
        sounds['pill'].play()

    ship.update()
    for laser in game.lasers:
        laser.update()
    for meteor in game.meteors:
        meteor.update()
    for pill in game.pills:
        pill.update()

    game.screen.blit(images['backgroung'], images['backgroung'].get_rect())
    game.write_text(str(game.score), (WIDTH / 10, HEIGHT / 10), 100, (255, 0, 0))
    if game.state == 'game over':
        game.write_text('GAME OVER', (WIDTH / 4, HEIGHT / 4), 100, (150, 150, 150))
    if game.state == 'pause':
        game.write_text('PAUSE', (WIDTH / 4, HEIGHT / 4), 100, (150, 150, 150))

    ship.draw()
    for laser in game.lasers:
        laser.draw()
    for meteor in game.meteors:
        meteor.draw()
    for pill in game.pills:
        pill.draw()

    pg.display.flip()

pg.mixer.quit()
pg.quit()
