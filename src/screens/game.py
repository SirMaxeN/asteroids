import pygame
from ..state import State
from ..constants import *
from ..game.player import Player
from ..game.asteroid import Asteroid
from ..game.asteroidfield import AsteroidField
from ..game.asteroidfake import AsteroidFake
from ..game.asteroidfieldfake import AsteroidFieldFake
from ..game.shot import Shot
from ..game.particle import Particle
from ..stateenum import StateEnum
from ..text import Text
from ..resources import Resources


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
        Particle.containers = (self.updatable, self.drawable_middle)

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
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - 340, (150, 150, 150), Resources.GAME_FONT_S),
            Text("LIVES",
                 SCREEN_WIDTH/2 - 600, SCREEN_HEIGHT / 2 - 340, (150, 150, 150), Resources.GAME_FONT_S),
            Text("",
                 SCREEN_WIDTH/2 - 600, SCREEN_HEIGHT / 2 - 320, (150, 150, 150), Resources.GAME_FONT_S),

        ]

        for i in Resources.credits(75):
            self.texts.append(i)

        for i in Resources.version(75):
            self.texts.append(i)

        self.set_lives_text()

    def set_lives_text(self):
        text = ""
        for i in range(0, self.lives-1):
            text += "X "
        text += "X"
        self.texts[2].set_text(text)

    def update_score(self):
        self.texts[0].set_text(f"SCORE: {Resources.SCORE}")

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_ESCAPE]:
                    return StateEnum.SCORE

        if self.score_timer > 1:
            Resources.SCORE += SCORE_PER_SEC
            self.update_score()
            self.score_timer = 0

        self.score_timer += dt

        for obj in self.updatable:
            obj.update(dt)

        for obj in self.asteroids:
            if obj.collision(self.player):
                if self.lives > 1:
                    self.lives -= 1
                    self.set_lives_text()
                    for obj in self.asteroids:
                        obj.kill()
                    for obj in self.shots:
                        obj.kill()
                    self.player.velocity.y = 0
                    self.player.position.x = SCREEN_WIDTH / 2
                    self.player.position.y = SCREEN_HEIGHT / 2
                else:
                    return StateEnum.SCORE

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
        Particle.containers = None
        Player.containers = None

        super().on_end()
