import pygame
from ..text import Text
from ..state import State
from ..constants import *
from ..stateenum import StateEnum
from ..resources import Resources


class Score(State):
    def on_start(self):
        super().on_start()

        self.texts = [
            Text("YOUR SCORE",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2, (255, 255, 255), Resources.GAME_FONT_XL),
            Text(f"{Resources.SCORE}",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50, (255, 255, 255), Resources.GAME_FONT_XL),
            Text("press ESC or ENTER key to go back to menu",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150, (255, 255, 255), Resources.GAME_FONT_L),
        ]

        for i in Resources.credits(150):
            self.texts.append(i)

        for i in Resources.version(150):
            self.texts.append(i)

        for i in Resources.title(100):
            self.texts.append(i)

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_ESCAPE] or keys[pygame.K_RETURN]:
                    return StateEnum.MENU

        for text in self.texts:
            screen.blit(text.get_obj(), text.get_position())

        return StateEnum.CONTINUE

    def on_end(self):
        while len(self.texts) > 0:
            self.texts.pop().kill()

        self.texts = []

        super().on_end()
