from random import choice
from typing import Tuple
import pygame as py
from pygame.sprite import Group, Sprite, AbstractGroup
from spritesheet import SpriteSheet
import os

WIDTH, HEIGHT = (640, 480)
TILESIZE = 16

class Tile(Sprite):
    def __init__(self, image: py.Surface, pos: Tuple[int], *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=(pos[0] * TILESIZE, pos[1] * TILESIZE))

class World:
    def __init__(self, size: Tuple[int]) -> None:
        self.size = size
        self.map_tiles = []
    
    def build(self):
        bgs = [0, 1, 5]
        for x in range(self.size[0]):
            col = []
            for y in range(self.size[1]):
                col.append(choice(bgs))
            self.map_tiles.append(col)
    
    def render(self, screen: py.Surface, sheet: list[py.Surface], topright = (0,0)):
        width, height = (screen.get_width(), screen.get_height())
        subset = [[col[y] for y in col[topright[1]:topright[1]+height]] for col in self.map_tiles[topright[0]:topright[0]+width]]
        for x in range(width):
            for y in range(height):
                tile = sheet[subset[x][y]]
                worldpos = (x*TILESIZE, y*TILESIZE)
                rect = py.Rect(worldpos[0],worldpos[1],TILESIZE,TILESIZE)
                screen.blit(tile, rect)

class Game:
    def load_sprites(self):
        self.sheet = SpriteSheet("images/1bitpack_kenney_1.2/Tilesheet/colored.png").load_grid_images(22, 49, x_padding=1, y_padding=1)

    def game_loop(self):
        campos_x, campos_y = (0,0)
        while self.running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    return
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_RIGHT:
                        campos_x += 1
                    elif event.key == py.K_LEFT:
                        campos_x -= 1
                    elif event.key == py.K_UP:
                        campos_y -= 1
                    elif event.key == py.K_DOWN:
                        campos_y += 1
                else:
                    print(event)
            
            campos_x, campos_y = (min(campos_x, WIDTH), min(campos_y, HEIGHT))
            campos_x, campos_y = (max(campos_x, 0), max(campos_y, 0))
            self.screen.fill((120,120,120))
            self.world.render(self.screen, self.sheet, (campos_x, campos_y))
            py.display.flip()

    def run(self):
        py.init()
        self.running = True
        self.screen = py.display.set_mode((WIDTH, HEIGHT))

        self.load_sprites()
        self.world = World((1000,1000))
        self.world.build()
        self.game_loop()
        py.quit()

def main():
    game = Game()
    game.run()        

if __name__ == "__main__":
    main()