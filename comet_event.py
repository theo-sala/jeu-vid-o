import pygame
from comet import Comet

# creer une classe pour gerer cet evenement
class CometFallEvent:

    # lors du chargement -> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 2
        self.game = game
        self.fall_mode = False

        # definir un groupe de sprite pour stocker les comet
        self.all_comet = pygame.sprite.Group()
    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour les valeurs entre 1 et 10
        for i in range(1, 10):
            # apparaitre une premiere boule de feu
            self.all_comet.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'event est totalement charge
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de Cometes !")
            self.meteor_fall()
            self.fall_mode = True   # activer l'evenement

    def update_bar(self, surface):

        # ajouter du pourcentage a la barre
        self.add_percent()

        # la barre noir (arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # axe x
            surface.get_height() - 40, # axe y
            surface.get_width(), # longueur
            10 # epaisseur
        ])
        # barre violette (jauge d'evenement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # axe x
            surface.get_height() - 40, # axe y
            (surface.get_width() / 100) * self.percent, # longueur
            10 # epaisseur
        ])