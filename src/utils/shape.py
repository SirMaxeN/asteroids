import pygame
from .constants import SCREEN_HEIGHT, SCREEN_WIDTH

# Base class for game objects


class Shape(pygame.sprite.Sprite):
    offset = 20

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

    def collision(self, shape) -> bool:
        distance = self.position.distance_to(shape.position)
        return distance <= self.radius + shape.radius

    def out_of_bounds(self):
        return (
            self.position.y < -self.radius - Shape.offset or
            self.position.y > SCREEN_HEIGHT + self.radius + Shape.offset or
            self.position.x < -self.radius - Shape.offset or
            self.position.x > SCREEN_WIDTH + self.radius + Shape.offset
        )

    def loop_around(self, additonal_offset=0) -> bool:
        if self.position.y < -self.radius - Shape.offset - additonal_offset:
            self.position.y = SCREEN_HEIGHT + self.radius + \
                Shape.offset + additonal_offset
            return True
        elif self.position.y > SCREEN_HEIGHT + self.radius + Shape.offset + additonal_offset:
            self.position.y = -self.radius - Shape.offset - additonal_offset
            return True
        elif self.position.x < -self.radius - Shape.offset - additonal_offset:
            self.position.x = SCREEN_WIDTH + self.radius + \
                Shape.offset + additonal_offset
            return True
        elif self.position.x > SCREEN_WIDTH + self.radius + Shape.offset + additonal_offset:
            self.position.x = -self.radius - Shape.offset - additonal_offset
            return True
        return False
