import pygame
from ..state import State
from ..constants import *
from .player import Player
from .asteroid import Asteroid
from .asteroidfield import AsteroidField
from .shot import Shot


class Game(State):
    def on_start(self):
        super().on_start()

        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable)
        Shot.containers = (self.shots, self.updatable, self.drawable)

        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.asteroidfield = AsteroidField()

    def loop(self, dt: float, screen: pygame.display) -> bool:
        for obj in self.updatable:
            obj.update(dt)

        for obj in self.asteroids:
            if obj.collision(self.player):
                print("Game over!")
                return False

        for ast in self.asteroids:
            for bullet in self.shots:
                if ast.collision(bullet):
                    ast.split()
                    bullet.kill()

        for obj in self.drawable:
            obj.draw(screen)

        return True

    def on_end(self):

        for obj in self.updatable:
            obj.kill()

        self.updatable.empty()
        self.drawable.empty()
        self.asteroids.empty()
        self.shots.empty()

        self.updatable = None
        self.drawable = None
        self.asteroids = None
        self.shots = None

        Player.containers = None
        Asteroid.containers = None
        AsteroidField.containers = None
        Shot.containers = None

        super().on_end()
