import pygame
import random
from .asteroid import Asteroid
from ..constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_VELOCITY_MULTIPLIER, SCORE_PER_ASTEROID
from ..resources import Resources


class AsteroidFake(Asteroid):

    def __init__(self, x, y, radius, type, color, scale):
        super().__init__(x, y, radius, type)
        self.scale = scale
        self.color = color

    def draw(self, screen: pygame.display):
        # pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        pygame.draw.polygon(screen, self.color, self.custom_polygon(), 3)
