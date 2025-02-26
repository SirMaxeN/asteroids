import pygame
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .text import Text


class Resources:

    GAME_FONT_XL: pygame.font.Font
    GAME_FONT_L: pygame.font.Font
    GAME_FONT_M: pygame.font.Font
    GAME_FONT_S: pygame.font.Font

    VERSION: str
    SCORE: int

    def __init__(self, version: str):
        Resources.GAME_FONT_XL = pygame.font.Font(
            "assets/fonts/DroidSansMono.ttf", 40)
        Resources.GAME_FONT_L = pygame.font.Font(
            "assets/fonts/DroidSansMono.ttf", 30)
        Resources.GAME_FONT_M = pygame.font.Font(
            "assets/fonts/DroidSansMono.ttf", 24)
        Resources.GAME_FONT_S = pygame.font.Font(
            "assets/fonts/DroidSansMono.ttf", 18)
        Resources.VERSION = version
        Resources.SCORE = 0

    def title():
        pos = 340
        offet = 21
        additionalOffset = 10
        return [
            Text("                     _____ _______ ______ _____   ____ _____ _____             ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - pos, (150, 150, 150), Resources.GAME_FONT_S),
            Text("              /\\    / ____|__   __|  ____|  __ \\ / __ \\_   _|  __ \\            ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos-offet), (150, 150, 150), Resources.GAME_FONT_S),
            Text("             /  \\  | (___    | |  | |__  | |__) | |  | || | | |  ||            ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos-offet*2), (150, 150, 150), Resources.GAME_FONT_S),
            Text("            / /\\ \\  \\___ \\   | |  |  __| |  _  /| |  | || | | |  ||            ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos-offet*3), (150, 150, 150), Resources.GAME_FONT_S),
            Text("           / ____ \\ ____) |  | |  | |____| | \\ \\| |__| || |_| |__||            ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos-offet*4), (150, 150, 150), Resources.GAME_FONT_S),
            Text("          /_/    \\_\\_____/   |_|  |______|_|  \\_\\\\____/_____|_____/            ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos-offet*5), (150, 150, 150), Resources.GAME_FONT_S),
            Text("  ____               __      __         __      __  __                          ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*6), (150, 150, 150), Resources.GAME_FONT_S),
            Text(" |  _ \\             | |     | |        | |     | |/ /                          ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*7), (150, 150, 150), Resources.GAME_FONT_S),
            Text(" | |_) |_   _       | | __ _| | ___   _| |__   | ' / ___  _ __ ___   __ _ _ __ ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*8), (150, 150, 150), Resources.GAME_FONT_S),
            Text(" |  _ <| | | |  _   | |/ _` | |/ / | | | '_ \\  |  < / _ \\| '_ ` _ \\ / _` | '__|",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*9), (150, 150, 150), Resources.GAME_FONT_S),
            Text(" | |_) | |_| | | |__| | (_| |   <| |_| | |_) | | . \\ (_) | | | | | | (_| | |   ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*10), (150, 150, 150), Resources.GAME_FONT_S),
            Text(" |____/ \\__, |  \\____/ \\__,_|_|\\_\\\\__,_|_.__/  |_|\\_\\___/|_| |_| |_|\\__,_|_|   ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*11), (150, 150, 150), Resources.GAME_FONT_S),
            Text("         __/ |                                                                 ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*12), (150, 150, 150), Resources.GAME_FONT_S),
            Text("        |___/                                                                  ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*13), (150, 150, 150), Resources.GAME_FONT_S)]
