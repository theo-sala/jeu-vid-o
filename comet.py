import pygame
import random

# class pour gerer la comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir l'image associée a la comete
        self.image = pygame.image.load('Asset/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comet.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        # verifier si le nombre de comete est de 0
        if len(self.comet_event.all_comet) == 0:
            print("event fini")
            # remettre la barre a 0
            self.comet_event.reset_percent()
            # apparaitre les 2 premiere monstres
            self.comet_event.game.start()
    def fall(self):
        self.rect.y += self.velocity

        # elle ne tombe pas sur le sol
        if self.rect.y >= 500:
            # retirer la boule de feu
            self.remove()

            # si il y a plus de bdf sur le jeu
            if len(self.comet_event.all_comet) == 0:
                # remettre jauge de vie au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verifier si la bdf touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("joueur touché")
            # retirer le boule de feu
            self.remove()
            # subire 50 points de degats
            self.comet_event.game.player.damage(50)