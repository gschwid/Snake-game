import tkinter as tk
import random as ran

class Snake:

    def __init__(self,canvas:tk.Canvas,x,y):
        self.canvas = canvas
        self.snake = canvas.create_rectangle(0,0,25,25,fill="green") # Creates the red square
        self.canvas.move(self.snake,x,y)

    def getPos(self):
        return self.canvas.coords(self.snake)
    
    def getSnake(self):
        return self.snake
        
