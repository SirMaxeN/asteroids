import pygame
from .asteroid import Asteroid


class AsteroidFake(Asteroid):

    def __init__(self, x, y, radius, type, color, scale):
        super().__init__(x, y, radius, type)
        self.scale = scale
        self.color = color

    def draw(self, screen: pygame.display):
        # pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        pygame.draw.polygon(screen, (0, 0, 0), self.custom_polygon())
        pygame.draw.polygon(screen, self.color, self.custom_polygon(), 3)
