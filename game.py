import sys
import pygame as pg
from world import World
from entity import Player
from camera import Camera
from constants import WINDOW_SIZE, DIRECTION, CONTROLS, KEYPRESS_DELAY, KEYPRESS_INTERVAL


def init_game():
    w = World('assets/level.lvl')
    w.addEntitiy(Player(pos=[3,3], image='assets/pika.png'))
    c = Camera(w)
    return w, c

def init():
    pg.init()
    pg.key.set_repeat(KEYPRESS_DELAY, KEYPRESS_INTERVAL)
    screen = pg.display.set_mode(WINDOW_SIZE)
    w, c = init_game()

    def update():
        for e in pg.event.get():
            if e.type == pg.QUIT: sys.exit()
            if e.type == pg.KEYDOWN:
                w.updateEvents(e)
        # if pg.key.get_focused():
        #     w.updateKeys(pg.key.get_pressed())

    def draw():
        c.draw(screen)
        pg.display.flip()

    return update, draw

if __name__ == '__main__':
    update, draw = init()
    while 1:
        update()
        draw()

