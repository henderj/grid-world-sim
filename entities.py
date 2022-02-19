from abc import ABC, abstractmethod, abstractproperty
from enum import Enum
from random import randint
from turtle import Vec2D
from typing import Any, Callable, Dict

from pygame import Color, Rect, Surface, Vector2

from metrics import TILESIZE
from statemachine import GoToRandomTarget, StateMachine


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


class Chicken(Entity):

    def __init__(self, pos: Vector2) -> None:
        super().__init__(pos)
        self.statemachine = StateMachine(GoToRandomTarget(self))
        # self.until_next_move = Chicken.BASE_MOVE_DELAY

    @property
    def speed(self) -> float:
        return 1

    def tick(self, dt: int):
        self.statemachine.tick(dt)
        # if self.target == None:
        #     self.target = self.new_target()
        #     self.until_next_move = Chicken.BASE_MOVE_DELAY

        # self.until_next_move -= dt
        # if self.until_next_move <= 0:
        #     self.pos = self.target
        #     self.target = None


    def load_surface(self, sheet: list[Surface]) -> None:
        self.surface = sheet[EntityTypes.CHICKEN.value].copy()
        self.surface.set_colorkey(Entity.COLOR_KEY)

