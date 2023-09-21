import tkinter as tk
import random as ran
import time
from Snake import Snake
from Food import Food

class Game:

    def __init__(self):
        # Variables to keep track of movement and game mechanics
        self.points = 0
        self.game_over = False
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        self.window = tk.Tk()
        self.window.geometry("500x500") # Sizing the window for the snake game
        self.window.title("Snake")
        self.canv = tk.Canvas(self.window,width=500,height=500,bg="black")
        self.canv.pack() # IDK what this rlly does but it puts the canvas on the windo

        # Setting binds for movement
        # self.window.bind("w", self.up)
        # self.window.bind("s", self.down)
        # self.window.bind("a", self.left)
        # self.window.bind("d", self.right)

        # Instance of snake and food class
        self.food = Food(self.canv)
        self.snake = Snake(self.canv,150,200)

    def getSnake(self):
        return self.snake.getPos()

    def runGame(self):
        self.window.mainloop() # Displays the GUI

