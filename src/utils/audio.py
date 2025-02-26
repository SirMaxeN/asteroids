import pygame
import random


class Audio:

    SOUND_VOLUME = 1
    MUSIC_VOLUME = 1
    CURRENT_MUSIC_VOLUME = 1

    SOUND_PATH = ""
    MUSIC_PATH = ""

    def __init__(self):

        Audio.SOUND_PATH = "assets/sound/"
        Audio.MUSIC_PATH = "assets/music/"

        Audio.SOUND_VOLUME = 1
        Audio.MUSIC_VOLUME = 1

    def sound_mute_change():
        if Audio.SOUND_VOLUME > 0:
            Audio.SOUND_VOLUME = 0
        else:
            Audio.SOUND_VOLUME = 1

    def music_mute_change():
        if Audio.SOUND_VOLUME > 0:
            Audio.MUSIC_VOLUME = 0
        else:
            Audio.MUSIC_VOLUME = 1
        pygame.mixer.music.set_volume(
            Audio.CURRENT_MUSIC_VOLUME * Audio.MUSIC_VOLUME)

    def play_move(volume):
        pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}move2.wav").play().set_volume(abs(volume) * Audio.SOUND_VOLUME)

    def play_explosion():
        pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}explosion_{random.randint(0, 3)}.wav").play().set_volume(0.2 * Audio.SOUND_VOLUME)

    def play_end():
        pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}end.wav").play().set_volume(0.4 * Audio.SOUND_VOLUME)

    def play_dead():
        pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}dead.wav").play().set_volume(0.2 * Audio.SOUND_VOLUME)

    def play_dead_symth():
        pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}dead_symth.wav").play().set_volume(0.2 * Audio.SOUND_VOLUME)

    def play_shoot():
        pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}shoot_{random.randint(0, 3)}.wav").play().set_volume(0.2 * Audio.SOUND_VOLUME)

    def play_click():
        pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}click.wav").play().set_volume(0.2 * Audio.SOUND_VOLUME)

    def play_enter():
        pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}blip.wav").play().set_volume(0.2 * Audio.SOUND_VOLUME)

    def load_game_music():
        pygame.mixer.music.load(f"{Audio.MUSIC_PATH}game.ogg")
        Audio.CURRENT_MUSIC_VOLUME = 1
        pygame.mixer.music.set_volume(
            Audio.CURRENT_MUSIC_VOLUME * Audio.MUSIC_VOLUME)
        pygame.mixer.music.play(-1, 0, 500)

    def load_menu_music():
        pygame.mixer.music.load(f"{Audio.MUSIC_PATH}menu.ogg")
        Audio.CURRENT_MUSIC_VOLUME = 0.5

        pygame.mixer.music.set_volume(
            Audio.CURRENT_MUSIC_VOLUME * Audio.MUSIC_VOLUME)
        pygame.mixer.music.play(-1, 0, 500)
