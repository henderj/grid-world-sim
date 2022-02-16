from typing import Tuple
from pygame import Surface, Rect
from metrics import TILESIZE
from random import choice

class World:
    def __init__(self, size: Tuple[int]) -> None:
        self.size = size
        self.map_surface = Surface((size[0]*TILESIZE,size[1]*TILESIZE))
    
    def build(self, sheet: list[Surface]):
        bgs = [0, 1, 5]
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                tile = choice(bgs)
                worldpos = (x*TILESIZE, y*TILESIZE)
                rect = Rect(worldpos[0],worldpos[1],TILESIZE,TILESIZE)
                self.map_surface.blit(sheet[tile], rect)
        
    
    def render(self, screen: Surface, sheet: list[Surface], topright = (0,0)):
        screen.blit(self.map_surface, (-topright[0], -topright[1]))
