import tkinter as tk
from random import randint, choice
import math
class Square:
    COLORS = ["green", "yellow", "red", "blue", "purple", "orange"]
    def __init__(self, x, y, color):
        self.size = randint(4,8)
        randomvitesse = randint(1,3)
        self.x = x
        self.y = y
        self.dx = randomvitesse
        self.dy = randomvitesse
        self.color = color
        #self.rect = canvas.create_rectangle(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)
        self.rect = canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, fill=self.color)
    def move(self):
        if self.x + SIZE >= WIDTH or self.x <= 0:
            self.dx *= -1
        if self.y + SIZE >= HEIGHT or self.y <= 0:  
            self.dy *= -1
        self.x += self.dx
        self.y += self.dy
        canvas.move(self.rect, self.dx, self.dy)
        canvas.bind("<Motion>", self.on_mouse_move)
        canvas.bind("<Button-1>", self.on_click)
    def on_click(self, event):
        mouse_x = event.x
        mouse_y = event.y
        global clicked_square
        clicked_square = None
        for square in squares:
            if (abs(square.x - mouse_x) < SIZE and abs(square.y - mouse_y) < SIZE):
                clicked_square = square
        if clicked_square is not None:
            clicked_square.change_color(choice(Square.COLORS))
    def on_mouse_move(self, event):
        mouse_x = event.x
        mouse_y = event.y
        self.change_color(choice(Square.COLORS))
        for square in squares:
            distance = math.sqrt((square.x - mouse_x)**2 + (square.y - mouse_y)**2)

            if distance <= 10:  # Ajout d'une condition pour vérifier la distance
                square.dx *= -1
                square.dy *= -1
            elif (abs(square.x - mouse_x) < SIZE and abs(square.y - mouse_y) < SIZE):
                square.dx *= -1
                square.dy *= -1
    def change_speed(self):
        for square in squares:
            self.dx = randint(1, 3) # Modification aléatoire de la vitesse en x
            self.dy = randint(1, 3) # Modification aléatoire de la vitesse en y
        


    def change_color(self, color):
        self.color = color
        canvas.itemconfig(self.rect, fill=color)
    #Les plus petit prennent la couleur des carré plus gros, 
    #si le carré plus gros vas plus vite que le carré plus petit ils gardes la même couleur, 
    #si le carré plus petit vas plus vite que le plus gros le plus gros deviens noir    
    def detect_collision(self, other_square):
        if (self.x < other_square.x + SIZE and self.x + SIZE > other_square.x and
        self.y < other_square.y + SIZE and self.y + SIZE > other_square.y):
            if self.size > other_square.size:
                if self.dx > other_square.dx and self.dy > other_square.dy:
                    other_square.change_color(self.color)
                else:
                    other_square.change_color("black")
            elif self.size < other_square.size:
                if self.dx < other_square.dx and self.dy < other_square.dy:
                    self.change_color(other_square.color)
                else:
                    self.change_color("black")
            self.dx *= -1
            self.dy *= -1
            other_square.dx *= -1
            other_square.dy *= -1

SIZE = 10 
speedrand = randint(15, 40)
SPEED = speedrand 
COLORS = ["green", "yellow", "red"] 
window = tk.Tk()
window.title("Carrés")
WIDTH = window.winfo_screenwidth()
HEIGHT = window.winfo_screenheight()
WIDTH = WIDTH - 100
HEIGHT =HEIGHT - 100
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
squares = []

for j in range(65):
    for i in range(3):
        x = randint(0, WIDTH-SIZE)
        y = randint(0, HEIGHT-SIZE)
        color = COLORS[i]
        squares.append(Square(x, y, color))
squares.append(Square(0, 0, "blue"))
squares.append(Square(WIDTH-SIZE, 0, "purple"))
squares.append(Square(0, HEIGHT-SIZE, "orange"))

def update():
    
    for square in squares:
        square.move()

        for other_square in squares:
            if square != other_square:
                square.detect_collision(other_square)
    
    window.after(1000, square.change_speed)
    window.after(SPEED, update)
update()
window.mainloop()
