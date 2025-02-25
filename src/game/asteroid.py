import pygame
import random
from .circleshape import CircleShape
from ..constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_VELOCITY_MULTIPLIER, SCREEN_HEIGHT, SCREEN_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, (255, 255, 255),
                           self.position, self.radius, 2)

    def update(self, dt: float):
        self.position += (self.velocity * dt)

        self.loop_around()

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return

        new_rotation = random.uniform(20, 50)
        self.create_splitted_asteroid(new_rotation)
        self.create_splitted_asteroid(-new_rotation)

    def create_splitted_asteroid(self, rotation):
        new_velocity = self.velocity.rotate(rotation)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_velocity * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
