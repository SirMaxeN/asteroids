import pygame
import random
from .asteroid import Asteroid
from ..utils.constants import *


class AsteroidField(pygame.sprite.Sprite):
    offset = 30
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS - AsteroidField.offset,
                                     y * SCREEN_HEIGHT + AsteroidField.offset),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS + AsteroidField.offset, y *
                SCREEN_HEIGHT + AsteroidField.offset
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH + AsteroidField.offset, -ASTEROID_MAX_RADIUS - AsteroidField.offset),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH + AsteroidField.offset, SCREEN_HEIGHT +
                ASTEROID_MAX_RADIUS + AsteroidField.offset
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.spawn_rate = ASTEROID_SPAWN_RATE
        self.limit = ASTEROID_MAX_PER_SCREEN

    def spawn(self, radius, position, velocity, kind):
        asteroid = Asteroid(position.x, position.y, radius, kind)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > self.spawn_rate and len(Asteroid.containers) > 0 and len(Asteroid.containers[0]) < self.limit:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity, kind)
