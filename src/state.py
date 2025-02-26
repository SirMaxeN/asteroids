import pygame
from .stateenum import StateEnum


class State:
    def __init__(self):
        self.__is_started = False

    def is_started(self):
        return self.__is_started

    def on_start(self):
        self.__is_started = True

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        # sub-classes must override
        pass

    def on_end(self):
        self.__is_started = False
