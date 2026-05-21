import pygame as pg
from constants import *
from board import Board
from pacman import PacMan
from spokelse import Spokelse

pg.init()
board = Board()
vindu = pg.display.set_mode(board.window_size())
clock = pg.time.Clock()
framecounter = 0


pacman = PacMan(3, 4)
spokelse = Spokelse(3, 5)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    # Tegn bakgrunn: (En slags "reset" av hele vinduet vårt)
    vindu.fill(BLACK)

    # Tegn brettet først, og pacman og andre ting "oppå":
    board.draw(vindu)

    # TODO: Oppdater objektene våre:
    dt = clock.tick(60)  # returnerer millisekunder siden forrige tick

    spokelse.update(dt)

    # Tegn objektene våre:
    pacman.draw(vindu)
    spokelse.draw(vindu)


    # Har alltid disse med til slutt:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame på en "ryddig måte":
pg.quit()
