
from .asteroidfield import AsteroidField
from .asteroidfake import AsteroidFake


class AsteroidFieldFake(AsteroidField):
    def __init__(self, color, scale):
        super().__init__()
        self.spawn_rate = 0.3
        self.limit = 10
        self.color = color
        self.scale = scale

    def spawn(self, radius, position, velocity, kind):
        asteroid = AsteroidFake(position.x, position.y,
                                radius, kind, self.color, self.scale)
        asteroid.velocity = velocity
