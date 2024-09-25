import pygame
from projectile import Projectile
import animation


# class du joueur
class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__('player')  #charger la superclass pour charger le joueur
        self.game = game
        self.health = 200
        self.max_health = 200
        self.attack = 20
        self.velocity = 3
        self.all_projectile = pygame.sprite.Group()     # ranger dans un groupe
        self.rect = self.image.get_rect()       #get_rect = genere un rectangle pour recup l'image
        self.rect.x = 400   #modifie la position sur l'axe x
        self.rect.y = 500   #modifie la position sur l'axe y

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # dessiner la barre de vie // surface, couleur, [position x, position y, largeur, hauteur]
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 5, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 5, self.rect.y - 20, self.health, 5])      # permet de dessiner un nouveau rectangle

    def lunch_projectile(self):
        # creer une nouvelle instance de la class projectile
        self.all_projectile.add(Projectile(self))
        # demarer l'animation du lance
        self.start_animation()
        # jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
