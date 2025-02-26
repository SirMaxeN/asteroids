import pygame
import random
from .circleshape import CircleShape
from .constants import PARTICLE_RADIUS


class ParticleAnimation(CircleShape):
    def __init__(self, x, y, radius, color, time_in, time_out, velocity):
        super().__init__(x, y, radius)
        self.time_out = time_out
        self.time_in = time_in
        self.color = color
        self.velocity = velocity

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, (0, 0, 0),
                           self.position, self.radius)
        pygame.draw.circle(screen, self.color,
                           self.position, self.radius, 2)

    def update(self, dt: float):
        self.position += (self.velocity * dt)
        self.time_out -= dt
        if (self.time_out < 0):
            self.kill()
        if self.out_of_bounds():
            self.kill()
