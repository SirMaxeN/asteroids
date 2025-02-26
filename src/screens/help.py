import pygame
from ..utils.text import Text
from ..utils.state import State
from ..utils.constants import *
from ..utils.stateenum import StateEnum
from ..utils.resources import Resources
from ..utils.animation import Animation
from ..utils.rectparticle import RectParticle
from ..utils.audio import Audio


class Help(State):
    def on_start(self):
        super().on_start()

        self.texts = [
            Text("HELP SCREEN",                 SCREEN_WIDTH/2,
                 SCREEN_HEIGHT/2 - 260, (255, 255, 255), Resources.FONT_XL),
            Text("DURING GAME:",                 SCREEN_WIDTH/2 - 300,
                 SCREEN_HEIGHT/2 - 140, (255, 255, 255), Resources.FONT_M),
            Text("W or ARROW UP  -  move forward",                 SCREEN_WIDTH /
                 2 - 300, SCREEN_HEIGHT/2 - 90, (255, 255, 255), Resources.FONT_S),
            Text("S or ARROW DOWN  -  move backward",                 SCREEN_WIDTH /
                 2 - 300, SCREEN_HEIGHT/2 - 60, (255, 255, 255), Resources.FONT_S),
            Text("A or ARROW LEFT  -  rotate left",                 SCREEN_WIDTH /
                 2 - 300, SCREEN_HEIGHT/2 - 30, (255, 255, 255), Resources.FONT_S),
            Text("D or ARROW RIGHT  -  rotate right",                 SCREEN_WIDTH /
                 2 - 300, SCREEN_HEIGHT/2, (255, 255, 255), Resources.FONT_S),
            Text("M or SPACE  -  shoot",                 SCREEN_WIDTH/2 - 300,
                 SCREEN_HEIGHT/2 + 30, (255, 255, 255), Resources.FONT_S),
            Text("ESC  -  back to menu",                 SCREEN_WIDTH/2 - 300,
                 SCREEN_HEIGHT/2 + 60, (255, 255, 255), Resources.FONT_S),
            Text("HOW TO PLAY:",                 SCREEN_WIDTH/2 + 300,
                 SCREEN_HEIGHT/2 - 140, (255, 255, 255), Resources.FONT_M),
            Text("Move ship around the space",                 SCREEN_WIDTH/2 +
                 300, SCREEN_HEIGHT/2 - 90, (255, 255, 255), Resources.FONT_S),
            Text("Avoid collision with asteroids",                 SCREEN_WIDTH /
                 2 + 300, SCREEN_HEIGHT/2 - 60, (255, 255, 255), Resources.FONT_S),
            Text("Shoot to asteroids to get points",                 SCREEN_WIDTH /
                 2 + 300, SCREEN_HEIGHT/2 - 30, (255, 255, 255), Resources.FONT_S),
            Text("Bigger asteroids will split to 2 smaller once",                 SCREEN_WIDTH /
                 2 + 300, SCREEN_HEIGHT / 2, (255, 255, 255), Resources.FONT_S),
            Text("You have 3 lives",                 SCREEN_WIDTH/2 + 300,
                 SCREEN_HEIGHT / 2 + 30, (255, 255, 255), Resources.FONT_S),
            Text("Space is looped around",                 SCREEN_WIDTH/2 + 300,
                 SCREEN_HEIGHT / 2 + 60, (255, 255, 255), Resources.FONT_S),
            Text("press any key to go back to menu",                 SCREEN_WIDTH /
                 2, SCREEN_HEIGHT/2 + 150, (255, 255, 255), Resources.FONT_L),
        ]

        for i in Resources.credits(150):
            self.texts.append(i)

        for i in Resources.version(150):
            self.texts.append(i)

        self.updatable = pygame.sprite.Group()
        self.drawable_bottom = pygame.sprite.Group()
        self.drawable_mid = pygame.sprite.Group()

        Animation.containers = (self.updatable, self.drawable_mid)
        RectParticle.containers = (self.updatable, self.drawable_bottom)
        Animation(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT + 80, (60, 60, 60))

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.KEYDOWN:
                Audio.play_enter()
                return StateEnum.MENU

        for obj in self.updatable:
            obj.update(dt)

        for obj in self.drawable_bottom:
            obj.draw(screen)
        for obj in self.drawable_mid:
            obj.draw(screen)

        for text in self.texts:
            screen.blit(text.get_obj(), text.get_position())

        return StateEnum.CONTINUE

    def on_end(self):

        while len(self.texts) > 0:
            self.texts.pop().kill()

        self.texts = []

        self.drawable_bottom.empty()
        self.drawable_mid.empty()
        self.updatable.empty()

        self.updatable = None
        self.drawable_bottom = None
        self.drawable_mid = None

        Animation.containers = None
        RectParticle.containers = None

        super().on_end()
