from .game.game import Game
from .menu.menu import Menu
from .state import State


class StateManager:
    def __init__(self):

        self.game = Game()
        self.menu = Menu()

        self.current_state: State = self.menu

    def get_state(self) -> State:
        return self.current_state

    def change_state(self) -> State:
        if self.current_state == self.menu:
            self.current_state = self.game
        elif self.current_state == self.game:
            self.current_state = self.menu

        return self.current_state
