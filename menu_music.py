
import pygame
pygame.init()
pygame.mixer.init()


def play_sound_effect(sound_file):
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    return sound


def play_background_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)