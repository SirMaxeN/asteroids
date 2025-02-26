import pygame
import pygame.freetype
from src.constants import *
from src.resources import Resources
from src.statemanager import StateManager
from src.stateenum import StateEnum


VERSION = "1.0.4"


def version():
    print(f"Asteroid game ver {VERSION}")


def main():
    version()
    pygame.init()

    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SHOWN)

    clock = pygame.time.Clock()
    dt = 0

    state_manager = StateManager()
    resources = Resources(VERSION)
    current_state = state_manager.get_state()

    while True:
        keys = pygame.key.get_pressed()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        if current_state:
            if current_state.is_started() == False:
                current_state.on_start()
            else:
                state = current_state.loop(dt, screen, events)
                if state != StateEnum.CONTINUE:
                    current_state.on_end()
                    if state == StateEnum.EXIT:
                        return
                    current_state = state_manager.change_state(state)

        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
