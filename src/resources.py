import pygame


class Resources:

    GAME_FONT: pygame.font.Font

    def __init__(self):
        Resources.GAME_FONT = pygame.font.Font(
            "assets/fonts/DroidSansMono.ttf", 30)
