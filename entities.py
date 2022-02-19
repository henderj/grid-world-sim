from abc import ABC, abstractmethod
from enum import Enum

from pygame import Color, Rect, Surface, Vector2

from metrics import TILESIZE


class EntityTypes(Enum):
    CHICKEN = 369

class Entity(ABC):
    
    COLOR_KEY = Color(71,45,60)

    def __init__(self, pos: Vector2) -> None:
        self.pos: Vector2 = pos
        self.surface: Surface = None

    @abstractmethod
    def tick(self, dt: int) -> None:
        pass

    @abstractmethod
    def load_surface(self, sheet: list[Surface]) -> None:
        pass

    def get_rect(self) -> Rect:
        return Rect(self.pos, (TILESIZE, TILESIZE))

class Chicken(Entity):

    def __init__(self, pos: Vector2) -> None:
        super().__init__(pos)
        self.move_delay = 1000
        self.until_next_move = 1000
    
    def tick(self, dt: int):
        self.until_next_move -= dt
        if self.until_next_move <= 0:
            self.pos += Vector2(1,0)
            self.until_next_move = self.move_delay

    def load_surface(self, sheet: list[Surface]) -> None:
        self.surface = sheet[EntityTypes.CHICKEN.value].copy()
        self.surface.set_colorkey(Entity.COLOR_KEY)

