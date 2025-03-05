import pygame
from ..utils.state import State
from ..utils.constants import *
from ..game.player import Player
from ..game.asteroid import Asteroid
from ..game.asteroidfield import AsteroidField
from ..game.asteroidfake import AsteroidFake
from ..game.asteroidfieldfake import AsteroidFieldFake
from ..game.shot import Shot
from ..game.particleengine import ParticleEngine
from ..utils.stateenum import StateEnum
from ..utils.text import Text
from ..utils.resources import Resources
from ..utils.audio import Audio
from ..utils.particleanimation import ParticleAnimation
from ..game.boostbomb import BoostBomb
from ..game.boostshot import BoostShot
from ..utils.button import Button
from ..utils.joystick import Joystick


class Game(State):
    def on_start(self):
        super().on_start()

        self.updatable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.asteroids_fake = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.drawable_bottom = pygame.sprite.Group()
        self.drawable_middle = pygame.sprite.Group()
        self.drawable_top = pygame.sprite.Group()
        self.boost = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()

        AsteroidField.containers = (self.updatable)

        AsteroidFake.containers = (
            self.asteroids_fake, self.updatable, self.drawable_bottom)

        Asteroid.containers = (
            self.asteroids, self.updatable, self.drawable_middle)
        Shot.containers = (self.shots, self.updatable, self.drawable_middle)
        ParticleEngine.containers = (self.updatable, self.drawable_middle)
        ParticleAnimation.containers = (self.updatable, self.drawable_top)

        BoostShot.containers = (self.boost, self.updatable, self.drawable_top)
        BoostBomb.containers = (self.boost, self.updatable, self.drawable_top)
        Player.containers = (self.updatable, self.drawable_top)

        Button.containers = (self.buttons, self.updatable, self.drawable_top)
        Joystick.containers = (self.updatable, self.drawable_top)

        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.asteroidfield = AsteroidField()
        AsteroidFieldFake((10, 10, 10), 0.008)
        AsteroidFieldFake((20, 20, 20), 0.01)
        AsteroidFieldFake((30, 30, 30), 0.015)

        Resources.SCORE = 0
        self.score_timer = 0
        self.lives = 3
        self.texts = [
            Text(f"SCORE: {Resources.SCORE}",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - 340, (150, 150, 150), Resources.FONT_S),
            Text("LIVES",
                 SCREEN_WIDTH/2 - 600, SCREEN_HEIGHT / 2 - 340, (150, 150, 150), Resources.FONT_S),
            Text("",
                 SCREEN_WIDTH/2 - 600, SCREEN_HEIGHT / 2 - 320, (150, 150, 150), Resources.FONT_S),
        ]

        for i in Resources.credits(75):
            self.texts.append(i)

        for i in Resources.version(75):
            self.texts.append(i)

        self.set_lives_text()

        self.joystick = None

        if Resources.IS_MOBILE:

            Button(SCREEN_WIDTH * 0.97, SCREEN_HEIGHT * 0.05, 28, "exit", (100, 100, 100)).set_icon([
                [-39.7, -27.8, -49.7, -37.8, -49.2, -43.2, -47.1, -46.6, -43.1, -48.8, -38.7, -47.8, 0.3, -8.8, 37.3, -46.8, 41.0, -48.6, 46.2, -48.0, 48.0, -46.4, 50.0, -43.9, 50.0, -41.7, 50.1, -39.5, 49.3, -
                 36.8, 12.3, 0.3, 49.3, 35.3, 50.3, 40.3, 49.3, 43.3, 46.3, 46.3, 42.3, 47.3, 38.3, 46.3, -0.7, 9.3, -37.7, 46.3, -40.7, 47.3, -44.7, 47.3, -47.7, 45.3, -49.7, 41.3, -49.7, 36.3, -12.7, -0.8]
            ], 0.01, 2, 2, 0)
            Button(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT *
                   0.735, 50, "shoot", (100, 100, 100)).set_icon([
                       [-131.0, -58.0, -120.0, -79.0, -106.0, -98.0, -91.5, -110.9, -81.2, -119.2, -64.5, -129.0, -45.5, -137.0, -32.9, -140.4, -17.6, -143.2, 1.7, -144.1, 16.2, -143.4, 34.8, -140.4, 58.4, -131.9, 74.2, -123.3, 93.9, -109.0, 108.0, -95.5, 119.5, -80.1, 133.6, -51.4, 141.1, -23.7, 141.7, -7.3, 141.1, 14.2, 135.6, 40.9, 124.0, 66.0, 112.7, 83.2, 100.7, 97.3, 80.0, 112.0, 62.0, 121.6, 45.0, 129.0, 28.0, 134.0, 8.0, 138.0, -12.0, 138.0, -29.1, 135.7, -52.0, 129.0, -66.1, 122.3, -88.6, 107.1, -106.8, 90.2, -123.8, 66.2, -136.5, 34.7, -141.3, 6.3, -140.7, -20.6, -
                        136.0, -43.0, -113.0, -36.0, -118.1, -9.0, -116.7, 12.1, -109.5, 40.1, -98.3, 61.7, -82.8, 81.0, -66.4, 95.0, -50.0, 105.0, -23.6, 112.8, 10.0, 114.0, 25.8, 110.3, 46.0, 103.0, 64.6, 94.3, 86.5, 77.5, 97.4, 63.2, 106.6, 47.8, 114.8, 27.6, 118.8, 6.0, 118.8, -11.4, 115.7, -27.2, 108.0, -51.1, 97.0, -70.9, 86.7, -83.5, 65.8, -100.7, 51.6, -109.0, 36.7, -116.0, 21.1, -119.2, 7.8, -120.8, -6.3, -120.8, -19.3, -119.5, -28.9, -117.4, -42.4, -113.0, -59.0, -104.8, -72.2, -96.5, -79.0, -90.0, -93.0, -76.0, -104.0, -58.0, -110.0, -45.0, -113.0, -36.0, -135.9, -43.0],
                       [-68.0, -40.0, -58.0, -53.0, -51.2, -59.7, -39.0, -68.9, -28.7, -74.6, -14.0, -78.6, -0.3, -79.8, 4.9, -79.4, 7.9, -77.4, 10.9, -72.8, 11.7, -67.5, 10.7, -61.9, 5.3, -56.7, -3.2, -55.3, -13.6, -
                        53.9, -24.7, -49.0, -33.0, -44.0, -44.0, -32.0, -50.2, -19.9, -52.2, -10.4, -53.6, 0.7, -57.0, 7.0, -63.1, 8.9, -69.1, 9.1, -73.0, 6.7, -76.2, 2.3, -77.2, -3.2, -75.4, -18.3, -71.7, -29.7]
                   ], 0.0045, 0, 0, 160)

            Button(SCREEN_WIDTH * 0.1, SCREEN_HEIGHT *
                   0.65 - 10, 50, "up", (100, 100, 100)).set_icon([
                       [-48.0, -11.7, -51.0, -14.7, -51.0, -19.7, -49.0, -23.7, -46.0, -25.7, -43.0, -25.7, -39.0, -24.7, -30.0, -15.7, -10.0, 4.3, -1.0, 13.3, 34.0, -21.7, 37.0, -24.7,
                        39.0, -25.7, 43.0, -25.7, 45.0, -24.7, 48.0, -21.7, 49.0, -19.7, 49.0, -16.7, 48.0, -13.7, 6.0, 28.3, 3.0, 31.3, 0.0, 32.3, -2.0, 32.3, -5.0, 31.3, -8.0, 28.3],
                       [-47.0, -50.7, -50.0, -53.7, -50.0, -58.7, -48.0, -62.7, -45.0, -64.7, -42.0, -64.7, -38.0, -63.7, -29.0, -54.7, -9.0, -34.7, 0.0, -25.7, 35.0, -60.7, 38.0, -63.7,
                        40.0, -64.7, 44.0, -64.7, 46.0, -63.7, 49.0, -60.7, 50.0, -58.7, 50.0, -55.7, 49.0, -52.7, 7.0, -10.7, 4.0, -7.7, 1.0, -6.7, -1.0, -6.7, -4.0, -7.7, -7.0, -10.7]
                   ], 0.01, 0, 25, 0)
            Button(SCREEN_WIDTH * 0.1, SCREEN_HEIGHT *
                   0.82 + 10, 50, "down", (100, 100, 100)).set_icon([
                       [-48.0, -11.7, -51.0, -14.7, -51.0, -19.7, -49.0, -23.7, -46.0, -25.7, -43.0, -25.7, -39.0, -24.7, -30.0, -15.7, -10.0, 4.3, -1.0, 13.3, 34.0, -21.7, 37.0, -24.7,
                        39.0, -25.7, 43.0, -25.7, 45.0, -24.7, 48.0, -21.7, 49.0, -19.7, 49.0, -16.7, 48.0, -13.7, 6.0, 28.3, 3.0, 31.3, 0.0, 32.3, -2.0, 32.3, -5.0, 31.3, -8.0, 28.3],
                       [-47.0, -50.7, -50.0, -53.7, -50.0, -58.7, -48.0, -62.7, -45.0, -64.7, -42.0, -64.7, -38.0, -63.7, -29.0, -54.7, -9.0, -34.7, 0.0, -25.7, 35.0, -60.7, 38.0, -63.7,
                        40.0, -64.7, 44.0, -64.7, 46.0, -63.7, 49.0, -60.7, 50.0, -58.7, 50.0, -55.7, 49.0, -52.7, 7.0, -10.7, 4.0, -7.7, 1.0, -6.7, -1.0, -6.7, -4.0, -7.7, -7.0, -10.7]
                   ], 0.01, 0, 25, 180)

            self.joystick = Joystick(SCREEN_WIDTH * 0.9, SCREEN_HEIGHT *
                                     0.65, 80, (100, 100, 100))

        self.restart_timer = None

        self.fingers = {}
        self.joystick_finger_id = None

    def set_lives_text(self):
        text = ""
        if self.lives > 0:
            for i in range(0, self.lives-1):
                text += "X "
            text += "X"
        self.texts[2].set_text(text)

    def update_score(self):
        self.texts[0].set_text(f"SCORE: {Resources.SCORE}")

    def restart(self):
        for obj in self.asteroids:
            obj.kill()
        for obj in self.shots:
            obj.kill()
        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

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

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_ESCAPE]:
                    Audio.play_end()
                    return StateEnum.SCORE
            if event.type == pygame.FINGERDOWN:
                x = self.get_pointer_x(event)
                y = self.get_pointer_y(event)
                self.fingers[event.finger_id] = x, y

                for button in self.buttons:
                    if button.is_pressed(x, y):
                        if button.type == "exit":
                            Audio.play_end()
                            return StateEnum.SCORE
                        if button.type == "shoot":
                            button.toggle = not (button.toggle)
                        if button.type == "brake":
                            button.toggle = not (button.toggle)

                if self.joystick and self.joystick.is_pressed(x, y):
                    self.joystick_finger_id = event.finger_id
                    self.joystick.register_hold(x, y)

            if event.type == pygame.FINGERMOTION:
                x = self.get_pointer_x(event)
                y = self.get_pointer_y(event)
                self.fingers[event.finger_id] = x, y

            if event.type == pygame.FINGERUP:
                self.fingers.pop(event.finger_id, None)
                if event.finger_id == self.joystick_finger_id:
                    self.joystick_finger_id = None
                    self.joystick.stop_held()
                    if self.player != None:
                        self.player.joystick_up = False
                else:
                    if self.player != None:
                        self.player.joystick_down = False
                        self.player.joystick_up = False
                    for button in self.buttons:
                        button.active = False

        for finger, pos in self.fingers.items():
            x: float = pos[0]
            y: float = pos[1]
            if finger == self.joystick_finger_id:
                self.joystick.current_pos(x, y)
                if self.player != None:
                    self.player.set_rotation = self.joystick.stick_angle
            else:
                for button in self.buttons:
                    if button.is_pressed(x, y):
                        if self.player != None:
                            if button.type == "down":
                                button.active = True
                                self.player.joystick_down = True
                                self.player.joystick_up = False
                            if button.type == "up":
                                button.active = True
                                self.player.joystick_down = False
                                self.player.joystick_up = True

        for button in self.buttons:
            if button.toggle == True:
                if self.player != None:
                    if button.type == "shoot":
                        self.player.shoot()

        if self.score_timer > 1:
            Resources.SCORE += SCORE_PER_SEC
            self.update_score()
            self.score_timer = 0

        self.score_timer += dt

        if self.restart_timer != None:
            self.restart_timer += dt
            if self.restart_timer > 2:
                self.restart_timer = None
                if self.lives <= 0:
                    return StateEnum.SCORE
                else:
                    self.restart()

        for obj in self.updatable:
            obj.update(dt)

        for obj in self.asteroids:
            if self.player != None and obj.collision(self.player):
                self.player.dead()
                self.player = None
                obj.split(False)
                self.lives -= 1
                self.set_lives_text()
                self.restart_timer = 0

                if self.lives > 0:
                    Audio.play_dead()
                    Audio.play_dead_symth()
                else:
                    Audio.play_dead()
                    Audio.play_end()

        for obj in self.boost:
            if self.player != None and obj.collision(self.player):
                if obj.type == "bomb":
                    for ast in self.asteroids:
                        ast.split(False)
                elif obj.type == "shot":
                    self.player.start_shoot_boost()
                obj.collect()

        for ast in self.asteroids:
            for bullet in self.shots:
                if ast.collision(bullet):
                    is_boost = False
                    if len(self.boost) < 3:
                        is_boost = True
                    ast.split(is_boost)
                    bullet.kill()
                    self.update_score()

        for obj in self.drawable_bottom:
            obj.draw(screen)

        for text in self.texts:
            screen.blit(text.get_obj(), text.get_position())

        for obj in self.drawable_middle:
            obj.draw(screen)

        for obj in self.drawable_top:
            obj.draw(screen)

        return StateEnum.CONTINUE

    def on_end(self):

        while len(self.texts) > 0:
            self.texts.pop().kill()

        self.texts = []

        for obj in self.updatable:
            obj.kill()

        self.updatable.empty()
        self.drawable_bottom.empty()
        self.drawable_middle.empty()
        self.drawable_top.empty()
        self.asteroids.empty()
        self.shots.empty()
        self.asteroids_fake.empty()
        self.boost.empty()
        self.buttons.empty()

        self.updatable = None
        self.drawable_bottom = None
        self.drawable_middle = None
        self.drawable_top = None
        self.asteroids = None
        self.shots = None
        self.asteroids_fake = None
        self.boost = None
        self.buttons = None

        AsteroidField.containers = None
        AsteroidFake.containers = None
        Asteroid.containers = None
        Shot.containers = None
        ParticleEngine.containers = None
        Player.containers = None
        ParticleAnimation.containers = None
        BoostShot.containers = None
        BoostBomb.containers = None

        super().on_end()
