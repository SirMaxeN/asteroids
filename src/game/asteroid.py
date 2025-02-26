import pygame
import random
from ..utils.circleshape import CircleShape
from ..utils.constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_VELOCITY_MULTIPLIER, SCORE_PER_ASTEROID, ASTEROID_TURN_SPEED
from ..utils.resources import Resources
from ..utils.audio import Audio
from ..utils.particleanimation import ParticleAnimation


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float, type: int):
        super().__init__(x, y, radius)
        self.type = type
        self.shape = self.get_shape()
        self.rotation = random.randint(0, 360)
        self.scale = 0.035
        self.rotation_direction = random.randint(-3, 3)/3

    def rotate(self, dt: float):
        self.rotation += ASTEROID_TURN_SPEED * dt

    def custom_polygon(self):
        output = []
        for i in range(0, len(self.shape), 2):
            output.append(
                self.position - pygame.Vector2(self.shape[i], self.shape[i+1]).rotate(self.rotation) * self.radius * self.scale)
        return output

    def draw(self, screen: pygame.display):
        # pygame.draw.circle(screen, (255, 255, 255),                           self.position, self.radius, 2)
        pygame.draw.polygon(screen, (0, 0, 0), self.custom_polygon())
        pygame.draw.polygon(screen, (255, 255, 255), self.custom_polygon(), 2)

    def update(self, dt: float):
        self.position += (self.velocity * dt)
        self.rotate(dt * self.rotation_direction)

        self.loop_around()

    def split(self):
        Audio.play_explosion()
        self.split_animation()
        self.kill()

        Resources.SCORE += SCORE_PER_ASTEROID * self.type

        if self.radius == ASTEROID_MIN_RADIUS:
            return

        new_rotation = random.uniform(20, 50)
        self.create_splitted_asteroid(new_rotation)
        self.create_splitted_asteroid(-new_rotation)

    def create_splitted_asteroid(self, rotation):
        new_velocity = self.velocity.rotate(rotation)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y,
                            new_radius, self.type - 1)
        asteroid.velocity = new_velocity * ASTEROID_SPLIT_VELOCITY_MULTIPLIER

    def get_shape(self):
        points = [
            [-19.0, -18.5, 1.0, -24.5, 21.0, -18.5, 28.0, 0.5,
                20.0, 21.5, 1.0, 26.5, -19.0, 21.5, -29.0, 1.5],
            [-20.0, -13.5, -12.0, -25.5, 1.0, -20.5, 12.0, -25.5, 20.0, -13.5, 20.0, -2.5, 28.0, 4.5, 26.0, 16.5,
             20.0, 25.5, 3.0, 17.5, 0.0, 30.5, -8.0, 23.5, -20.0, 26.5, -16.0, 13.5, -29.0, 5.5, -25.0, -7.5],
            [-17.0, -16.5, -7.0, -34.5, 4.0, -23.5, 11.0, -23.5, 23.0, -16.5,
             31.0, 2.5, 23.0, 22.5, 3.0, 28.5, -17.0, 23.5, -26.0, 2.5],
            [-18.0, -20.5, -9.0, -24.5, -8.0, -38.5, 3.0, -27.5, 4.0, -14.5, 14.0, -19.5, 22.0, -20.5, 16.0, -10.5,
             30.0, -1.5, 32.0, 10.5, 22.0, 18.5, 13.0, 28.5, 2.0, 24.5, -18.0, 19.5, -30.0, 10.5, -27.0, -1.5],
            [-17.0, -18.5, -11.0, -22.5, -7.0, -25.5, 3.0, -24.5, 13.0, -26.5, 23.0, -18.5, 30.0, 0.5,
             29.0, 15.5, 22.0, 21.5, 3.0, 26.5, -8.0, 26.5, -17.0, 21.5, -27.0, 12.5, -27.0, 1.5],
            [-20.0, -7.5, -14.0, -18.5, -10.0, -20.5, 0.0, -20.5, 10.0, -22.5, 20.0, -14.5, 27.0, 4.5,
             20.0, 15.5, 19.0, 25.5, 0.0, 30.5, -5.0, 26.5, -16.0, 16.5, -30.0, 16.5, -30.0, 5.5],
            [-22.0, -10.5, -16.0, -21.5, -12.0, -23.5, -1.0, -20.5, 8.0, -25.5, 20.0, -12.5, 25.0, 1.5,
             21.0, 10.5, 17.0, 22.5, -2.0, 27.5, -7.0, 23.5, -18.0, 13.5, -21.0, 1.5, -28.0, -1.5]
        ]
        index = random.randint(0, len(points)-1)
        return points[index]

    def split_animation(self):
        for i in range(1, 200):
            ParticleAnimation(self.position.x, self.position.y, 2, (255, 255, 255), 0, random.uniform(0.8,1.5),
                              pygame.Vector2(0, 1).rotate(
                self.rotation + i * 5.4) * (random.uniform(10, 80))
            )
