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
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2 , (255, 255, 255), Resources.GAME_FONT_XL),
            Text(f"{Resources.SCORE}",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50, (255, 255, 255), Resources.GAME_FONT_XL),
            Text("press ESC or ENTER key to go back to menu",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150, (255, 255, 255), Resources.GAME_FONT_L),
            Text(f"ver {Resources.VERSION}",
                 SCREEN_WIDTH/2 - 570, SCREEN_HEIGHT / 2 + 330, (150, 150, 150), Resources.GAME_FONT_S),
            Text("base game made during boot.dev python course",
                 SCREEN_WIDTH/2 + 383, SCREEN_HEIGHT / 2 + 290, (150, 150, 150), Resources.GAME_FONT_S),
            Text("rest made by Jakub \"SirMaxeN\" Komar",
                 SCREEN_WIDTH/2 + 433, SCREEN_HEIGHT / 2 + 310, (150, 150, 150), Resources.GAME_FONT_S),
            Text("https://github.com/SirMaxeN/asteroids",
                 SCREEN_WIDTH/2 + 420, SCREEN_HEIGHT / 2 + 330, (150, 150, 150), Resources.GAME_FONT_S),
        ]

        self.title_text = Resources.title()

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_ESCAPE] or keys[pygame.K_RETURN]:
                    return StateEnum.MENU

        for text in self.texts:
            screen.blit(text.get_obj(), text.get_position())
        for text in self.title_text:
            screen.blit(text.get_obj(), text.get_position())

        return StateEnum.CONTINUE

    def on_end(self):
        while len(self.texts) > 0:
            self.texts.pop().kill()

        self.texts = []

        while len(self.title_text) > 0:
            self.title_text.pop().kill()

        self.title_text = []

        super().on_end()
