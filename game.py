import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager


# class qui represente le jeu
class Game:
    def __init__(self):
        # definir si notre jeu a commencer ou non
        self.is_playing = False
        # generer joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # gerer le son
        self.sound_manager = SoundManager()
        # mettre le score a 0
        self.font = pygame.font.SysFont("monospace", 25)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        # remttre le jeu a neuf
        self.all_monsters = pygame.sprite.Group()   # ecrase le groupe existant en un groupe vierge
        self.comet_event.all_comet = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.sound_manager.play("game_over")

    def update(self, ecran):
        # afficher le score a l'ecran
        score_text = self.font.render(f"score : {self.score}", 1, (0, 0, 0))   # render() = creer un nouveau text
        ecran.blit(score_text, (20, 20))

        # appliquer l'image du joueur
        ecran.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(ecran)

        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(ecran)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # recuperer les projectile du joueur
        for projectile in self.player.all_projectile:
            projectile.move()

        # recupere les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(ecran)
            monster.update_animation()

        # recuperer les cometes du jeu
        for comet in self.comet_event.all_comet:
            comet.fall()

        # appliquer les images du groupe de projectile
        self.player.all_projectile.draw(ecran)  # per met de dessiner sur l'ecran tous les projectile present dans le groupe

        # appliquer l'ensemble des image de mon groupe de monstre

        self.all_monsters.draw(ecran)

        # appliquer l'ensemble des images du groupe de comete
        self.comet_event.all_comet.draw(ecran)

        # verif si on veut aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < ecran.get_width():  # verif si fleche droit est active
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)   # permet de comparer si le sprite rendre en collision avec le groupe de sprite