import pygame
from .circleshape import CircleShape
from .shot import Shot
from ..constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_ACCELERATION, PLAYER_BRAKING


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cool_down_time = 0
        self.is_moving = False
        self.last_moving_direction = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.display):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float):
        forward = pygame.Vector2(0, self.velocity.y).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt: float):
        self.cool_down_time -= dt

        keys = pygame.key.get_pressed()

        is_moving_direction = 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            is_moving_direction = -1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            is_moving_direction = 1
        if keys[pygame.K_SPACE] and self.cool_down_time <= 0:
            self.shoot()

        if is_moving_direction != 0:
            if is_moving_direction != self.last_moving_direction:
                self.velocity.y = self.velocity.y*-1
            self.velocity.y += PLAYER_ACCELERATION
            if self.velocity.y > 1:
                self.velocity.y = 1
            self.last_moving_direction = is_moving_direction
            self.move(dt * is_moving_direction)
        else:
            if self.velocity.y > 0:
                self.velocity.y -= PLAYER_BRAKING
                self.move(dt * self.last_moving_direction)
            else:
                self.velocity.y = 0

        self.loop_around()

    def shoot(self):
        self.cool_down_time = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(
            self.rotation) * PLAYER_SHOOT_SPEED
