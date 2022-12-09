import random
import math

from tkinter import Tk, Canvas

# Définition des constantes
N_SQUARES = 100
R_SQUARES = 100
SQUARE_SIZE = 10  # en pixels
MAX_SPEED = 7  # en pixels/frame

# Création de la fenêtre
root = Tk()
root.title("Déplacement aléatoire de carrés")

# Création du canevas
canvas = Canvas(root, width=800, height=600)
canvas.pack()

# Création des carrés
squares = []
for i in range(N_SQUARES):
    x1 = random.randint(0, 800 - SQUARE_SIZE)
    y1 = random.randint(0, 600 - SQUARE_SIZE)
    x2 = x1 + SQUARE_SIZE
    y2 = y1 + SQUARE_SIZE
    square = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    squares.append(square)
for i in range(R_SQUARES):
    x1 = random.randint(0, 800 - SQUARE_SIZE)
    y1 = random.randint(0, 600 - SQUARE_SIZE)
    x2 = x1 + SQUARE_SIZE
    y2 = y1 + SQUARE_SIZE
    square = canvas.create_rectangle(x1, y1, x2, y2, fill="red")
    squares.append(square)

# Initialisation des vecteurs de vitesse des carrés
speeds = []
for i in range(N_SQUARES):
    speed = random.uniform(0, MAX_SPEED)
    direction = random.uniform(0, 2 * math.pi)
    dx = speed * math.cos(direction)
    dy = speed * math.sin(direction)
    speeds.append((dx, dy))
for i in range(R_SQUARES):
    speed = random.uniform(0, MAX_SPEED)
    direction = random.uniform(0, 2 * math.pi)
    dx = speed * math.cos(direction)
    dy = speed * math.sin(direction)
    speeds.append((dx, dy))
# Déplacement aléatoire des carrés
while True:
    for i, square in enumerate(squares):
        dx, dy = speeds[i]
        canvas.move(square, dx, dy)

        # Vérification des limites de la fenêtre et rebond si nécessaire
        x1, y1, x2, y2 = canvas.coords(square)
        if x1 < 0 or x2 > 800 or y1 < 0 or y2 > 600:
            # remise à l'intérieur de la fenêtre
            if x1 < 0:
                dx = -x1
            elif x2 > 800:
                dx = 800 - x2
            else:
                dx = 0

            if y1 < 0:
                dy = -y1
            elif y2 > 600:
                dy = 600 - y2
            else:
                dy = 0

            canvas.move(square, dx, dy)

            # inversion du sens pour le rebond
            dx, dy = speeds[i]
            if x1 < 0 or x2 > 800:
                dx = -dx
            if y1 < 0 or y2 > 600:
                dy = -dy

            speeds[i] = (dx, dy)

    # Mise à jour de l'affichage
    root.update()
