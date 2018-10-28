from enum import Enum
import pygame as pg

WORLD_SIZE = (60,60)
WINDOW_SIZE = (600,600)

DIRECTION = Enum('DIRECTIONS', 'up down left right')

CONTROLS = {
    pg.K_w: DIRECTION.up,
    pg.K_s: DIRECTION.down,
    pg.K_a: DIRECTION.left,
    pg.K_d: DIRECTION.right
}

TILE_MAP = {
    'g': (157, 246, 43, 255),
    '_': (234, 186, 41, 255),
    'T': (3, 201, 3, 255),
    'r': (201, 199, 192, 255),
}

COLLIDEABLE = ['T', 'r']