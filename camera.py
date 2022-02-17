
from pygame import Rect, Vector2


class Camera:
    def __init__(self, size: Rect, pos: Vector2=(0,0)) -> None:
        self.viewport = size.copy()
        self.viewport.center = pos
    
    def move(self, x: float, y: float):
        self.viewport = self.viewport.move(x, y)