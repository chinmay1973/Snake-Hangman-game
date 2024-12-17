import  tkinter  as  tk
from random import randint
from tkinter import ttk
from  PIL  import  Image , ImageTk
from tkinter import messagebox
import mysql.connector as c
import tkinter.font as font
from datetime import datetime, timedelta
from itertools import cycle


# ========================================================================================================================================================================
mydb=c.connect(host="localhost",user="root",password="root", database="game")
mycursor = mydb.cursor()

# ========================================================================================================================================================================


def popup():
        # button.config(state = 'disable')

        messagebox.showwarning("Game Over", " You have lost the game")
        
        qry1 = "select * from score_board"
        mycursor.execute(qry1)
        myresult = mycursor.fetchall()
                    
        mydb.commit()


# ========================================================================================================================================================================
class Snake(tk.Canvas):
            qry1 = "select name, score from score_board"
            mycursor.execute(qry1)
            myresult = mycursor.fetchall()
            Score_challenge = []
            if(myresult == []): 
                 challenge = 100
            else:
                for score in myresult:
                    Score_challenge.append(score[1])
                Score_challenge.sort()
                if(Score_challenge[len(Score_challenge)-1]>=100):
                     challenge = Score_challenge[len(Score_challenge)-1]
                else:
                     challenge = 100
            mydb.commit()
        
            def __init__(self):
                super().__init__(
                    width=1000, height=764, background="gray9", highlightthickness=0
                )
                global moves_per_second
                self.snake_positions = [(80, 100), (60, 100), (40, 100)]
                self.food_position = self.set_new_food_position()
                self.direction = "Right"
                moves_per_second =15
                self.score = 0
                
                self.restart_button=tk.Button(frame, text='restart',command=self.restart,  bg= "purple", fg="white", padx = 20, font=("Fixedsys", 3) )
                self.restart_button.pack(side = "bottom")
                self.restart_button['state']= 'disabled'
                # DisplayHighestScore(Snake.challenge)


                self.load_assets()
                self.create_objects()
        
                self.bind_all("<Key>", self.on_key_press)
        
                self.pack()
        
                self.after(1000 // moves_per_second, self.perform_actions)
                        # challenge2 = challenge + 1
                        # yay = tk.messagebox.askyesno('CHALLENGE', f' SCORE {challenge2}')
                        # challenge = challenge2
                        # if yay ==1:
                        #     super().destroy()
                        #     lbl.destroy()

                        #     self.after(500,self.__init__)
                        #     self.restart_button.destroy()
                        #     iBET.destroy()
                        # if yay == 0:
                        #     root.destroy()

            def load_assets(self):
                try:
                    self.snake_body_image = Image.open("./assets/snake.png")
                    self.snake_body = ImageTk.PhotoImage(self.snake_body_image)
        
                    self.food_image = Image.open("./assets/food.png")
                    self.food = ImageTk.PhotoImage(self.food_image)
                except IOError as error:
                    root.destroy()
                    raise
                    
            def create_objects(self):
                self.create_text(
                    115, 15, text=f"Score: {self.score} , speed: {moves_per_second}", tag="score", fill="WHITE", font=('HELVETICA', 6)
                )
        
                for x_position, y_position in self.snake_positions:
                    self.create_image(
                        x_position, y_position, image=self.snake_body, tag="snake"
                    )
        
                self.create_image(*self.food_position, image=self.food, tag="food")
                self.create_rectangle(7,27, 993, 757, outline="#525d69")
        
            def check_collisions(self):
                head_x_position, head_y_position = self.snake_positions[0]
        
                return (
                    head_x_position in (0, 1000)
                    or head_y_position in (40,760)
                    or (head_x_position, head_y_position) in self.snake_positions[1:]
                )
        
            def check_food_collision(self):    
                global moves_per_second
                if self.snake_positions[0] == self.food_position:
                    self.score += 1
                    self.snake_positions.append(self.snake_positions[-1])
        
                    if self.score % 5== 0:
                        moves_per_second += 1
                    
                    self.create_image(
                        *self.snake_positions[-1], image=self.snake_body, tag="snake"
                    )
                    self.food_position = self.set_new_food_position()
                    self.coords(self.find_withtag("food"), *self.food_position)
        
                    score = self.find_withtag("score")
                    self.itemconfigure(score,
                                       text=f"Score: {self.score} , speed: {moves_per_second}", 
                                       tag="score")
                    
            def move_snake(self):
                head_x_position, head_y_position = self.snake_positions[0]
        
                if self.direction == "Left":
                    new_head_position = (head_x_position - MOVE_INCREMENT, head_y_position)
                elif self.direction == "Right":
                    new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)
                elif self.direction == "Down":
                    new_head_position = (head_x_position, head_y_position + MOVE_INCREMENT)
                elif self.direction == "Up":
                    new_head_position = (head_x_position, head_y_position - MOVE_INCREMENT)
        
                self.snake_positions = [new_head_position] + self.snake_positions[:-1]
        
                for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
                    self.coords(segment, position)
        
            def on_key_press(self, e):
                new_direction = e.keysym
        
                all_directions = ("Up", "Down", "Left", "Right")
                opposites = ({"Up", "Down"}, {"Left", "Right"})
        
                if (
                    new_direction in all_directions
                    and {new_direction, self.direction} not in opposites
                ):
                    self.direction = new_direction
        
            def perform_actions(self):
                if self.check_collisions():
                    self.end_game()
        
                self.check_food_collision()
                self.move_snake()
        
                self.after(1000 // moves_per_second, self.perform_actions)
        
            def set_new_food_position(self):
                while True:
                    x_position = randint(1, 48) * MOVE_INCREMENT
                    y_position = randint(3, 35) * MOVE_INCREMENT
                    food_position = (x_position, y_position)
        
                    if food_position not in self.snake_positions:
                        return food_position

            def end_game(self):
                global lbl
                self.delete(tk.ALL)
                self.create_text(
                    self.winfo_width() / 2,
                    self.winfo_height() / 2,
                    text=f"Game over! You scored {self.score}!",
                    fill="WHITE",
                    font= ('Fixedsys', 6)
                    )
                mycursor = mydb.cursor()
                qry =f"insert into score_board (name,Score) values('{name.get()}','{self.score}');"
                mycursor.execute(qry)
                mycursor.execute("SELECT COUNT(*) FROM score_board;")
                n = mycursor.fetchone()

                mydb.commit()
                def fro():
                    for i in n:
                        return i

                count = fro()
                my_tree.insert(parent = '', index = 'end',iid= count,values=(f"{name.get()}",f"{self.score}"))              
                popup()
                self.restart_button['state']='active'
                
                
                if self.score >= Snake.challenge:
                        Snake.challenge = self.score + 1
                        DisplayHighestScore.iBET.config(text=f'WOW UR HIGHEST SCORE IS {self.score}\nCAN U BEAT IT AGAIN 0_0\' ')

                        super().destroy()
                        top=tk.Toplevel(root)
                        top.title()
                        top.configure(background = 'lavender')
                        top.attributes('-fullscreen', True)
                        top.wm_attributes('-transparent','lavender')
                        fnt = font.Font(family = 'fixedsys',size = 40,weight='bold')
                        lbl = ttk.Label(top, font=fnt, foreground="black", background="lavender")
                        lbl.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                        self.change()
                        self.after(2100, lbl.destroy)
                        top.mainloop()

            def change(self):
                lbl.config(text = "YOU HAVE SET A NEW RECORD!!", foreground=next(colour))
                root.after(300, self.change)

            def restart(self):              
                if self.score > Snake.challenge-1:
                        self.restart_button.destroy()
                else:
                     super().destroy()
                     self.restart_button.destroy()
                     self.after(250, self.__init__)

# ========================================================================================================================================================================

class DisplayHighestScore:
            iBET = None
            def __init__(self, challenge):
                DisplayHighestScore.iBET=tk.Label(frame2, text=f'XD! MY HIGHEST SCORE IS {challenge}\nI BET U CANT BREAK IT! ;) ' ,font=("Fixedsys", 3))
                DisplayHighestScore.iBET.pack(side="top", pady=20)

# ========================================================================================================================================================================
                

MOVE_INCREMENT = 20
moves_per_second =15
GAME_SPEED = 1000 // moves_per_second

global name, my_tree,restart_button,highest, frame2, insert,highes,n, count, colour,lbl

colour = cycle(['black', 'lavender'])

mydb=c.connect(host="localhost",user="root",password="root", database="game")
mycursor = mydb.cursor()

def quit(*args):
    root.destroy()


# ========================================================================================================================================================================
root = tk.Tk()
root.title("New Game")

root.configure(background='lavender')

root.attributes('-fullscreen', True)
root.tk.call("tk", "scaling", 4.0)
root.bind('<Escape>',quit)

frame = ttk.Frame(root, padding= (20,10,20,10), relief = 'sunken')
frame.pack(side="left", fill="y")

tk.Label(frame, text="Enter your name:",font=("Fixedsys", 3)).pack(side="top")
name=tk.Entry(frame,borderwidth = 3, width=30, font=("Fixedsys", 3))
name.focus()
name.pack(side="top")


def insert():
          global button
          if name.get()== "":
                 tk.messagebox.showerror("ERROR!!", 'You forgot to enter your name!!')
          else:
                btn1['state'] = 'disable'
                root.after(1000,Snake)

                 
                 
btn1= tk.Button(frame, text = "Play",command = insert, bg= "purple", fg="white", padx = 15, font=("Fixedsys", 3))
btn1.pack(side="top", pady=10)



def reset():
    DisplayHighestScore.iBET.config(text=f'XD! MY HIGHEST SCORE IS 100\nI BET U CANT BREAK IT! ;) ')
    mycursor = mydb.cursor()
    mycursor.execute("delete from score_board")
    
    mycursor = mydb.cursor()
    mydb.commit()
    for i in my_tree.get_children():
        my_tree.delete(i)

        
frame2=tk.Frame(frame)
frame2.pack(side="top", pady=50)
           
                     
# ========================================================================================================================================================================
style = ttk.Style()
style.configure("Treeview",
                background="#D3D3D3",
                forground="white",
                font=("Fixedsys", 3)
                )

style.map('Treeview',
          background=[('selected','purple')]
          )
# ========================================================================================================================================================================
btn2=tk.Button(frame , text= "Quit", command = root.destroy,  bg= "purple", fg="white", padx = 20, font=("Fixedsys", 3))
btn2.pack(side="bottom", pady=10)

btn= tk.Button(frame2, text="Reset Score", command=reset, bg= "purple", fg="white",font=("Fixedsys", 3))
btn.pack(side="bottom", pady=20)
# ========================================================================================================================================================================

DisplayHighestScore(Snake.challenge)

my_tree = ttk.Treeview(frame2, show='headings', column=('Name', 'Scores'), height=16)
my_tree.pack(side="bottom")

# ========================================================================================================================================================================

style = ttk.Style()
style.configure("Treeview.Heading", font=("Fixedsys", 3))

my_tree.column('Name',width=150, minwidth=50, anchor="center")
my_tree.column('Scores',width=150, minwidth=50, anchor="center")

qry1 = "select name, score from score_board"
mycursor.execute(qry1)
myresult = mycursor.fetchall()

for i in range(0,len(myresult),1):
    my_tree.insert(parent = '', index = 'end', iid =i,values=(myresult[i][0],myresult[i][1]))
        
mydb.commit()

my_tree.heading("Name", text = "Name" )
my_tree.heading("Scores", text = "Scores")

root . mainloop()
