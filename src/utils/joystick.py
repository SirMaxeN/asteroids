import pygame
import math
from .circleshape import CircleShape


class Joystick(CircleShape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius)

        self.__max_distance_from_center = 70
        self.__stick_speed = 14

        self.color = color
        self.rotation = 0
        self.__held = False
        self.zero_position = pygame.Vector2(0, 0)
        self.current_position = pygame.Vector2(0, 0)
        self.stick_position = pygame.Vector2(0, 0)

        self.stick_angle = 0
        self.nomralized_distance = 0


    def is_held(self) -> bool:
        return self.__held

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, self.color,
                           self.position, self.radius, 2)

        pygame.draw.circle(screen, self.color,
                           self.position+self.stick_position, self.radius*0.6, 8)

    def stop_held(self):
        self.__held = False
        self.zero_position.x = 0
        self.zero_position.y = 0
        self.current_position.x = 0
        self.current_position.y = 0
        self.current_position.x = 0
        self.current_position.y = 0

    def register_hold(self, x, y):
        self.__held = True
        self.zero_position.x = x
        self.zero_position.y = y
        self.stick_position.x = 0
        self.stick_position.y = 0
        self.current_position.x = x
        self.current_position.y = y

    def current_pos(self, x, y):
        self.current_position.x = x
        self.current_position.y = y

    def update(self, dt: float):
        pos = self.current_position - self.zero_position

        self.stick_position = self.stick_position.move_towards(
            pos, self.__stick_speed)
        stick_distance_from_center = (
            self.stick_position + self.zero_position).distance_to(self.zero_position)
        if stick_distance_from_center >= self.__max_distance_from_center:
            self.stick_position = self.stick_position.move_towards(
                (0, 0), self.__stick_speed+(self.__stick_speed*0.01))

        self.stick_angle = self.calculate_angle(
            self.stick_position.x, self.stick_position.y)
        self.nomralized_distance = stick_distance_from_center/self.__max_distance_from_center


    def calculate_angle(self, x, y):
        angle_radians = math.atan2(y, x)
        angle_degrees = math.degrees(angle_radians)
        angle_degrees = (angle_degrees + 270) % 360
        return angle_degrees

    def is_pressed(self, x, y) -> bool:
        return self.in_hitbox(x, y)
