import random
import math
import sys
from tkinter import Tk, Canvas
sys.setrecursionlimit(5000)

class Window:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)

    def add_canvas(self, canvas):
        self.canvas = canvas
        self.canvas.pack()

    def update(self):
        self.root.update()
class Canvas:
    def __init__(self, width, height):
        self.canvas = Canvas(width=width, height=height)

    def create_square(self, x1, y1, x2, y2, fill):
        square = self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill)
        return square

    def move(self, square, dx, dy):
        self.canvas.move(square, dx, dy)

    def coords(self, square):
        return self.canvas.coords(square)

class Square:
    def __init__(self, canvas, x1, y1, x2, y2, fill):
        self.square = canvas.create_square(x1, y1, x2, y2, fill)
        self.speed = random.uniform(0, MAX_SPEED)
        self.direction = random.uniform(0, 2 * math.pi)
        self.dx = self.speed * math.cos(self.direction)
        self.dy = self.speed * math.sin(self.direction)
        self.fill = fill

    def move(self):
        self.canvas.move(self.square, self.dx, self.dy)

        # Vérification des limites de la fenêtre et rebond si nécessaire
        x1, y1, x2, y2 = self.canvas.coords(self.square)
        if x1 < 0 or x2 > 800 or y1 < 0 or y2 > 600:
            # remise à l'intérieur de la fenêtre
            if x1 < 0:
                self.dx = -x1
            elif x2 > 800:
                self.dx = 800 - x2
            else:
                self.dx = 0

            if y1 < 0:
                self.dy = -y1
            elif y2 > 600:
                self.dy = 600 - y2
            else:
                self.dy = 0

            self.canvas.move(self.square, self.dx, self.dy)

            # inversion du sens pour le rebond
            if x1 < 0 or x2 > 800:
                self.dx = -self.dx
            if y1 < 0 or y2 > 600:
                self.dy = -self.dy
def intersects(self, other):
    x1, y1, x2, y2 = self.canvas.coords(self.square)
    other_x1, other_y1, other_x2, other_y2 = self.canvas.coords(other.square)

    return x1 < other_x2 and x2 > other_x1 and y1 < other_y2 and y2 > other_y1
cl =  Window("test")
mycanvas = Canvas(450, 450)
cl.add_canvas(mycanvas)
cl.update()