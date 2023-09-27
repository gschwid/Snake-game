import tkinter as tk
import random as ran
import time
from Snake import Snake
from Food import Food

class Game:

    def __init__(self):
        # Variables to keep track of movement and game mechanics
        self.direction = "down"
        self.points = 0
        self.game_over = False

        # Sets up the window for the game
        self.window = tk.Tk()
        self.window.geometry("500x500") # Sizing the window for the snake game
        self.window.title("Snake")
        self.canv = tk.Canvas(self.window,width=500,height=500,bg="black")
        self.canv.pack() # IDK what this rlly does but it puts the canvas on the windo

        # Setting binds for movement
        self.window.bind("w", self.up)
        self.window.bind("s", self.down)
        self.window.bind("a", self.left)
        self.window.bind("d", self.right)

        # Instance of snake and food class
        self.food = Food(self.canv)
        self.snake = Snake(self.canv,150,200)
        self.gameMovement(self.snake,self.food)

    def gameMovement(self,snake: Snake,food: Food):
        body = snake.getSnakeBody()
        cords = snake.getSnakeCords()
        x,y = cords[0] # Gets the position of the head of the snake.

        # If statements that determine how the coordinates get updated.
        if self.direction == "up":
            y = y - 25 # moves head up 
        elif self.direction == "down":
            y = y + 25 # moves head down
        elif self.direction == "right":
            x = x + 25 # moves head right
        else:
            x = x - 25 # moves head left

        # Creates a new head for the snake depending on which way the user inputs.
        snakeHead = self.canv.create_rectangle(x,y,x + 25, y + 25,fill="green") # Creates new square to replace the old snake head
        body.insert(0,snakeHead)
        cords.insert(0,[x,y])

        if self.checkBounds(x,y):
            self.window.destroy()
        
        elif(cords[0] == food.getPos()):
            self.food.move(self.canv)
            self.points += 1

        else:
            # Deletes the last element in list if the head of snake hasnt touched no food.
            self.canv.delete(body[-1])
            del body[-1]
            del cords[-1]
            self.canv.update()

        self.window.after(80,self.gameMovement,snake,food) #Creates a loop for the movement, normal while loops didnt work.

    def checkBounds(self,x: int,y: int): # Method ends the game if the snake leaves the screen
        if x >= 500 or x < 0:
            print("Game over")
            return True
        elif y >= 500 or y < 0:
            print("Game over")
            return True     
        else:
            return False
    
    def checkCollisions(self,snake:Snake): # Checks if the snake has collided with itself.
        pass
    
    def up(self,event):
        self.direction = "up"

    def down(self,event):
        self.direction = "down"

    def right(self,event):
        self.direction = "right"

    def left(self,event):
        self.direction = "left"
    
    def runGame(self):
        self.window.mainloop() # Displays the GUI

    
