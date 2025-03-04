import asyncio
import sys
import platform
import pygame
import pygame.freetype
from src.utils.constants import *
from src.utils.audio import Audio
from src.utils.resources import Resources
from src.utils.statemanager import StateManager
from src.utils.stateenum import StateEnum


class GameLoop:
    async def start(self, version: str):
        pygame.init()
        pygame.mixer.init()
        resources = Resources(version)
        audio = Audio()

        screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)

        clock = pygame.time.Clock()
        dt = 0

        state_manager = StateManager()
        current_state = state_manager.get_state()

        while True:
            keys = pygame.key.get_pressed()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    if sys.platform == "emscripten":
                        platform.window.location.reload()
                        return
                    else:
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
                            if sys.platform == "emscripten":
                                platform.window.location.reload()
                                return
                            else:
                                return
                        current_state = state_manager.change_state(state)

            pygame.display.flip()

            dt = clock.tick(60)/1000

            await asyncio.sleep(0)
