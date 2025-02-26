import pygame
from ..utils.text import Text
from ..utils.state import State
from ..utils.constants import *
from ..utils.stateenum import StateEnum
from ..utils.resources import Resources
from ..utils.animation import Animation
from ..utils.rectparticle import RectParticle
from ..utils.audio import Audio


class Menu(State):
    def on_start(self):
        super().on_start()

        self.menu_text = [
            Text("START_GAME",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2, (255, 255, 255), Resources.FONT_L),
            Text("HELP",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40, (255, 255, 255), Resources.FONT_L),
            Text("SOUNDS_ON",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 80, (255, 255, 255), Resources.FONT_L),
            Text("EXIT_GAME",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 120, (255, 255, 255), Resources.FONT_L)
        ]

        self.menu_index = 0
        self.current_text = None
        self.set_current_selected()

        self.texts = []

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

        self.check_sound_text()

    def set_current_selected(self):
        if self.current_text != None:
            s: str = self.current_text.get_text()
            s = s.replace("> ", "")
            s = s.replace(" <", "")
            self.current_text.set_text(s)

        self.current_text = self.menu_text[self.menu_index]
        s: str = self.current_text.get_text()
        self.current_text.set_text(f"> {s} <")

    def change_sound(self):
        Audio.music_mute_change()
        Audio.sound_mute_change()
        self.check_sound_text()

    def check_sound_text(self):
        if Audio.SOUND_VOLUME > 0:
            self.menu_text[2].set_text(
                self.menu_text[2].get_text().replace("OFF", "ON"))
        else:
            self.menu_text[2].set_text(
                self.menu_text[2].get_text().replace("ON", "OFF"))

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_ESCAPE]:
                    return StateEnum.EXIT
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    Audio.play_click()
                    self.menu_index += 1
                    self.menu_index %= len(self.menu_text)
                    self.set_current_selected()
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    Audio.play_click()
                    self.menu_index -= 1
                    self.menu_index %= len(self.menu_text)
                    self.set_current_selected()
                if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                    Audio.play_enter()
                    if self.menu_index == 0:
                        return StateEnum.GAME
                    elif self.menu_index == 1:
                        return StateEnum.HELP
                    elif self.menu_index == 2:
                        self.change_sound()
                    elif self.menu_index == 3:
                        return StateEnum.EXIT

        for obj in self.updatable:
            obj.update(dt)

        for obj in self.drawable_bottom:
            obj.draw(screen)
        for obj in self.drawable_mid:
            obj.draw(screen)

        for text in self.menu_text:
            screen.blit(text.get_obj(), text.get_position())
        for text in self.texts:
            screen.blit(text.get_obj(), text.get_position())

        return StateEnum.CONTINUE

    def on_end(self):
        while len(self.texts) > 0:
            self.texts.pop().kill()

        self.texts = []

        while len(self.menu_text) > 0:
            self.menu_text.pop().kill()

        self.menu_text = []

        for obj in self.updatable:
            obj.kill()

        self.drawable_bottom.empty()
        self.drawable_mid.empty()
        self.updatable.empty()

        self.updatable = None
        self.drawable_bottom = None
        self.drawable_mid = None

        Animation.containers = None
        RectParticle.containers = None

        super().on_end()
