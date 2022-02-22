from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Callable

from pygame import Color, Rect, Surface, Vector2

from game.metrics import TILESIZE

class Direction(Enum):
    N = Vector2(0,1)
    NE = Vector2(1,1)
    E = Vector2(1,0)
    SE = Vector2(1,-1)
    S = Vector2(0,-1)
    SW = Vector2(-1,-1)
    W = Vector2(-1, 0)
    NW = Vector2(-1, 1)

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
        if self.is_moving:
            self.move_timer -= dt
            if self.move_timer <= 0:
                self.pos += self.move_direction.value
                if self.move_callback: self.move_callback()
                self.is_moving = False
        pass

    @abstractmethod
    def load_surface(self, sheet: list[Surface]) -> None:
        pass

    def get_rect(self) -> Rect:
        return Rect(self.pos, (TILESIZE, TILESIZE))
    
    def move(self, dir: Direction, callback: Callable[..., Any]=None):
        self.is_moving = True
        self.move_direction = dir
        self.move_callback = callback
        self.move_timer = self.BASE_MOVE_DELAY * (1/self.speed)
