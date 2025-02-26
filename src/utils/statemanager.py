from ..screens.game import Game
from ..screens.menu import Menu
from ..screens.help import Help
from ..screens.score import Score
from .state import State
from .stateenum import StateEnum
from .audio import Audio


class StateManager:
    def __init__(self):

        self.game = Game()
        self.menu = Menu()
        self.help = Help()
        self.score = Score()

        self.current_state: State = self.menu
        Audio.load_menu_music()

    def get_state(self) -> State:
        return self.current_state

    def change_state(self, state: StateEnum) -> State:
        if state == StateEnum.GAME:
            self.current_state = self.game
            Audio.load_game_music()
        elif state == StateEnum.SCORE:
            self.current_state = self.score
            Audio.load_menu_music()
        elif state == StateEnum.HELP:
            self.current_state = self.help
        elif state == StateEnum.MENU:
            self.current_state = self.menu

        return self.current_state
