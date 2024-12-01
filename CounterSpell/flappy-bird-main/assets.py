import os
import pygame

# Define the base path
BASE_PATH = r"./flappy-bird-main"

sprites = {}
audios = {}

def load_sprites():
    # Use the absolute path for assets/sprites
    path = os.path.join(BASE_PATH, "assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def get_sprite(name):
    return sprites[name]

def load_audios():
    # Use the absolute path for assets/audios
    path = os.path.join(BASE_PATH, "assets", "audios")
    for file in os.listdir(path):
        audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))

def play_audio(name):
    audios[name].play()
