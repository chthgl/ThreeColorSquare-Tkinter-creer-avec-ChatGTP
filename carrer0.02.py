import random
import pygame

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
window_size = (600, 600)

# Créer la fenêtre d'affichage
screen = pygame.display.set_mode(window_size)

# Définir la taille des pixels
pixel_size = 10

# Définir la couleur bleue
blue = (0, 0, 255)

# Définir la couleur jaune
yellow = (255, 255, 0)

# Définir la couleur violette
purple = (255, 0, 255)

# Créer une liste de pixels bleus
blue_pixels = []
for i in range(50):
    # Générer des coordonnées aléatoires pour le pixel
    x = random.randint(0, window_size[0] - pixel_size)
    y = random.randint(0, window_size[1] - pixel_size)

    # Créer le pixel bleu et l'ajouter à la liste
    blue_pixels.append(pygame.Rect(x, y, pixel_size, pixel_size))

# Créer une liste de pixels jaunes
yellow_pixels = []
for i in range(60):
    # Générer des coordonnées aléatoires pour le pixel
    x = random.randint(0, window_size[0] - pixel_size)
    y = random.randint(0, window_size[1] - pixel_size)

    # Créer le pixel jaune et l'ajouter à la liste
    yellow_pixels.append(pygame.Rect(x, y, pixel_size, pixel_size))

# Définir la vitesse de déplacement des pixels (en pixels par frame)
speed = 5

# Définir la direction des pixels (1 = vers la droite, -1 = vers la gauche)
direction = 1

# Exécuter la boucle principale
while True:
    # Récupérer les événements de la queue
    for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre, quitter le programme
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Effacer l'écran
    screen.fill((0, 0, 0))

    # Déplacer les pixels bleus
    for pixel in blue_pixels:
        # Déplacer le pixel en fonction de la direction et de la vitesse
        pixel.x += direction * speed

        # Si le pixel sort de l'écran, changer sa direction
        if pixel.right > window_size[0] or pixel.left < 0:
            direction *= -1

    # Déplacer les pixels j
