import pygame
import random
from ..utils.rectshape import RectShape
from ..utils.constants import PLANET_SPEED


class RectParticle(RectShape):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color
        self.random_speed = random.uniform(1, 2)

    def draw(self, screen: pygame.display):
        pygame.draw.rect(screen, self.color,
                         (self.position.x, self.position.y, self.width, self.height), 2)

    def update(self, dt: float):
        self.position += (self.velocity * dt * PLANET_SPEED *
                          1.3 * self.random_speed)
        if self.out_of_bounds():
            self.kill()
