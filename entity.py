import pygame as pg
from constants import TILE_SIZE, DIRECTION
from gametypes import Position
class Entity():

    def __init__(self, pos: Position=(0,0), image=(255,0,0,255), size=TILE_SIZE):
        self.pos = pos
        if type(image) == tuple:
            self.image = image
        elif type(image) == str:
            self.image = pg.transform.scale(pg.image.load(image), size)
        self.size = size
        self.facing = DIRECTION.DOWN

    def draw(self, surface: pg.Surface, offset: Position=(0,0)):
        x, y = self.pos[1] - offset[0], self.pos[0] - offset[1]
        if type(self.image) == tuple:
            surface.fill(self.image, rect=pg.Rect(x*self.size[0], y*self.size[1], self.size[0], self.size[1]))
        elif type(self.image) == pg.Surface:
            surface.blit(self.image, pg.Rect(x*self.size[0], y*self.size[1], self.size[0], self.size[1]))

    def move(self, vec, collisionFunc=lambda: False):
        newpos = self.pos[:]
        newpos[0] += vec[0]
        newpos[1] += vec[1]

        if not collisionFunc(newpos):
            self.pos = newpos

class Player(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 1

    def move(self, d: DIRECTION, collisionFunc=lambda: False):
        if d != self.facing:
            angle =  (d.value[1] * self.facing.value[0]) - (d.value[0] * self.facing.value[1])
            angle = (angle * -90) + 180
            # print(angle)
            self.image = pg.transform.rotate(self.image, angle)
            self.facing = d
        else:
            v = []
            if d == DIRECTION.UP:
                v = [-self.speed, 0]
            elif d == DIRECTION.DOWN:
                v = [self.speed, 0]
            elif d == DIRECTION.LEFT:
                v = [0, -self.speed]
            elif d == DIRECTION.RIGHT:
                v = [0, self.speed]
            super().move(v, collisionFunc)
