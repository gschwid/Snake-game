import tkinter as tk
import random as ran

class Food:

    def __init__(self,canvas:tk.Canvas):
        self.canvas = canvas 
        self.food = canvas.create_rectangle(0,0,25,25,fill="red") # Creates the red square
        self.move(canvas)
    
    def move(self,canvas:tk.Canvas): # Generates random x and y value on a 20 x 20 grid
        x = (ran.randint(0,19)) * 25
        y = (ran.randint(0,19)) * 25
        canvas.move(self.food,x,y)
    
    def getPos(self):
        return self.canvas.coords(self.food)
    
    def getFood(self):
        return self.food