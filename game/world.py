from enum import Enum
from typing import Tuple
from pygame import Surface, Rect, Vector2

from game.camera import Camera
from game.entities.entity import Entity
from game.entities.chicken import Chicken
from game.metrics import TILESIZE
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

        self.entities: list[Entity] = []
        self.entities.append(Chicken(Vector2(0,0)))
        self.entities.append(Chicken(Vector2(5,0)))
        self.entities.append(Chicken(Vector2(-4,3)))

    def load_surfaces(self, sheet: list[Surface]):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                surfacepos = (x*TILESIZE, y*TILESIZE)
                rect = Rect(surfacepos[0],surfacepos[1],TILESIZE,TILESIZE)
                self.map_surface.blit(sheet[self.tiles[x][y]], rect)
        for e in self.entities:
            e.load_surface(sheet)
            
    def tick(self, dt: int):
        for e in self.entities:
            e.tick(dt)

    def render(self, screen: Surface, cam: Camera):
        surface_topleft_of_cam = ((cam.viewport.left + self.size[0] / 2) * TILESIZE, (cam.viewport.top + self.size[1] / 2) * TILESIZE)
        topleft = (-surface_topleft_of_cam[0], -surface_topleft_of_cam[1])
        world_surface = Surface(screen.get_size())
        world_surface.blit(self.map_surface, topleft)
        
        entities_to_draw = [e for e in self.entities if cam.viewport.colliderect(e.get_rect())]
        entity_surface = Surface(screen.get_size())
        for e in entities_to_draw:
            offset = (e.pos - Vector2(cam.viewport.center)) * TILESIZE
            topleft_offset = Vector2(entity_surface.get_rect().center) + offset
            world_surface.blit(e.surface, topleft_offset)
        screen.blit(world_surface, (0,0))
