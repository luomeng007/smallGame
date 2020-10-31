# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:35:17 2020

@author: 15025
"""
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class GuessNumber:
    def __init__(self):
        self.number = random.randint(0, 10)
        self.para1 = None
    
    def mainProgram(self):
        self.guiInterface()
        
    def guiInterface(self):
        self.gui = tk.Tk()
        
        self.gui.title("Guess number v1.00")
        
        self.gui.geometry("300x200+350+150")
        
        basic_position_x = 20
        basic_position_y = 50
        
        self.para1 = tk.Entry(self.gui)
        self.para1.place(x=basic_position_x + 100, y=basic_position_y)
        
        tk.Label(self.gui, text="请猜一个1-10中的数值:").place(x=basic_position_x, y=basic_position_y - 30)
        tk.Label(self.gui, text="猜测值:").place(x=basic_position_x + 50, y=basic_position_y)
        
        ttk.Button(self.gui, text="确定", command=self.compareValue).place(x=120,y=100)
        
        self.gui.mainloop()
        
    def compareValue(self):
        number = int(self.para1.get())
        if number > self.number:
            messagebox.showinfo(title="猜测结果", message="猜的大了")
        elif number < self.number:
            messagebox.showinfo(title="猜测结果", message="猜的小了")
        else:
            messagebox.showinfo(title="猜测结果", message="猜对了！")
            self.gui.destroy()
    

if __name__ == "__main__":
    game = GuessNumber()
    game.mainProgram()