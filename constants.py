from enum import Enum
import pygame as pg

WORLD_SIZE = (60,60)
WINDOW_SIZE = (600,600)

class DIRECTION(Enum):
    UP=(-1,0)
    RIGHT=(0,1)
    DOWN=(1,0)
    LEFT=(0,-1)
    NULL=(0,0)

class ACTION(Enum):
    INTERACT=0

CONTROLS = {
    pg.K_w: DIRECTION.UP,
    pg.K_s: DIRECTION.DOWN,
    pg.K_a: DIRECTION.LEFT,
    pg.K_d: DIRECTION.RIGHT,
    pg.K_i: ACTION.INTERACT
}

TILE_MAP = {
    'g': (157, 246, 43, 255),
    '_': (234, 186, 41, 255),
    'T': (3, 201, 3, 255),
    'r': (201, 199, 192, 255),
}

COLLIDEABLE = ['T', 'r']

INTERACT_MAP = {
    'g': 'It\'s grass',
    '_': 'It\'s a path',
    'T': 'It\'s a tree',
    'r': 'It\'s a rock',
}