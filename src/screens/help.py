import pygame
from ..text import Text
from ..state import State
from ..constants import *
from ..stateenum import StateEnum
from ..resources import Resources


class Help(State):
    def on_start(self):
        super().on_start()

        self.texts = [
            Text("HELP SCREEN",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 260, (255, 255, 255), Resources.GAME_FONT_XL),
            Text("DURING GAME:",
                 SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 - 140, (255, 255, 255), Resources.GAME_FONT_M),
            Text("W or ARROW UP  -  move forward",
                 SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 - 90, (255, 255, 255), Resources.GAME_FONT_S),
            Text("S or ARROW DOWN  -  move backward",
                 SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 - 60, (255, 255, 255), Resources.GAME_FONT_S),
            Text("A or ARROW LEFT  -  rotate left",
                 SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2-30, (255, 255, 255), Resources.GAME_FONT_S),
            Text("D or ARROW RIGHT  -  rotate right",
                 SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2, (255, 255, 255), Resources.GAME_FONT_S),
            Text("M or SPACE  -  shoot",
                 SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 + 30, (255, 255, 255), Resources.GAME_FONT_S),
            Text("ESC  -  back to menu",
                 SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 + 60, (255, 255, 255), Resources.GAME_FONT_S),
            Text("HOW TO PLAY:",
                 SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT/2 - 140, (255, 255, 255), Resources.GAME_FONT_M),
            Text("Move ship around the space",
                 SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT/2 - 90, (255, 255, 255), Resources.GAME_FONT_S),
            Text("Avoid collision with asteroids",
                 SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT/2 - 60, (255, 255, 255), Resources.GAME_FONT_S),
            Text("Shoot to asteroids to get points",
                 SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT/2 - 30, (255, 255, 255), Resources.GAME_FONT_S),
            Text("Bigger asteroids will split to 2 smaller once",
                 SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT / 2, (255, 255, 255), Resources.GAME_FONT_S),
            Text("You have 3 lives",
                 SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT / 2 + 30, (255, 255, 255), Resources.GAME_FONT_S),
            Text("Space is looped around",
                 SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT / 2 + 60, (255, 255, 255), Resources.GAME_FONT_S),
            Text("press any key to go back to menu",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150, (255, 255, 255), Resources.GAME_FONT_L),
        ]

        for i in Resources.credits(150):
            self.texts.append(i)

        for i in Resources.version(150):
            self.texts.append(i)

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.KEYDOWN:
                return StateEnum.MENU

        for text in self.texts:
            screen.blit(text.get_obj(), text.get_position())

        return StateEnum.CONTINUE

    def on_end(self):

        while len(self.texts) > 0:
            self.texts.pop().kill()

        self.texts = []
        super().on_end()
