import  tkinter  as  tk
from tkinter import *
import random
from random import randint
from tkinter import ttk
from  PIL  import  Image , ImageTk
from tkinter import messagebox
import mysql.connector as c
import tkinter.font as font
from datetime import datetime, timedelta
from itertools import cycle
from subprocess import call



zstar = tk.Tk()

zstar.title("Home")
zstar.state("zoomed")
zstar.config(background="black")
s = ttk.Style()
s.configure('My.TFrame', background='black', foreground="white")

frame300 = ttk.Frame(zstar,style='My.TFrame' )
frame300.pack(side="left",fill="y",expand=True)

tk.Label(frame300, text ="                HANGMAN                ", font=('fixedsys 7'), bg = "black", fg = "white").pack(side="top")

tk.Label(frame300, text ="1)Play individually or in groups.\n2)select a letter of the alphabets.\n3)Click on the button with appropriate letter on it to reveal the \nletter within the movie\n4)If the letter is contained in the movie,it will be revealed\n5)If the letter is not contained in the movie,a portion of the hangman is added\n6)The game continues until:\n         1)the movie is guessed (all letters are revealed) – WINNER or,\n         2)all the parts of the hangman are displayed – LOSER", font=('fixedsys 5'), justify="left", bg = "black", fg = "white").pack()

frame200 = ttk.Frame(zstar,style='My.TFrame' )
frame200.pack(side="right",fill="y",expand=True)

tk.Label(frame200, text ="                SNAKE                ", font=('fixedsys 7'),  bg = "black", fg = "white").pack(side="top")

tk.Label(frame200 , text= "1)no such instructions", font=('fixedsys 4'), justify="left", bg = "black", fg = "white").pack()

def btn1():
    call(["python", "snake2.py"])
tk.Button(frame200, text="play", command=btn1, padx = 10, font=('fixedsys 5'), background="purple", foreground= "white").pack(anchor=tk.CENTER, pady = 10)

def btn2():
    call(["python", "hangman1.py"])    
tk.Button(frame300, text="play", command=btn2, padx = 10, font=('fixedsys 5'), background="purple", foreground= "white").pack(anchor=tk.CENTER, pady = 10)

zstar.mainloop()