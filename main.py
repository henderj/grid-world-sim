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

class Game:
    def load_sprites(self):
        sheet = SpriteSheet("images/1bitpack_kenney_1.2/Tilesheet/colored.png").load_grid_images(22, 49, x_padding=1, y_padding=1)
        bgs = [sheet[0], sheet[1], sheet[2], sheet[5], sheet[6], sheet[7]]
        
        all_sprites: Group = Group()
        
        for x in range(WIDTH):
            for y in range(HEIGHT):
                Tile(choice(bgs), (x,y), all_sprites)

    def run(self):
        py.init()
        running = True
        screen = py.display.set_mode((WIDTH, HEIGHT))

        self.load_sprites()
        
        while running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                    break
                else:
                    print(event)
            
            screen.fill((120,120,120))
            all_sprites.draw(screen)
            py.display.flip()
        
        py.quit()

def main():
    py.init()
    running = True
    screen = py.display.set_mode((WIDTH, HEIGHT))

    sheet = SpriteSheet("images/1bitpack_kenney_1.2/Tilesheet/colored.png").load_grid_images(22, 49, x_padding=1, y_padding=1)
    bgs = [sheet[0], sheet[1], sheet[2], sheet[5], sheet[6], sheet[7]]
    
    all_sprites: Group = Group()
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            Tile(choice(bgs), (x,y), all_sprites)
    
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
                break
            else:
                print(event)
        
        screen.fill((120,120,120))
        all_sprites.draw(screen)
        py.display.flip()
    
    py.quit()
            

if __name__ == "__main__":
    main()