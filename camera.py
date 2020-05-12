import pygame as pg

from world import World
from constants import TILE_SIZE, WINDOW_SIZE, TILE_MAP
from gametypes import Position

class Camera():

    def __init__(self, world: World):
        self.world = world
        self.VIEW_SIZE = WINDOW_SIZE[0] // TILE_SIZE[0], WINDOW_SIZE[1] // TILE_SIZE[1]

    def draw(self, surface: pg.Surface):
        s = self.world.size
        p = self.world._player.pos
        v = self.VIEW_SIZE

        toplefty = max(0, p[0]-v[0]//2)
        topleftx = max(0, p[1]-v[1]//2)
        view = (
            topleftx,
            toplefty,
            min(s[0], topleftx+v[0]),
            min(s[1], toplefty+v[1])
        )
        self.world.draw(surface, view)


class View():

    def __init__(self, size: Position, bounds: Position):
        self.bounds = bounds
        self.size = size
        self.x1 = 0
        self.y1 = 0
        self.x2 = min(size[0], bounds[0])
        self.y2 = min(size[1], bounds[1])


    def getView(self, player_pos: Position):
        x = player_pos[1]
        y = player_pos[0]

        nx1 = self.x1 + x if self.x1 + x < self.bounds[0] else self.bounds[0]
        ny1 = self.y1 + y if self.y1 + y < self.bounds[1] else self.bounds[1]
        nx2 = self.x2 + x if self.x1 + x < self.bounds[0] else self.bounds[0]
        ny2 = self.y2 + y if self.x1 + x < self.bounds[0] else self.bounds[0]
        out = (

        )

        return self.view