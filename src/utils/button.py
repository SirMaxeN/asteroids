import pygame
from .circleshape import CircleShape


class Button(CircleShape):
    def __init__(self, x, y, radius, type: str, color):
        super().__init__(x, y, radius)
        self.scale = 1
        self.lock_timer = 1
        self.type = type
        self.color = color
        self._icon_lists = None
        self.rotation = 0
        self.toggle = False
        self.active = False

    def set_icon(self, icon_lists, icon_scale: float, icon_offset_x: float, icon_offset_y: float, icon_rotation: int):
        self._icon_lists = icon_lists
        self._icon_scale: float = icon_scale
        self._icon_offset_x: float = icon_offset_x
        self._icon_offset_y: float = icon_offset_y
        self._icon_rotation: int = icon_rotation
        return self

    def draw(self, screen: pygame.display):
        color = self.color
        if self.toggle == True or self.active == True:
            color = (100, 255, 100)

        pygame.draw.circle(screen, color,
                           self.position, self.radius*self.scale, 2)
        if self._icon_lists != None:
            for icon in self._icon_lists:
                pygame.draw.polygon(screen, (0, 0, 0),
                                    self.custom_polygon(icon, self._icon_scale * self.scale, self._icon_rotation, (self._icon_offset_x, self._icon_offset_y)), 2)
                pygame.draw.polygon(screen, color,
                                    self.custom_polygon(icon, self._icon_scale * self.scale, self._icon_rotation, (self._icon_offset_x, self._icon_offset_y)), 2)

    def update(self, dt: float):
        if self.scale < 1:
            self.scale += dt
        else:
            self.scale = 1

        if self.lock_timer < 1:
            self.lock_timer += dt
        else:
            self.lock_timer = 1

    def is_pressed(self, x, y) -> bool:
        if self.lock_timer < 1:
            return False
        if self.in_hitbox(x, y):
            self.scale = 0.9
            self.lock_timer = 0.8
            return True
        return False
