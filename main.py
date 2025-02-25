import pygame
import pygame.freetype
from src.constants import *
from src.resources import Resources
from src.statemanager import StateManager


VERSION = "1.0.3"


def version():
    print(f"Asteroid game ver {VERSION}")


def main():
    version()
    pygame.init()

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)

    clock = pygame.time.Clock()
    dt = 0

    state_manager = StateManager()
    resources = Resources()
    current_state = state_manager.get_state()

    while True:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        if current_state:
            if current_state.is_started() == False:
                current_state.on_start()
            else:
                if current_state.loop(dt, screen) == False:
                    current_state.on_end()
                    current_state = state_manager.change_state()

        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
