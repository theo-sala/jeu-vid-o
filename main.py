import pygame
import math
from game import Game
pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60

#generer la fenetre de jeu
pygame.display.set_caption("Comet fall Game")
ecran = pygame.display.set_mode((1080, 720))

running = True

# importation le background
background = pygame.image.load('Asset/bg.jpg')     #charge une image

# importer charger notre banierre
banner = pygame.image.load('Asset/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(ecran.get_width() / 4)    # arrondie a l'entier pres (math.ceil)

# importer charger le bouton pour lancer a partie
play_button = pygame.image.load('Asset/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))     # redimensionne l'image
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(ecran.get_width() / 3.33)
play_button_rect.y = math.ceil(ecran.get_height() / 2)


# charger le jeu
game = Game()

#boucle tant que running == True
while running == True:

    #appliquer l'arriere plan
    ecran.blit(background, (0, -200))  #applique l'image avec ecran.blit()  /  les parametre gerent la position de l'image

    # verif si le jeu a commencer ou non
    if game.is_playing:
        # declancher lees instructions de la partie
        game.update(ecran)
    # verifier si le jeu n'a pas commencer
    else:
        # ajouter l'ecran de bienvenue
        ecran.blit(play_button, play_button_rect)
        ecran.blit(banner, banner_rect)

    # mettre a jour l'ecran
    pygame.display.flip()   #met a jour la fenettre

    #fermetture
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #event.type recupere le type d'evenement
            running = False
            pygame.quit()
            print("fermetture du jeu")

        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True      #prendre la methode pressed dans game

            # detecter si la touche espace est enfoncée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.lunch_projectile()
                else:
                    # mettre le jeu en mode lancé
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:  # MOUSEBUTTONDOWN = clicl souris
            # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):   # verifier si le bouton possede un point correspondant a la position de la souris au moment du clique
                # mettre le jeu en mode lancé
                game.start()
                # jouer le son
                game.sound_manager.play('click')

    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)