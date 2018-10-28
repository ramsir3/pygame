import pygame as pg
from constants import WORLD_SIZE, TILE_MAP, COLLIDEABLE

class world(object):
    
    _grid = []

    def __init__(self, fileName: str):
        with open(fileName, 'r') as f:
            for l in f:
                self._grid.append(l[:-1])
        self.size = (len(self._grid[0]), len(self._grid))

    def draw(self, surface: pg.Surface):
        for i, l in enumerate(self._grid):
            for j, c in enumerate(l):
                ct = TILE_MAP[c]
                surface.fill(ct, rect=pg.Rect(j*WORLD_SIZE[0], i*WORLD_SIZE[1], WORLD_SIZE[0], WORLD_SIZE[1]))
            
    def collision(self, pos):
        oob = pos[0] < 0 or pos[0] >= self.size[0] or pos[1] < 0 or pos[1] >= self.size[1]
        return oob or self._grid[pos[0]][pos[1]] in COLLIDEABLE