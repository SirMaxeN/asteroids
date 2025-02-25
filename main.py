import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                return

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
