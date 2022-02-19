from abc import ABC, abstractmethod
from random import randint
from typing import Any
from pygame import Vector2

from entities import Entity

class State(ABC):

    def __init__(self, entity: Entity) -> None:
        self.entity = entity

    @abstractmethod
    def tick(self, dt: int) -> Any:
        pass

class Idle(State):
    def tick(self, dt: int) -> State:
        if randint(1, 1000) == 1: return GoToRandomTarget(self.entity)
        return self

class GoToRandomTarget(State):
    def __init__(self, entity: Entity) -> None:
        super().__init__(entity)
        range = (8,8)
        self.target: Vector2 = self.pick_new_target(range)
        self.nextstep: Vector2 = self.get_next_step()
        self.until_next_move = entity.BASE_MOVE_DELAY * (1/entity.speed)

    def tick(self, dt: int) -> State:
        if self.entity.pos == self.target:
            return Idle(self.entity)
        

        self.until_next_move -= dt
        if self.until_next_move <= 0:
            self.entity.pos = self.nextstep
            self.nextstep = self.get_next_step()
            self.until_next_move = self.entity.BASE_MOVE_DELAY * (1/self.entity.speed)
            if self.nextstep.x == 0 and self.nextstep.y == 0:
                self.until_next_move *= 1.41421 # sqrt of 2

        return self

    def get_next_step(self) -> Vector2:
        nextstep = Vector2(0,0)
        if self.entity.pos.x < self.target.x: nextstep.x = 1
        elif self.entity.pos.x > self.target.x: nextstep.x = -1

        if self.entity.pos.y < self.target.y: nextstep.y = 1
        elif self.entity.pos.y > self.target.y: nextstep.y = -1

        return self.entity.pos + nextstep

    def pick_new_target(self, range: tuple[int,int]):
        return self.entity.pos + Vector2(randint(-range[0], range[0]), randint(-range[1], range[1]))

class StateMachine:
    def __init__(self, initial_state: State) -> None:
        self.current_state: State = initial_state

    def tick(self, dt: int):
        self.current_state = self.current_state.tick(dt)
