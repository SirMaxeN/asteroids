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

        AsteroidField.containers = (self.updatable)

        AsteroidFake.containers = (
            self.asteroids_fake, self.updatable, self.drawable_bottom)

        Asteroid.containers = (
            self.asteroids, self.updatable, self.drawable_middle)
        Shot.containers = (self.shots, self.updatable, self.drawable_middle)
        ParticleEngine.containers = (self.updatable, self.drawable_middle)
        ParticleAnimation.containers = (self.updatable, self.drawable_top)

        Player.containers = (self.updatable, self.drawable_top)

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

        self.restart_timer = None

    def set_lives_text(self):
        text = ""
        if self.lives>0:
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

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_ESCAPE]:
                    Audio.play_end()

                    return StateEnum.SCORE

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
                obj.split()
                self.lives -= 1
                self.set_lives_text()
                self.restart_timer = 0

                if self.lives > 0:
                    Audio.play_dead()
                    Audio.play_dead_symth()

                else:
                    Audio.play_dead()
                    Audio.play_end()

        for ast in self.asteroids:
            for bullet in self.shots:
                if ast.collision(bullet):
                    ast.split()
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

        self.updatable = None
        self.drawable_bottom = None
        self.drawable_middle = None
        self.drawable_top = None
        self.asteroids = None
        self.shots = None
        self.asteroids_fake = None

        AsteroidField.containers = None
        AsteroidFake.containers = None
        Asteroid.containers = None
        Shot.containers = None
        ParticleEngine.containers = None
        Player.containers = None
        ParticleAnimation.containers = None

        super().on_end()
