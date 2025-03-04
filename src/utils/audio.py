import pygame
import random


class Audio:

    SOUND_VOLUME = 1
    MUSIC_VOLUME = 1
    CURRENT_MUSIC_VOLUME = 1

    SOUND_PATH = ""
    MUSIC_PATH = ""

    __CURRENT_CHANNEL = 0

    def __init__(self):

        Audio.SOUND_PATH = "assets/sound/"
        Audio.MUSIC_PATH = "assets/music/"

        Audio.SOUND_VOLUME = 1
        Audio.MUSIC_VOLUME = 1

        Audio.__CURRENT_CHANNEL = 0

        pygame.mixer.set_num_channels(50)

    def __get_channel():
        Audio.__CURRENT_CHANNEL += 1
        if Audio.__CURRENT_CHANNEL > 49:
            Audio.__CURRENT_CHANNEL = 1
        return pygame.mixer.Channel(Audio.__CURRENT_CHANNEL)

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
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}move2.ogg")
        sound.set_volume(abs(volume) * Audio.SOUND_VOLUME)
        Audio.__get_channel().play(sound)

    def play_explosion():
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}explosion_{random.randint(0, 3)}.ogg")
        sound.set_volume(0.2 * Audio.SOUND_VOLUME)
        Audio.__get_channel().play(sound)

    def play_end():
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}end.ogg")
        sound.set_volume(0.4 * Audio.SOUND_VOLUME)
        Audio.__get_channel().play(sound)

    def play_dead():
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}dead.ogg")
        sound.set_volume(0.2 * Audio.SOUND_VOLUME)
        Audio.__get_channel().play(sound)

    def play_dead_symth():
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}dead_symth.ogg")
        sound.set_volume(0.2 * Audio.SOUND_VOLUME)
        Audio.__get_channel().play(sound)

    def play_boost():
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}boost.ogg")
        sound.set_volume(0.4 * Audio.SOUND_VOLUME)
        Audio.__get_channel().play(sound)

    def play_boost_shot():
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}boost_shot.ogg")
        sound.set_volume(0.4 * Audio.SOUND_VOLUME)
        Audio.__get_channel().play(sound)

    def play_boost_bomb():
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}boost_bomb.ogg")
        sound.set_volume(0.4 * Audio.SOUND_VOLUME)
        Audio.__get_channel().play(sound)

    def play_shoot():
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}shoot_{random.randint(0, 3)}.ogg")
        sound.set_volume(0.2 * Audio.SOUND_VOLUME)

        Audio.__get_channel().play(sound)

    def play_click():
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}click.ogg")
        sound.set_volume(0.2 * Audio.SOUND_VOLUME)
        Audio.__get_channel().play(sound)

    def play_enter():
        sound = pygame.mixer.Sound(
            f"{Audio.SOUND_PATH}blip.ogg")
        sound.set_volume(0.2 * Audio.SOUND_VOLUME)
        Audio.__get_channel().play(sound)

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
