from abc import ABC, abstractmethod
from enum import Enum

from pygame import Color, Rect, Surface, Vector2

from metrics import TILESIZE


class EntityTypes(Enum):
    CHICKEN = 369

class Entity(ABC):
    BASE_MOVE_DELAY = 300
    COLOR_KEY = Color(71,45,60)

    def __init__(self, pos: Vector2) -> None:
        self.pos: Vector2 = pos
        self.surface: Surface = None

    @property
    @abstractmethod
    def speed(self) -> float:
        pass

    @abstractmethod
    def tick(self, dt: int) -> None:
        pass

    @abstractmethod
    def load_surface(self, sheet: list[Surface]) -> None:
        pass

    def get_rect(self) -> Rect:
        return Rect(self.pos, (TILESIZE, TILESIZE))
