import tkinter as tk
import random as ran

class Snake:

    def __init__(self,canvas:tk.Canvas,x,y):
        self.canvas = canvas
        #self.snake = canvas.create_rectangle(0,0,25,25,fill="green") # Creates the red square
        #self.canvas.move(self.snake,x,y)
        self.cords = [] # keeps track of the coordnates of the snake
        self.body = [] # keeps track of the squares associated with the cords.

        for i in range(2):
            self.cords.append([0,0])
       
        for i,j in self.cords:
            print(j)
            snake = self.canvas.create_rectangle(i,j,i + 25, j + 25,fill="green")
            self.body.append(snake)
    
    

    def getSnake(self):
        return self.snake

