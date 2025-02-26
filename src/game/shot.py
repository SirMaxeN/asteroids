import pygame
from .circleshape import CircleShape
from ..constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, (212, 213, 255),
                           self.position, self.radius, 2)

    def update(self, dt: float):
        self.position += (self.velocity * dt)
        if self.out_of_bounds():
            self.kill()
