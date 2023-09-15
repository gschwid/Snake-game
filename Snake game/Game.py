import tkinter as tk
import random as ran
import time
from Snake import Snake
from Food import Food

class Game:
    
    game_over = False

    def game_end(cls):
        canv.destroy()
        print("Game over wahhhhhh")

    def check_boundaries(cls):
        while cls.game_over == False:
            print("HI BABA")


    def up(event):
        while True:
            canv.update()
            canv.move(snake.getSnake(),0,-25)
            time.sleep(.1)

    def down(event):
        while True:
            canv.update()
            canv.move(snake.getSnake(),0,25)
            time.sleep(.1)

    def left(event):
        while True:
            canv.update()
            canv.move(snake.getSnake(),-25,0)
            time.sleep(.1)

    def right(event):
        while True:
            canv.update()
            canv.move(snake.getSnake(),25,0)
            time.sleep(.1)

    window = tk.Tk()
    window.geometry("500x500") # Sizing the window for the snake game
    window.title("Snake")
    global canv
    canv = tk.Canvas(window,width=500,height=500,bg="black")
    canv.pack() # IDK what this rlly does but it puts the canvas on the windo

    window.bind("w", up)
    window.bind("s", down)
    window.bind("a", left)
    window.bind("d", right)
    global snake
    food = Food(canv)
    snake = Snake(canv,150,200)
    window.mainloop() # Displays the GUI


