import pygame
from ..utils.circleshape import CircleShape
from ..utils.constants import SHOT_RADIUS
from ..utils.audio import Audio


class Boost(CircleShape):
    def __init__(self, x, y, radius, type):
        super().__init__(x, y, radius)
        Audio.play_boost()
        self.type = type
        self.rotation = 0

    def custom_polygon(self, points, scale, rotation, offset):
        output = []
        for i in range(0, len(points), 2):
            output.append(
                self.position - pygame.Vector2(points[i] + offset[0], points[i+1] + offset[1]).rotate(rotation).rotate(self.rotation) * (self.radius * scale))
        return output

    def collect(self):
        self.kill()
