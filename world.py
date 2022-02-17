from enum import Enum
from typing import Tuple
from pygame import Surface, Rect
from camera import Camera
from metrics import TILESIZE
from random import choice
import numpy as np

class TileTypes(Enum):
    DIRT = 0
    DIRT_COURSE = 1
    GRASS = 5

class World:
    def __init__(self, size: Tuple[int, int]) -> None:
        self.size = size
        self.map_surface = Surface((size[0]*TILESIZE,size[1]*TILESIZE))
    
    def build(self):
        self.tiles = np.zeros(self.size, np.int16)
        ground_types = [TileTypes.DIRT, TileTypes.DIRT_COURSE, TileTypes.GRASS]
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                tile = choice(ground_types)
                self.tiles[x][y] = tile.value

    def load_surface(self, sheet: list[Surface]):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                surfacepos = (x*TILESIZE, y*TILESIZE)
                rect = Rect(surfacepos[0],surfacepos[1],TILESIZE,TILESIZE)
                self.map_surface.blit(sheet[self.tiles[x][y]], rect)
            
    def render(self, screen: Surface, cam: Camera):
        surface_topleft_of_cam = ((cam.viewport.left + self.size[0] / 2) * TILESIZE, (cam.viewport.top + self.size[1] / 2) * TILESIZE)
        topleft = (-surface_topleft_of_cam[0], -surface_topleft_of_cam[1])
        screen.blit(self.map_surface, topleft)
