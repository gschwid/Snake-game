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
        self.canvas.delete(self.food)
        self.food = canvas.create_rectangle(x,y,x+25,y+25,fill="red") # Creates new rectangle with the new cords.

    
    def getPos(self):
        cords = self.canvas.coords(self.food)
        cords = [int(cords[0]),int(cords[1])] # Gets just the x and y cords, not the other that show how big it is.
        return cords
    
    def getFood(self):
        return self.food