import pygame
import random
from ..utils.circleshape import CircleShape
from ..utils.constants import PARTICLE_RADIUS


class ParticleEngine(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PARTICLE_RADIUS)
        self.timer = 0.06

    def draw(self, screen: pygame.display):
        color = [(255, 212, 212), (255, 222, 212), (255, 230, 212),
                 (255, 236, 212), (255, 244, 212), (255, 251, 212), (255, 255, 212)][random.randint(0, 6)]
        if (self.timer < 0.025):
            pygame.draw.circle(screen, color,
                               self.position, self.radius, 2)

    def update(self, dt: float):
        self.position += (self.velocity * dt)
        self.timer -= dt
        if (self.timer < 0):
            self.kill()
        if self.out_of_bounds():
            self.kill()
