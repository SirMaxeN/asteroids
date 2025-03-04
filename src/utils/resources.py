import pygame
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .text import Text


class Resources:

    FONT_XL: pygame.font.Font
    FONT_L: pygame.font.Font
    FONT_M: pygame.font.Font
    FONT_S: pygame.font.Font

    VERSION: str
    SCORE: int

    def __init__(self, version: str):

        Resources.FONT_XL = pygame.font.Font(
            "assets/font/DroidSansMono.ttf", 40)
        Resources.FONT_L = pygame.font.Font(
            "assets/font/DroidSansMono.ttf", 30)
        Resources.FONT_M = pygame.font.Font(
            "assets/font/DroidSansMono.ttf", 24)
        Resources.FONT_S = pygame.font.Font(
            "assets/font/DroidSansMono.ttf", 18)
        Resources.VERSION = version
        Resources.SCORE = 0

    def credits(color: int):
        return [
            Text("made by Jakub \"SirMaxeN\" Komar",
                 SCREEN_WIDTH/2 + 460, SCREEN_HEIGHT / 2 + 290, (color, color, color), Resources.FONT_S),
            Text("using pygame 2.6.1, web version pygbag 0.9.2",
                 SCREEN_WIDTH/2 + 380, SCREEN_HEIGHT / 2 + 310, (color, color, color), Resources.FONT_S),
            Text("https://github.com/SirMaxeN/asteroids",
                 SCREEN_WIDTH/2 + 420, SCREEN_HEIGHT / 2 + 330, (color, color, color), Resources.FONT_S),
        ]

    def version(color: int):
        return [
            Text(f"ver {Resources.VERSION}",
                 SCREEN_WIDTH/2 - 570, SCREEN_HEIGHT / 2 + 330, (color, color, color), Resources.FONT_S),
        ]

    def title(color: int):
        pos = 340
        offet = 21
        additionalOffset = 10
        return [
            Text("                    _____ _______ ______ _____   ____ _____ _____  _____           ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - pos, (color, color, color), Resources.FONT_S),
            Text("            /\\    / ____|__   __|  ____|  __ \\ / __ \\_   _|  __ \\/ ____|         ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos-offet), (color, color, color), Resources.FONT_S),
            Text("         /  \\  | (___    | |  | |__  | |__) | |  | || | | |  || (___         ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos-offet*2), (color, color, color), Resources.FONT_S),
            Text("         / /\\ \\  \\___ \\   | |  |  __| |  _  /| |  | || | | |  ||\\___ \\         ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos-offet*3), (color, color, color), Resources.FONT_S),
            Text("         / ____ \\ ____)|   | |  | |____| | \\ \\| |__| || |_| |__||____)|          ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos-offet*4), (color, color, color), Resources.FONT_S),
            Text("        /_/    \\_\\_____/   |_|  |______|_|  \\_\\\\____/_____|_____/_____/          ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos-offet*5), (color, color, color), Resources.FONT_S),
            Text("  ____               __      __         __      __  __                          ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*6), (color, color, color), Resources.FONT_S),
            Text(" |  _ \\             | |     | |        | |     | |/ /                          ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*7), (color, color, color), Resources.FONT_S),
            Text(" | |_) |_   _       | | __ _| | ___   _| |__   | ' / ___  _ __ ___   __ _ _ __ ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*8), (color, color, color), Resources.FONT_S),
            Text(" |  _ <| | | |  _   | |/ _` | |/ / | | | '_ \\  |  < / _ \\| '_ ` _ \\ / _` | '__|",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*9), (color, color, color), Resources.FONT_S),
            Text(" | |_) | |_| | | |__| | (_| |   <| |_| | |_) | | . \\ (_) | | | | | | (_| | |   ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*10), (color, color, color), Resources.FONT_S),
            Text(" |____/ \\__, |  \\____/ \\__,_|_|\\_\\\\__,_|_.__/  |_|\\_\\___/|_| |_| |_|\\__,_|_|   ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*11), (color, color, color), Resources.FONT_S),
            Text("         __/ |                                                                 ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*12), (color, color, color), Resources.FONT_S),
            Text("        |___/                                                                  ",
                 SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - (pos - additionalOffset - offet*13), (color, color, color), Resources.FONT_S)]
