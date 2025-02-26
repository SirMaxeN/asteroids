import pygame
import random
from ..utils.circleshape import CircleShape
from .shot import Shot
from .particleengine import ParticleEngine
from ..utils.constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_ACCELERATION, PLAYER_BRAKING, PARTICLE_SPEED
from ..utils.particleanimation import ParticleAnimation
from ..utils.audio import Audio


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cool_down_time = 0
        self.is_moving = False
        self.last_moving_direction = 0
        self.sound_timer = 0

    def custom_polygon(self):
        points = [(-150, -146), (-46, -642), (-38, -649), (-38, -655), (-30, -655), (-29, -647), (-24, -647), (-22, -641), (-22, -459), (-10, -439), (-10, -366), (-4, -367), (-3, -393), (10, -393), (11, -367), (17, -366), (17, -439), (28, -459), (28, -640), (30, -647), (35, -647), (36, -654), (44, -654), (44, -648), (53, -641), (157, -133), (219, -15), (234, 162), (224, 197), (206, 205), (218, 350), (255, 365), (258, 440), (136, 533), (140, 605), (134, 604), (133, 598), (124, 587),
                  (123, 605), (105, 612), (106, 626), (93, 629), (92, 633), (81, 633), (80, 628), (65, 624), (65, 594), (43, 594), (41, 644), (32, 646), (14, 657), (-3, 657), (-17, 646), (-28, 644), (-30, 593), (-52, 593), (-53, 625), (-67, 630), (-68, 634), (-79, 634), (-80, 630), (-93, 627), (-94, 611), (-111, 604), (-112, 586), (-121, 596), (-122, 604), (-126, 605), (-128, 531), (-246, 440), (-245.71093786521217, 366.6716985471187), (-207, 351), (-195, 202), (-214, 197), (-219, 169), (-209, -17)]
        scale = 0.04
        output = []
        for i in points:
            output.append(
                self.position - pygame.Vector2(i[0], i[1]).rotate(self.rotation) * scale)
        return output

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.display):
        pygame.draw.polygon(screen, (0, 0, 0), self.custom_polygon())
        pygame.draw.polygon(screen, (255, 255, 255), self.custom_polygon(), 2)

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float):
        forward = pygame.Vector2(0, self.velocity.y).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.spawn_particles()
        if self.sound_timer > 0.2:
            self.sound_timer=0
            Audio.play_move(self.velocity.y*0.11)

    def update(self, dt: float):
        self.cool_down_time -= dt
        self.sound_timer += dt
        
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
        if (keys[pygame.K_SPACE] or keys[pygame.K_m]) and self.cool_down_time <= 0:
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

    def spawn_particles(self):
        for i in range(1, 10):
            self.particle(i)
        for i in range(-10, -1):
            self.particle(i)

    def particle(self, index: int):

        if self.velocity.y > 0.5:
            particle = ParticleEngine(self.position.x,
                                      self.position.y)
            particle.velocity = pygame.Vector2(0, self.velocity.y*-0.6).rotate(
                self.rotation + index * 8) * PARTICLE_SPEED
            
    def dead(self):
        self.kill()
        for i in range(1, 100):
            ParticleAnimation(self.position.x, self.position.y, 2, (255, 255, 255), 0, random.uniform(0.4,1),
                              pygame.Vector2(0, 1).rotate(
                self.rotation + i * 5.4) * (random.uniform(4, 40))
            )
