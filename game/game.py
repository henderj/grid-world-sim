from game.spritesheet import SpriteSheet
import pygame as py

import game.metrics as metrics
import game.world as world
import game.camera as camera

class Game:
    def load_sprites(self):
        self.tilesheet = SpriteSheet("images/1bitpack_kenney_1.2/Tilesheet/colored.png").load_grid_images(22, 49, x_padding=1, y_padding=1)
        # color key = #472d3c

    def game_loop(self):
        while self.running:
            dt = self.clock.tick()
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    return
                else:
                    self.cam.process_event(event)
                    print(event)
            self.screen.fill((120,120,120))
            self.world.tick(dt)
            self.world.render(self.screen, self.cam)
            py.display.flip()
    def run(self):
        py.init()
        self.running = True
        self.screen = py.display.set_mode((metrics.WIDTH, metrics.HEIGHT))
        py.key.set_repeat(500, 100)

        self.load_sprites()
        self.cam = camera.Camera(py.Rect(0,0, metrics.WIDTH / metrics.TILESIZE, metrics.HEIGHT / metrics.TILESIZE))
        self.world = world.World((100,100))
        self.world.build()
        self.world.load_surfaces(self.tilesheet)

        self.clock = py.time.Clock()
        self.game_loop()
        py.quit()

if __name__ == "__main__":
    game = Game()
    game.run()