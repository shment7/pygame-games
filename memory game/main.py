from sprites import *


board = create_board()

while game.running:
    game.clock.tick(FPS)
    if game.score == ROWS * COLS // 2:
        pg.mixer.music.play(loops=-1)

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            game.running = False

        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            r, c = int(ROWS * pos[1] / HEIGHT), int(COLS * pos[0] / WIDTH)
            if not board[r][c].is_flipped:
                if game.first_flip is None and game.second_flip is None:
                    board[r][c].flip()
                    board[r][c].is_flipped = True
                    game.first_flip = board[r][c]
                elif game.first_flip is not None and game.second_flip is None:
                    game.guess += 1
                    board[r][c].flip()
                    board[r][c].is_flipped = True
                    game.second_flip = board[r][c]
                    if game.first_flip.image_num == game.second_flip.image_num:
                        game.first_flip.is_paired = True
                        game.second_flip.is_paired = True
                        game.first_flip = None
                        game.second_flip = None
                        sounds['pair'].play()
                        game.score += 1
                    else:
                        sounds['fail'].play()

                elif game.first_flip is not None and game.second_flip is not None:
                    game.first_flip.flip()
                    game.second_flip.flip()
                    game.second_flip = None
                    board[r][c].flip()
                    board[r][c].is_flipped = True
                    game.first_flip = board[r][c]

    game.screen.fill((0, 0, 0))
    game.write_text(str(game.guess), ((WIDTH - 50) // 2, HEIGHT), 30, (255, 255, 255))
    for c in range(COLS):
        for r in range(ROWS):
            board[r][c].draw()

    pg.display.flip()

pg.mixer.quit()
pg.quit()
