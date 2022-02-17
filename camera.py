import pygame as py
from pygame import Rect, Vector2

class Camera:
    def __init__(self, size: Rect, pos: Vector2=(0,0)) -> None:
        self.viewport = size.copy()
        self.viewport.center = pos
        self.speed = 1
    
    def move(self, x: float, y: float):
        self.viewport = self.viewport.move(x, y)

    def process_event(self, event: py.event.Event):
        if(event.type != py.KEYDOWN): return

        mods = py.key.get_mods()
        modded_speed = self.speed
        if(mods & py.KMOD_CTRL): modded_speed *= 5
        if(mods & py.KMOD_SHIFT): modded_speed *= 10

        key = event.key

        if(key == py.K_RIGHT): self.move(modded_speed, 0)
        elif(key == py.K_LEFT): self.move(-modded_speed, 0) 
        if(key == py.K_DOWN): self.move(0, modded_speed)
        elif(key == py.K_UP): self.move(0, -modded_speed)