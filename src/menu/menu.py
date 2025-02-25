import pygame
from .text import Text
from ..state import State
from ..constants import *


class Menu(State):
    def on_start(self):
        super().on_start()

        self.texts = []

        text = Text("PRESS ENTER TO START",
                         SCREEN_WIDTH/2, SCREEN_HEIGHT/2, (255, 255, 255))

        self.texts.append(text)

    def loop(self, dt: float, screen: pygame.display) -> bool:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            return False

        for text in self.texts:
            screen.blit(text.get_text(), text.get_position())

        return True

    def on_end(self):

        while len(self.texts) > 0:
            self.texts.pop().kill()

        self.texts = []
        super().on_end()
