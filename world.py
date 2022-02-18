from abc import ABC, abstractmethod
from enum import Enum
from typing import Tuple
from pygame import Surface, Rect, Vector2
from camera import Camera
from metrics import TILESIZE
from random import choice
import numpy as np

class EntityTypes(Enum):
    CHICKEN = 369

class TileTypes(Enum):
    DIRT = 0
    DIRT_COURSE = 1
    GRASS = 5

class Entity(ABC):
    
    def __init__(self, pos: Vector2) -> None:
        self.pos = pos

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def load_surface(self, entitysheet: list[Surface]):
        pass

    @abstractmethod
    def render(self, screen: Surface, cam: Camera):
        pass

class Chicken(Entity):

    def __init__(self, pos: Vector2) -> None:
        super().__init__(pos)
    
    def tick(self):
        return super().tick()

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

        self.entities: list[Entity] = []
        self.entities.append(Chicken((0,0)))

    def load_surfaces(self, tilesheet: list[Surface], entitysheet: list[Surface]):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                surfacepos = (x*TILESIZE, y*TILESIZE)
                rect = Rect(surfacepos[0],surfacepos[1],TILESIZE,TILESIZE)
                self.map_surface.blit(tilesheet[self.tiles[x][y]], rect)
        for e in self.entities:
            e.load_surface(entitysheet)
            
    def tick(self):
        for e in self.entities:
            e.tick()

    def render(self, screen: Surface, cam: Camera):
        surface_topleft_of_cam = ((cam.viewport.left + self.size[0] / 2) * TILESIZE, (cam.viewport.top + self.size[1] / 2) * TILESIZE)
        topleft = (-surface_topleft_of_cam[0], -surface_topleft_of_cam[1])
        screen.blit(self.map_surface, topleft)
        for e in self.entities:
            e.render(screen, cam)
