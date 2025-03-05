import pygame
from ..utils.button import Button
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
        self.buttons = pygame.sprite.Group()

        Button.containers = (self.buttons, self.updatable, self.drawable_mid)
        Animation.containers = (self.updatable, self.drawable_mid)
        RectParticle.containers = (self.updatable, self.drawable_bottom)
        Animation(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT + 80, (60, 60, 60))

        if Resources.IS_MOBILE:
            Button(SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.55, 60, "up", (100, 100, 100)).set_icon([
                [-48.0, -11.7, -51.0, -14.7, -51.0, -19.7, -49.0, -23.7, -46.0, -25.7, -43.0, -25.7, -39.0, -24.7, -30.0, -15.7, -10.0, 4.3, -1.0, 13.3, 34.0, -21.7, 37.0, -24.7,
                 39.0, -25.7, 43.0, -25.7, 45.0, -24.7, 48.0, -21.7, 49.0, -19.7, 49.0, -16.7, 48.0, -13.7, 6.0, 28.3, 3.0, 31.3, 0.0, 32.3, -2.0, 32.3, -5.0, 31.3, -8.0, 28.3],
                [-47.0, -50.7, -50.0, -53.7, -50.0, -58.7, -48.0, -62.7, -45.0, -64.7, -42.0, -64.7, -38.0, -63.7, -29.0, -54.7, -9.0, -34.7, 0.0, -25.7, 35.0, -60.7, 38.0, -63.7,
                 40.0, -64.7, 44.0, -64.7, 46.0, -63.7, 49.0, -60.7, 50.0, -58.7, 50.0, -55.7, 49.0, -52.7, 7.0, -10.7, 4.0, -7.7, 1.0, -6.7, -1.0, -6.7, -4.0, -7.7, -7.0, -10.7]
            ], 0.01, 0, 25, 0)
            Button(SCREEN_WIDTH * 0.9, SCREEN_HEIGHT *
                   0.75, 60, "down", (100, 100, 100)).set_icon([
                       [-48.0, -11.7, -51.0, -14.7, -51.0, -19.7, -49.0, -23.7, -46.0, -25.7, -43.0, -25.7, -39.0, -24.7, -30.0, -15.7, -10.0, 4.3, -1.0, 13.3, 34.0, -21.7, 37.0, -24.7,
                        39.0, -25.7, 43.0, -25.7, 45.0, -24.7, 48.0, -21.7, 49.0, -19.7, 49.0, -16.7, 48.0, -13.7, 6.0, 28.3, 3.0, 31.3, 0.0, 32.3, -2.0, 32.3, -5.0, 31.3, -8.0, 28.3],
                       [-47.0, -50.7, -50.0, -53.7, -50.0, -58.7, -48.0, -62.7, -45.0, -64.7, -42.0, -64.7, -38.0, -63.7, -29.0, -54.7, -9.0, -34.7, 0.0, -25.7, 35.0, -60.7, 38.0, -63.7,
                        40.0, -64.7, 44.0, -64.7, 46.0, -63.7, 49.0, -60.7, 50.0, -58.7, 50.0, -55.7, 49.0, -52.7, 7.0, -10.7, 4.0, -7.7, 1.0, -6.7, -1.0, -6.7, -4.0, -7.7, -7.0, -10.7]
                   ], 0.01, 0, 25, 180)
            Button(SCREEN_WIDTH * 0.1, SCREEN_HEIGHT *
                   0.65, 60, "enter", (100, 100, 100)).set_icon([
                       [-131.0, -58.0, -120.0, -79.0, -106.0, -98.0, -91.5, -110.9, -81.2, -119.2, -64.5, -129.0, -45.5, -137.0, -32.9, -140.4, -17.6, -143.2, 1.7, -144.1, 16.2, -143.4, 34.8, -140.4, 58.4, -131.9, 74.2, -123.3, 93.9, -109.0, 108.0, -95.5, 119.5, -80.1, 133.6, -51.4, 141.1, -23.7, 141.7, -7.3, 141.1, 14.2, 135.6, 40.9, 124.0, 66.0, 112.7, 83.2, 100.7, 97.3, 80.0, 112.0, 62.0, 121.6, 45.0, 129.0, 28.0, 134.0, 8.0, 138.0, -12.0, 138.0, -29.1, 135.7, -52.0, 129.0, -66.1, 122.3, -88.6, 107.1, -106.8, 90.2, -123.8, 66.2, -136.5, 34.7, -141.3, 6.3, -140.7, -20.6, -
                        136.0, -43.0, -113.0, -36.0, -118.1, -9.0, -116.7, 12.1, -109.5, 40.1, -98.3, 61.7, -82.8, 81.0, -66.4, 95.0, -50.0, 105.0, -23.6, 112.8, 10.0, 114.0, 25.8, 110.3, 46.0, 103.0, 64.6, 94.3, 86.5, 77.5, 97.4, 63.2, 106.6, 47.8, 114.8, 27.6, 118.8, 6.0, 118.8, -11.4, 115.7, -27.2, 108.0, -51.1, 97.0, -70.9, 86.7, -83.5, 65.8, -100.7, 51.6, -109.0, 36.7, -116.0, 21.1, -119.2, 7.8, -120.8, -6.3, -120.8, -19.3, -119.5, -28.9, -117.4, -42.4, -113.0, -59.0, -104.8, -72.2, -96.5, -79.0, -90.0, -93.0, -76.0, -104.0, -58.0, -110.0, -45.0, -113.0, -36.0, -135.9, -43.0],
                       [-68.0, -40.0, -58.0, -53.0, -51.2, -59.7, -39.0, -68.9, -28.7, -74.6, -14.0, -78.6, -0.3, -79.8, 4.9, -79.4, 7.9, -77.4, 10.9, -72.8, 11.7, -67.5, 10.7, -61.9, 5.3, -56.7, -3.2, -55.3, -13.6, -
                        53.9, -24.7, -49.0, -33.0, -44.0, -44.0, -32.0, -50.2, -19.9, -52.2, -10.4, -53.6, 0.7, -57.0, 7.0, -63.1, 8.9, -69.1, 9.1, -73.0, 6.7, -76.2, 2.3, -77.2, -3.2, -75.4, -18.3, -71.7, -29.7]
                   ], 0.0045, 0, 0, 160)

        self.fingers = {}

        self.check_sound_text()

        # self.change_sound()

    def get_pointer_x(self, event) -> float:
        x: float = 0
        if hasattr(event, 'pos'):
            x: float = event.pos[0]
        else:
            x: float = event.x * SCREEN_WIDTH
        return x

    def get_pointer_y(self, event) -> float:
        y: float = 0
        if hasattr(event, 'pos'):
            y: float = event.pos[1]
        else:
            y: float = event.y * SCREEN_HEIGHT
        return y

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

    def __press(self):
        Audio.play_click()

    def press_down(self):
        self.__press()
        self.menu_index += 1
        self.menu_index %= len(self.menu_text)
        self.set_current_selected()

    def press_up(self):
        self.__press()
        self.menu_index -= 1
        self.menu_index %= len(self.menu_text)
        self.set_current_selected()

    def press_enter(self):
        Audio.play_enter()
        if self.menu_index == 0:
            return StateEnum.GAME
        elif self.menu_index == 1:
            return StateEnum.HELP
        elif self.menu_index == 2:
            self.change_sound()
            return None
        elif self.menu_index == 3:
            return StateEnum.EXIT

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_ESCAPE]:
                    return StateEnum.EXIT
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    self.press_down()
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    self.press_up()
                if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                    state = self.press_enter()
                    if state != None:
                        return state

            if event.type == pygame.FINGERDOWN:
                x = self.get_pointer_x(event)
                y = self.get_pointer_y(event)
                self.fingers[event.finger_id] = x, y

            if event.type == pygame.FINGERUP:
                self.fingers.pop(event.finger_id, None)

        for finger, pos in self.fingers.items():
            x: float = pos[0]
            y: float = pos[1]
            for button in self.buttons:
                if button.is_pressed(x, y):
                    if button.type == "up":
                        self.press_up()
                    if button.type == "down":
                        self.press_down()
                    if button.type == "enter":
                        state = self.press_enter()
                        if state != None:
                            return state

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
        self.buttons.empty()

        self.updatable = None
        self.drawable_bottom = None
        self.drawable_mid = None
        self.buttons = None

        Animation.containers = None
        RectParticle.containers = None

        super().on_end()
