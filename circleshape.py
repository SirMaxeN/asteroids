import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from typing import Type

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: pygame.display):
        # sub-classes must override
        pass

    def update(self, dt: float):
        # sub-classes must override
        pass

    def collision(self, circle) -> bool:
        distance = self.position.distance_to(circle.position)
        return distance <= self.radius + circle.radius

    def out_of_bounds(self):
        return (
            self.position.y < -self.radius or
            self.position.y > SCREEN_HEIGHT + self.radius or
            self.position.x < -self.radius or
            self.position.x > SCREEN_WIDTH + self.radius
        )

    def loop_around(self):
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius
        elif self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
