import pygame

# definir une classse qui va as'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    #definir lees choses a faire a la creation de l'entité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size  = size
        self.image = pygame.image.load(f'Asset/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0   # commencer l'animation a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une methode pour demarer l'animation
    def start_animation(self):
        self.animation = True

    # definir une mathod pour animé le sprite
    def animate(self, loop=False):

        # verif si l'animation est active
        if self.animation:
            # passer a l'image suivante
            self.current_image += 1

            # verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au depart
                self.current_image = 0

                # verifier si l'animation n'est pas en mode loop
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            # modifier l'image de l'animation precedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)



# definir une fonction pour charger les image d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # recup le chemin du dossier pour ce sprite
    path = f"asset/{sprite_name}/{sprite_name}"

    # boculé sur chaque image de ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'images
    return images

# definir un dictionnaire qui va contenir les images chargés de chaque sprite
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}