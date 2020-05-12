import pygame as pg
from gametypes import Rect, Position

from constants import TILE_SIZE, TILE_MAP, INTERACT_MAP, COLLIDEABLE, CONTROLS, DIRECTION, ACTION
from entity import Entity, Player

class World():

    _grid = []
    _entities = []
    _player = None

    def __init__(self, fileName: str):
        with open(fileName, 'r') as f:
            for l in f:
                self._grid.append(l[:-1])
        self.size = (len(self._grid[0]), len(self._grid))

    # def draw(self, surface: pg.Surface):
    #     for i, l in enumerate(self._grid):
    #         for j, c in enumerate(l):
    #             ct = TILE_MAP[c]
    #             surface.fill(ct, rect=pg.Rect(j*TILE_SIZE[0], i*TILE_SIZE[1], TILE_SIZE[0], TILE_SIZE[1]))

    #     self._player.draw(surface)

    def draw(self, surface: pg.Surface, view: Rect):
        # print(view)
        for i in range(view[1], view[3]):
            for j in range(view[0], view[2]):
                c = self._grid[i][j]
                ct = TILE_MAP[c]
                surface.fill(ct, rect=pg.Rect((j-view[0])*TILE_SIZE[0], (i-view[1])*TILE_SIZE[1], TILE_SIZE[0], TILE_SIZE[1]))

                # if self._player.pos == (j, i):
                self._player.draw(surface, (view[:2]))

    def oob(self, pos: Position):
        return pos[0] < 0 or pos[0] >= self.size[0] or pos[1] < 0 or pos[1] >= self.size[1]

    def collision(self, pos: Position):
        return self.oob(pos) or self._grid[pos[0]][pos[1]] in COLLIDEABLE

    def addEntitiy(self, e: Entity):
        if (isinstance(e, Player)):
            self._player = e
        elif (isinstance(e, Entity)):
            self._entities.append(e)

    def updateEvents(self, event):
        if event.key in CONTROLS:
            c = CONTROLS[event.key]
            if isinstance(c, DIRECTION):
                self._player.move(CONTROLS[event.key], self.collision)
                # print(self._player.pos)
            if isinstance(c, ACTION):
                if c == ACTION.INTERACT:
                    v = self._player.facing.value
                    ipos = self._player.pos[0]+v[0], self._player.pos[1]+v[1]
                    if not self.oob(ipos):
                        item = self._grid[ipos[0]][ipos[1]]
                        print(INTERACT_MAP[item])

        for e in self._entities:
            e.update()

    # def updateKeys(self, keys):
    #     if 1 in keys: print(keys)
    #     for k in CONTROLS:
    #         # if keys[k]: print(keys[k])
    #         if keys[k]:
    #             c = CONTROLS[k]
    #             if isinstance(c, ACTION):
    #                 if c == ACTION.INTERACT:
    #                     v = self._player.facing.value
    #                     ipos = self._player.pos[0]+v[0], self._player.pos[1]+v[1]
    #                     if not self.oob(ipos):
    #                         item = self._grid[ipos[0]][ipos[1]]
    #                         print(INTERACT_MAP[item])
    #             if isinstance(c, DIRECTION):
    #                 self._player.move(c, self.collision)
    #                 print(self._player.pos)