from enum import Enum


class State(Enum):
    MENU = 0,
    START = 1,
    CONTINUE = 2,
    CHOOSE_THEME = 3,
    CHOOSE_HERO = 4,
    LEVEL_2 = 5,
    QUIT = 6


class GameState:
    def __init__(self):
        self.state = State.MENU

    def change(self, state):
        self.state = state

    def check(self, state):
        if self.state == state:
            return True
        return False
