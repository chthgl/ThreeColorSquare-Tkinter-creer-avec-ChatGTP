# -*- coding: utf-8 -*-
import tkinter as tk
from random import randint
class Square:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.dx = 1 # déplacement en x
        self.dy = 1 # déplacement en y
        self.color = color
        self.rect = canvas.create_rectangle(self.x, self.y, self.x + SIZE, self.y + SIZE, fill=self.color)

    def move(self):
        # Vérifie si le carré touche un bord de la fenêtre
        if self.x + SIZE >= WIDTH or self.x <= 0:
            self.dx *= -1
        if self.y + SIZE >= HEIGHT or self.y <= 0:
            self.dy *= -1

        # Déplacement du carré
        self.x += self.dx
        self.y += self.dy
        canvas.move(self.rect, self.dx, self.dy)
        canvas.bind("<Motion>", self.on_mouse_move)
    def on_mouse_move(self, event):
        # Récupère la position actuelle de la souris
        mouse_x = event.x
        mouse_y = event.y

        # Pour chaque carré
        for square in squares:
            # Si la souris est à côté du carré (à une distance inférieure à la moitié de la taille du carré)
            if (abs(square.x - mouse_x) < SIZE/2 and abs(square.y - mouse_y) < SIZE/2):
                # On inverse la direction de déplacement du carré
                square.dx *= -1
                square.dy *= -1

    # Ajout d'une fonction pour changer la couleur d'un carré
    def change_color(self, color):
        self.color = color
        canvas.itemconfig(self.rect, fill=color)

    # Ajout d'une fonction pour détecter les collisions entre les carrés
    def detect_collision(self, other_square):
        # Vérifie si les carrés se chevauchent
        if (self.x < other_square.x + SIZE and self.x + SIZE > other_square.x and
            self.y < other_square.y + SIZE and self.y + SIZE > other_square.y):
            if self.color == "green" and other_square.color == "green":
                self.change_color("black")
                other_square.change_color("black")
            elif self.color == "yellow" and other_square.color == "yellow":
                self.change_color("black")
                other_square.change_color("black")
            elif self.color == "red" and other_square.color == "red":
                self.change_color("black")
                other_square.change_color("black")
            # Inverse la direction de déplacement des deux carrés
            self.dx *= -1
            self.dy *= -1
            other_square.dx *= -1
            other_square.dy *= -1

            # Change la couleur des carrés en fonction de leur couleur actuelle
 


# Définition des constantes
SIZE = 5 # taille des carrés en pixels
speedrand = randint(15, 40)
SPEED = speedrand # vitesse de déplacement en ms
COLORS = ["green", "yellow", "red"] # couleurs des carrés

# Création de la fenêtre principale
window = tk.Tk()
window.title("Carrés")

# Création du canvas
WIDTH = 500
HEIGHT = 500
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# Création des carrés
squares = []
for j in range(15):
    for i in range(3):
        x = randint(0, WIDTH-SIZE)
        y = randint(0, HEIGHT-SIZE)
        color = COLORS[i]
        squares.append(Square(x, y, color))

# Ajout de trois carrés supplémentaires
squares.append(Square(0, 0, "blue"))
squares.append(Square(WIDTH-SIZE, 0, "purple"))
squares.append(Square(0, HEIGHT-SIZE, "orange"))

# Fonction appelée régulièrement pour mettre à jour l'affichage
def update():
    for square in squares:
        square.move()

        # Détecte les collisions entre les carrés
        for other_square in squares:
            if square != other_square:
                square.detect_collision(other_square)

    # Appel de la fonction pour mettre à jour l'affichage
    window.after(SPEED, update)
# Appel de la fonction pour mettre à jour l'affichage
update()

# Affichage de la fenêtre
window.mainloop()