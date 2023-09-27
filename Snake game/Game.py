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
        self.gameMovement(self.snake,self.food)
        print(self.food.getPos())

    def gameMovement(self,snake: Snake,food: Food):
        body = snake.getSnakeBody()
        cords = snake.getSnakeCords()
        x,y = cords[0] # Gets the position of the head of the snake.
        x = x + 25
        snakeHead = self.canv.create_rectangle(x,y,x + 25, y + 25,fill="green")
        body.insert(0,snakeHead)
        cords.insert(0,[x,y])
        self.canv.delete(body[-1])
        del body[-1]
        del cords[-1]
        self.canv.update()
        self.window.after(200,self.gameMovement,snake,food)

    def runGame(self):
        self.window.mainloop() # Displays the GUI

    
