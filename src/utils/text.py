import pygame
from .constants import *
from typing import Tuple


class Text:
    def __init__(self, text: str, x: float, y: float, color: Tuple[int, int, int], font: pygame.font.Font):

        self.__text_obj: pygame.Surface = None
        self.__text_str: str = text
        self.__color:  Tuple[int, int, int] = color
        self.__position: pygame.Vector2 = pygame.Vector2(x, y)
        self.__font: pygame.font.Font = font
        self.__render_text()

    def __render_text(self):
        self.__text_obj = self.__font.render(
            self.__text_str, True, self.__color)

    def set_text(self, text: str):
        self.__text_str = text
        self.__render_text()

    def get_text(self) -> str:
        return self.__text_str

    def get_obj(self) -> pygame.Surface:
        return self.__text_obj

    def get_position(self) -> Tuple[float, float]:
        return (self.__position.x - self.__text_obj.get_width()/2, self.__position.y - self.__text_obj.get_height()/2)

    def kill(self):
        self.__text_obj = None
        self.__text_str = None
        self.__color = None
        self.__position = None
