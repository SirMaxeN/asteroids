import pygame
from ..utils.circleshape import CircleShape
from ..utils.constants import SHOT_RADIUS
from ..utils.audio import Audio


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        Audio.play_shoot()

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, (212, 213, 255),
                           self.position, self.radius, 2)

    def update(self, dt: float):
        self.position += (self.velocity * dt)
        if self.out_of_bounds():
            self.kill()
