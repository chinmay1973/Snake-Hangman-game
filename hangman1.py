import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from  PIL  import  Image , ImageTk
import mysql.connector
import tkinter.font as font


score = 0
run = True

mydb=mysql.connector.connect(host="localhost",user="root",password="root", database="hollywood")
mycursor = mydb.cursor()
                    
qry='select (movie) from movies'
mycursor.execute(qry)
mymovies=mycursor.fetchall()

global BTN1, BTN2, BTN3

# main loop
while run:
    roo1 = tk.Tk()
    roo1.geometry('905x700')
    roo1.title('HANG MAN')
    roo1.attributes('-fullscreen' , True)
    #roo1.bind('<Escape>',quit)

    roo1.config(bg = '#E7FFFF')
    count = 0
    win_count = 0

    # choosing word
    words_list=list(mymovies)
    word= list(random.choice(words_list))
    the_word=[]
    for i in range(0,len(word[0])):
         the_word.append(word[0][i])
    mydb.commit()


    def hinta():
        global word
     
        qry1=f'select (Hint1) from movies where movie = "{word[0]}"'
        mycursor.execute(qry1)
        myhint=list(mycursor.fetchone())
        label1=tk.Label(roo1, text=myhint[0], font= 'helvetica 15', bg = '#E7FFFF',padx = 10, pady =5).place(x = 600 , y = 100)
        BTN2=tk.Button(roo1 , text = 'hint 2' , command =hintb, bg = 'green', fg = 'white',padx = 10, pady =5).place(x=600,y=150)

    def hintb():
        
        global word
        qry2=f'select (Hint2) from movies where movie = "{word[0]}"'
        mycursor.execute(qry2)
        myhint=list(mycursor.fetchone())
        label2=tk.Label(roo1, text=myhint[0],font= 'helvetica 15', bg = '#E7FFFF',padx = 10, pady =5).place(x = 600 , y = 150)
        BTN3=tk.Button(roo1 , text = 'hint 3' , command =hintc, bg = 'green', fg = 'white',padx = 10, pady =5).place(x=600,y=200)
    def hintc():
        global word
        qry3=f'select (Hint3) from movies where movie = "{word[0]}"'
        mycursor.execute(qry3)
        myhint=list(mycursor.fetchone())
        label3=tk.Label(roo1, text=myhint[0], font= 'helvetica 15', bg = '#E7FFFF',padx = 10, pady =5).place(x = 600 , y = 200)
    BTN1=tk.Button(roo1 , text = 'hint 1' , command =hinta, bg = 'green', fg = 'white',padx = 10, pady =5).place(x = 600, y = 100)
    #for b_b in lst:
     #   if b_b != "_":
      #      pass
        
       # tk.messagebox.askyesno('YOU WIN','THE MOVIE WAS \n "{}" \nYOU WON!\nWANT TO PLAY AGAIN?\n'.format(word[0]))
        #if answer == True:
         #           run = True
          #          score = 0
           #         roo1.destroy()
        #else:
         #           run = False
          #          roo1.destroy()

  
   
    # creation of word dashes variables
    x = 25
    lst=[]
    for i in range(0,len(the_word)):
        x += 40
        for a_a in [" ", ":", "a","e","i","o","u", "A","E","I","O","U"]:
            if the_word[i]==a_a:
                exec('d{}=Label(roo1,text=a_a.upper(),bg="#E7FFFF",font=("fixedsys", 25))'.format(i))
                exec('d{}.place(x={},y={})'.format(i,x,450))
                lst.append(f'{a_a}')
                break
                
                         
        else:
                exec('d{}=Label(roo1,text="_",bg="#E7FFFF",font=("fixedsys", 25))'.format(i))
                exec('d{}.place(x={},y={})'.format(i,x,450))
                lst.append("_")
            
               
        
    #letters icon
    al = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    for let in al:
        exec('{}=ImageTk.PhotoImage(file="e:/hangman1/{}.png")'.format(let,let))
    
        
    # hangman images
    h123 = ['hang0','hang1','hang2','hang3','hang4','hang5','hang6']
    for hangman in h123:
        exec('{}=ImageTk.PhotoImage(Image.open("e:/hangman1/{}.png").resize((350,350), Image.ANTIALIAS))'.format(hangman,hangman))


    # button press check function
    def check(letter,button):
        global count,win_count,run,score,_count
        _count = 0
        exec('{}.destroy()'.format(button))
        for _ in lst:
            if _=="_":
                _count+=1
        print(_count)
        print(lst)
                
        if letter in the_word:
                  for i in range(0,len(the_word)):
                        if the_word[i] == letter:
                            _count =_count-1
                            print(_count)
                            exec('d{}.config(text="{}")'.format(i,letter.upper()))
                            lst[i] = letter
                  if _count == 0:           
                                score +=1
                                s2 = 'SCORE:'+str(score)
                                s1 = tk.Label(roo1,text = s2,bg = "#E7FFFF",font = ("arial",25))
                                s1.place(x = 10,y = 10)
                                answer = tk.messagebox.askyesno('YOU WIN','THE MOVIE WAS \n "{}" \nYOU WON!\nWANT TO PLAY AGAIN?\n'.format(word[0]))
                                if answer == True:
                                      run = True
                                      
                                      roo1.destroy()
                                else:
                                      run = False
                                      roo1.destroy()

                            
                        
        else:
            count += 1
            #exec(f'c{count}.destroy()')
            exec('c{}.place(x={},y={})'.format(count+1,100,70))
            if count == 6:
                answer = messagebox.askyesno('GAME OVER','THE MOVIE WAS \n "{}" \nYOU LOST!\nWANT TO PLAY AGAIN?\n'.format(word[0]))
                if answer == True:
                    run = True
                    score = 0
                    roo1.destroy()
                else:
                    run = False
                    roo1.destroy()
        
        
    #letters placement
    button = [['b2','b',100,600],['b3','c',200,600],['b4','d',300,600],['b6','f',500,600],['b7','g',600,600],['b8','h',700,600],['b10','j',900,600],['b11','k',1000,600],['b12','l',1100,600],['b13','m',1200,600],['b14','n',0,650],['b16','p',200,650],['b17','q',300,650],['b18','r',400,650],['b19','s',500,650],['b20','t',600,650],['b22','v',800,650],['b23','w',900,650],['b24','x',1000,650],['b25','y',1100,650],['b26','z',1200,650]]
    for __ in button:
        exec('{}=tk.Button(roo1,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(__[0],__[1],__[0],__[1]))
        exec('{}.place(x={},y={})'.format(__[0],__[2],__[3]))
        
    #hangman placement
    han = [['c1','hang0'],['c2','hang1'],['c3','hang2'],['c4','hang3'],['c5','hang4'],['c6','hang5'],['c7','hang6']]
    for p1 in han:
        exec('{}=Label(roo1,bg="#E7FFFF",image={})'.format(p1[0],p1[1]))

    # placement of first hangman image
    "c1".place(x = 100,y = 70)    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            roo1.destroy()
            
    e1 = ImageTk.PhotoImage(file = 'e:/hangman1/exit.png')
    ex = tk.Button(roo1,bd = 0,command = close,bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = e1)
    ex.place(x=1200,y=10)
    s2 = 'SCORE:'+str(score)
    s1 = tk.Label(roo1,text = s2,bg = "#E7FFFF",font = ("arial",25))
    s1.place(x = 10,y = 10)

   
  
    roo1.mainloop()
