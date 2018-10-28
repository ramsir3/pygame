import pygame as pg
from constants import WORLD_SIZE, DIRECTION

class entity(object):

    def __init__(self, pos=[0,0], image=(255,0,0,255), size=WORLD_SIZE, world=None):
        self.pos = pos
        self.image = image
        self.size = size
        self.world = world

    def draw(self, surface: pg.Surface):
        surface.fill(self.image, rect=pg.Rect(self.pos[1]*self.size[0], self.pos[0]*self.size[1], self.size[0], self.size[1]))

    def move(self, vec):
        newpos = self.pos[:]
        newpos[0] += vec[0]
        newpos[1] += vec[1]
        if self.world:
            if not self.world.collision(newpos):
                self.pos = newpos
        else:
            self.pos = newpos

class player(entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 1

    def move(self, d: DIRECTION):
        if d == DIRECTION.up:
            super().move([-self.speed, 0])
        elif d == DIRECTION.down:
            super().move([self.speed, 0])
        elif d == DIRECTION.left:
            super().move([0, -self.speed])
        elif d == DIRECTION.right:
            super().move([0, self.speed])