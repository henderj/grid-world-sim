from pygame import Surface, Vector2
from game.statemachine import Idle, StateMachine

from game.entities.entity import Entity, EntityTypes

class Chicken(Entity):

    def __init__(self, pos: Vector2) -> None:
        super().__init__(pos)
        self.statemachine = StateMachine(Idle(self))

    @property
    def speed(self) -> float:
        return 1

    def tick(self, dt: int):
        super().tick(dt)
        self.statemachine.tick(dt)


    def load_surface(self, sheet: list[Surface]) -> None:
        self.surface = sheet[EntityTypes.CHICKEN.value].copy()
        self.surface.set_colorkey(Entity.COLOR_KEY)
