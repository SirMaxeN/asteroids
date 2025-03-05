import pygame
from ..utils.text import Text
from ..utils.state import State
from ..utils.constants import *
from ..utils.stateenum import StateEnum
from ..utils.resources import Resources
from ..utils.animation import Animation
from ..utils.rectparticle import RectParticle
from ..utils.audio import Audio


class Score(State):
    def on_start(self):
        super().on_start()

        self.texts = [
            Text("YOUR SCORE",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2, (255, 255, 255), Resources.FONT_XL),
            Text(f"{Resources.SCORE}",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50, (255, 255, 255), Resources.FONT_XL),

        ]

        if Resources.IS_MOBILE:
            self.texts.append(Text("tap anywhere to go back to menu",                 SCREEN_WIDTH /
                                   2, SCREEN_HEIGHT/2 + 150, (255, 255, 255), Resources.FONT_L))
        else:
            self.texts.append(Text("press ESC or ENTER key to go back to menu",
                                   SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150, (255, 255, 255), Resources.FONT_L))

        for i in Resources.credits(150):
            self.texts.append(i)

        for i in Resources.version(150):
            self.texts.append(i)

        for i in Resources.title(100):
            self.texts.append(i)

        self.updatable = pygame.sprite.Group()
        self.drawable_bottom = pygame.sprite.Group()
        self.drawable_mid = pygame.sprite.Group()

        Animation.containers = (self.updatable, self.drawable_mid)
        RectParticle.containers = (self.updatable, self.drawable_bottom)
        Animation(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT + 80, (60, 60, 60))

        if Resources.IS_MOBILE:
            self.lock_timer = 0.5
        else:
            self.lock_timer = 0.1

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()
        if self.lock_timer < 0:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_ESCAPE] or keys[pygame.K_RETURN]:
                        Audio.play_enter()
                        return StateEnum.MENU
                if event.type == pygame.FINGERDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    Audio.play_enter()
                    return StateEnum.MENU
        else:
            self.lock_timer -= dt

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
