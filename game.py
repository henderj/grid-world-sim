from spritesheet import SpriteSheet
import pygame as py

from metrics import HEIGHT, TILESIZE, WIDTH
from world import World


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
                        campos_x += TILESIZE
                    elif event.key == py.K_LEFT:
                        campos_x -= TILESIZE
                    elif event.key == py.K_UP:
                        campos_y -= TILESIZE
                    elif event.key == py.K_DOWN:
                        campos_y += TILESIZE
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
        self.world.build(self.sheet)
        self.game_loop()
        py.quit()
