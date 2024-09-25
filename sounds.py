import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound('Asset/sounds/click.ogg'),
            "game_over": pygame.mixer.Sound('Asset/sounds/game_over.ogg'),
            "meteorite": pygame.mixer.Sound('Asset/sounds/meteorite.ogg'),
            "tir": pygame.mixer.Sound('Asset/sounds/tir.ogg')
        }

    def play(self, name):
        self.sounds[name].play()    # .play() pour jouer le son