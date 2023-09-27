import tkinter as tk
import random as ran

class Snake:

    def __init__(self,canvas:tk.Canvas,x,y):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.cords = [] # keeps track of the coordnates of the snake
        self.body = [] # keeps track of the squares associated with the cords.

        for i in range(2): # Creating the starting coordinates for the snake
            self.cords.append([self.x,self.y])
       
        for x,y in self.cords: # This is creating the 2 rectangles to start the snake.
            snake = self.canvas.create_rectangle(x,y,x + 25, y + 25,fill="green")
            self.body.append(snake)

    def getSnakeBody(self):
        return self.body
    
    def getSnakeCords(self):
        return self.cords

