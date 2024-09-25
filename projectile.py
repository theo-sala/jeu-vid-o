import pygame

# definir la classe qui gere le projectile
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('Asset/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))   # transform.scale permet de redimenssioner image
        self.rect = self.image.get_rect()   #enere un rectangle pour recup l'image
        self.rect.x = player.rect.x + 120   # recup les coordonnée du joueur
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image      # garde l'image d'originie
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)   # recuper le centre de l'image

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verif si le projectile entre en collision avec un groupe de sprite monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()
            # infliger les degats
            monster.damage(self.player.attack)

        # verif si le projectile n'est plus present sur l'ecran
        if self.rect.x > 1080:
            # supprimer le projectile
            self.remove()
