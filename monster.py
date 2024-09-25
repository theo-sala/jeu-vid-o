import pygame
import random
import animation

# class qui gere la notion de monstre
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)      # appel de la superclass
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300) # peut apparaitre entre 1000 et 1300
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, self.default_speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        self.health -= amount

        # verifier si son nouveau nombre d'hp est inferieur ou egal a 0
        if self.health <= 0:
            # reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health
            # ajouter le nombre de point au score
            self.game.add_score(self.loot_amount)

        # si la barre d'evenement est chargée au max
        if self.game.comet_event.is_full_loaded():
            # retirer du jeu
            self.game.all_monsters.remove(self)

            # appel de la method pour essayer de declancher la pluie
            self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # dessiner la barre de vie // surface, couleur, [position x, position y, largeur, hauteur]
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (255, 0, 51), [self.rect.x + 10, self.rect.y - 20, self.health, 5])      # permet de dessiner un nouveau rectangle

    def forward(self):
        # le deplacement ne se fait que si il n'y a pas de collision avec un groupe joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des degats au joueur
            self.game.player.damage(self.attack)

# definir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, 'mummy', (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)
        
# definir une classe pour l'alienne
class Alien(Monster):
    
    def __init__(self, game):
        super().__init__(game, 'alien', (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.5
        self.set_speed(1)
        self.set_loot_amount(50)