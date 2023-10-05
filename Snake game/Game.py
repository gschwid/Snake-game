import tkinter as tk
import random as ran
import time
from Snake import Snake
from Food import Food

class Game:

    def __init__(self):
        # Variables to keep track of movement and game mechanics
        self.oldDirection = "down"
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
        if (self.direction == "up"):
            if(self.oldDirection == "down"):
                self.direction = "down" # Updates the current direction if its unable to move cause itll kill itself
                y = y + 25
            else:
                y = y - 25 # moves head up 
        elif (self.direction == "down"):
            if (self.oldDirection == "up"):
                self.direction = "up" # Updates the current direction if its unable to move cause itll kill itself
                y = y - 25
            else:
                y = y + 25 # moves head down
        elif (self.direction == "right"):
            if (self.oldDirection == "left"):
                self.direction = "left" # Updates the current direction if its unable to move cause itll kill itself
                x = x - 25
            else:
                x = x + 25 # moves head right
        elif (self.direction == "left"):
            if(self.oldDirection == "right"):
                self.direction = "right" # Updates the current direction if its unable to move cause itll kill itself
                x = x + 25
            else:
                x = x - 25 # moves head left

        # Creates a new head for the snake depending on which way the user inputs.
        snakeHead = self.canv.create_rectangle(x,y,x + 25, y + 25,fill="green") # Creates new square to replace the old snake head
        body.insert(0,snakeHead)
        cords.insert(0,[x,y])

        # Checks for out of bounce and self collisions
        if self.checkBounds(x,y) or self.checkCollisions(cords):
            self.window.destroy()
        
        # If the snake touches the food, the food gets moved and the snake gets another piece.
        elif(cords[0] == food.getPos()):
            self.food.move(self.canv,cords)
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
            print("You got " + str(self.points) + " points")
            return True
        elif y >= 500 or y < 0:
            print("Game over")
            print("You got " + str(self.points) + " points")
            return True     
        else:
            return False
    
    def checkCollisions(self,cords): # Checks if the snake has collided with itself.
        head = cords[0]
        for i in cords[1:]: # Compares the head cords to all the other cords in the list
            if head == i:
                print("Game over")
                print("You got " + str(self.points) + " points")
                return True
        return False
    
    def up(self,event):
        self.oldDirection = self.direction
        self.direction = "up"

    def down(self,event):
        self.oldDirection = self.direction
        self.direction = "down"

    def right(self,event):
        self.oldDirection = self.direction
        self.direction = "right"

    def left(self,event):
        self.oldDirection = self.direction
        self.direction = "left"
    
    def runGame(self):
        self.window.mainloop() # Displays the GUI

    
