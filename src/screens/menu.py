import pygame
from ..text import Text
from ..state import State
from ..constants import *
from ..stateenum import StateEnum
from ..resources import Resources


class Menu(State):
    def on_start(self):
        super().on_start()

        self.menu_text = []

        start_game = Text("START_GAME",
                          SCREEN_WIDTH/2, SCREEN_HEIGHT/2 , (255, 255, 255), Resources.GAME_FONT_L)
        help = Text("HELP",
                    SCREEN_WIDTH/2, SCREEN_HEIGHT/2+40, (255, 255, 255), Resources.GAME_FONT_L)
        exit_game = Text("EXIT_GAME",
                         SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 80, (255, 255, 255), Resources.GAME_FONT_L)

        self.menu_index = 0
        self.current_text = None
        self.menu_text.append(start_game)
        self.menu_text.append(help)
        self.menu_text.append(exit_game)
        self.set_current_selected()


        self.texts = [
            Text(f"ver {Resources.VERSION}",
                 SCREEN_WIDTH/2 - 570, SCREEN_HEIGHT / 2 + 330, (150, 150, 150), Resources.GAME_FONT_S),
            Text("base game made during boot.dev python course",
                 SCREEN_WIDTH/2 + 383, SCREEN_HEIGHT / 2 + 290, (150, 150, 150), Resources.GAME_FONT_S),
            Text("rest made by Jakub \"SirMaxeN\" Komar",
                 SCREEN_WIDTH/2 + 433, SCREEN_HEIGHT / 2 + 310, (150, 150, 150), Resources.GAME_FONT_S),
            Text("https://github.com/SirMaxeN/asteroids",
                 SCREEN_WIDTH/2 + 420, SCREEN_HEIGHT / 2 + 330, (150, 150, 150), Resources.GAME_FONT_S),
        ]
        
        self.title_text = Resources.title()

    def set_current_selected(self):
        if self.current_text != None:
            s: str = self.current_text.get_text()
            s = s.replace("> ", "")
            s = s.replace(" <", "")
            self.current_text.set_text(s)

        self.current_text = self.menu_text[self.menu_index]
        s: str = self.current_text.get_text()
        self.current_text.set_text(f"> {s} <")

    def loop(self, dt: float, screen: pygame.display, events) -> StateEnum:
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_ESCAPE]:
                    return StateEnum.EXIT
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    self.menu_index += 1
                    self.menu_index %= len(self.menu_text)
                    self.set_current_selected()
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    self.menu_index -= 1
                    self.menu_index %= len(self.menu_text)
                    self.set_current_selected()
                if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                    if self.menu_index == 0:
                        return StateEnum.GAME
                    elif self.menu_index == 1:
                        return StateEnum.HELP
                    elif self.menu_index == 2:
                        return StateEnum.EXIT

        for text in self.menu_text:
            screen.blit(text.get_obj(), text.get_position())
        for text in self.texts:
            screen.blit(text.get_obj(), text.get_position())
        for text in self.title_text:
            screen.blit(text.get_obj(), text.get_position())
            
        return StateEnum.CONTINUE

    def on_end(self):
        while len(self.texts) > 0:
            self.texts.pop().kill()

        self.texts = []

        while len(self.menu_text) > 0:
            self.menu_text.pop().kill()

        self.menu_text = []
        
        while len(self.title_text) > 0:
            self.title_text.pop().kill()

        self.title_text = []
        
        super().on_end()
