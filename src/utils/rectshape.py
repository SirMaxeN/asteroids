from .shape import Shape


class RectShape(Shape):
    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__(x, y, max(width, height))
        self.width: float = width
        self.height: float = height
