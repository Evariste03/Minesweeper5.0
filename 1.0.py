#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import random
import tkinter.messagebox


# In[2]:


def win_check():
    global x
    global y
    global board
    global di
    
    for a in range(x):
        for b in range(y):
            if board[b][a]==0 and di[(a,b)]['state']=='normal':
                return False
    return True


# In[3]:


def click(x, y):
            
    global di
    global board
    global game_on
    
    di[(x, y)]['state']='disabled'
    di[(x, y)]['relief']='groove'
    
    if not game_on:
        game_on=True
        board=generate_mine(x,y)
            
    if board[y][x]==1:
        show_all()
        game_on=False
        tkinter.messagebox.showinfo("", "You lost the game!")
        
    else:
        count=0
        for p in range(x-1,x+2):
            for q in range(y-1, y+2):
                if p>=0 and q>=0:
                    try:
                        count+=board[q][p]
                    except:
                        pass
                
        if count>0:
            di[(x, y)]['text']=count
                    
        else:
            for p in range(x-1,x+2):
                for q in range(y-1, y+2):
                    if p>=0 and q>=0:
                        try:
                            di[(p, q)].invoke()
                        except:
                            pass
    
    if game_on:
        if win_check():
            tkinter.messagebox.showinfo("", "Congratulations! You won the game!")
            for a in range(x):
                for b in range(y):
                    di[(a,b)]['state']='disabled'


# In[4]:


class s_Button(Button):
    def __init__(self, x, y, **args):
        Button.__init__(self, **args)
        self.x=x
        self.y=y
    def flag(self, event):
        if self['state']=='normal':
            if self['text']=='':
                self['text']='🚩'
            elif self['text']=='🚩':
                self['text']='?'
            elif self['text']=='?':
                self['text']=''
    def operate(self):
        self['command']=lambda: click(self.x, self.y)
        self.bind('<Button-3>', self.flag)


# In[5]:


def generate_mine(a,b):
    global x
    global y
    global mine_num

    initial=[]

    if (a,b)==(0,0) or (a,b)==(x-1,0) or (a,b)==(0,y-1) or (a,b)==(x-1,y-1):
        total=x*y-4
    elif a==0 or a==x-1 or b==0 or b==y-1:
        total=x*y-6
    else:
        total=x*y-9

    for i in range(mine_num):
        initial.append(1)
    for i in range(total-mine_num):
        initial.append(0)

    random.shuffle(initial)

    board = [[0 for i in range(x)] for i in range(y)]

    for i in range(x):
        for j in range(y):
            if not ((i,j)==(a+1,b+1) or (i,j)==(a,b+1) or (i,j)==(a-1,b+1) or (i,j)==(a+1,b) or (i,j)==(a,b) or (i,j)==(a-1,b) or (i,j)==(a+1,b-1) or (i,j)==(a,b-1) or (i,j)==(a-1,b-1)):
                board[j][i]=initial.pop()
    
    return board


# In[6]:


def show_all():
    global di
    global board
    global x
    global y
    
    for a in range(x):
        for b in range(y):
            if board[b][a]==1:
                di[(a,b)]['text']='✹'
            di[(a,b)]['state']='disabled'


# In[7]:


def restart():
    root.destroy()
    mine()


# In[8]:


def mine():
    global x
    global y
    global mine_num
    global root
    global frame
    global but
    global game_on
    global di
    
    x=15
    y=12
    mine_num=25

    size=f'{x*25}x{y*25+30}'

    root = Tk()
    root.title("扫雷")
    root.geometry(size)

    but = Button(root, text='😊', command=restart)
    but.pack()

    frame = Frame(root)
    frame.place(relx=0.0, rely=30/(25*y+30), relwidth=1.0, relheight=(25*y)/(25*y+30))

    game_on=False

    di=dict()

    for a in range(x):
        for b in range(y):
            example=s_Button(master=frame, x=a, y=b)
            example.place(relx=a/x, rely=b/y, relwidth=1/x, relheight=1/y)
            example.operate()
            di[(a,b)]=example

    root.mainloop()


# In[9]:


mine()

