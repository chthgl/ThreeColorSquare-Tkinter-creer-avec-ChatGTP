import tkinter as tk
import random
class Square:
    def __init__(self, canvas, color):
        self.id = canvas.create_rectangle(
            random.randint(0, 475),
            random.randint(0, 475),
            random.randint(0, 475) + 5,
            random.randint(0, 475) + 5,
            fill=color
        )
        self.speed_x = random.randint(1, 10)
        self.speed_y = random.randint(1, 10)
        if self.speed_x == 0 and self.speed_y == 0:
            self.speed_x = random.randint(1, 10)
            self.speed_y = random.randint(1, 10)
        self.canvas = canvas

    def update(self):
        self.canvas.move(
            self.id,
            self.speed_x,
            self.speed_y
        )
        if (self.canvas.coords(self.id)[0] < 0 or
            self.canvas.coords(self.id)[2] > 500 or
            self.canvas.coords(self.id)[1] < 0 or
            self.canvas.coords(self.id)[3] > 500):
            self.speed_x *= -1
            self.speed_y *= -1
    
    def check_collision(self, squares):
        for square in squares:
            if square == self:
                continue
            if (self.canvas.coords(self.id)[0] <= self.canvas.coords(square.id)[2] and
                self.canvas.coords(self.id)[2] >= self.canvas.coords(square.id)[0] and
                self.canvas.coords(self.id)[1] <= self.canvas.coords(square.id)[3] and
                self.canvas.coords(self.id)[3] >= self.canvas.coords(square.id)[1]):
                if self.speed_x == square.speed_x and self.speed_y == square.speed_y:
                    self.canvas.itemconfig(self.id, fill="green")
                else:
                    self.speed_x *= -1
                    self.speed_y *= -1
                    square.speed_x *= -1
                    square.speed_y *= -1

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

squares = []
for i in range(50):
    squares.append(Square(canvas, "red"))

for i in range(50):
    squares.append(Square(canvas, "blue"))

while True:
    map(lambda x: x.update(), squares)
    map(lambda x: x.check_collision(squares), squares)
    root.update()
