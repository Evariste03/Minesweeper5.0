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
            game_on=False
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


def restarteasy():
    root.destroy()
    easy()


# In[8]:


def restartmedium():
    root.destroy()
    medium()


# In[9]:


def restarthard():
    root.destroy()
    hard()


# In[10]:


def easy():
    global x
    global y
    global mine_num
    global root
    global frame
    global but
    global game_on
    global di
    
    try:
        root.destroy()
    except:
        pass
    
    x=9
    y=9
    mine_num=10

    size=f'{x*25}x{y*25+30}'

    root = Tk()
    root.title("扫雷")
    root.geometry(size)
    
    menubar=Menu(root)
    filemenu=Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Menu', menu=filemenu)
    filemenu.add_command(label='Easy', command=restarteasy)
    filemenu.add_command(label='Medium', command=restartmedium)
    filemenu.add_command(label='Hard', command=restarthard)
    filemenu.add_command(label='custom', command=custom1)

    but = Button(root, text='😊', command=restarteasy)
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
            
    root.config(menu=menubar)

    root.mainloop()


# In[11]:


def medium():
    global x
    global y
    global mine_num
    global root
    global frame
    global but
    global game_on
    global di
    
    try:
        root.destroy()
    except:
        pass
    
    x=16
    y=16
    mine_num=40

    size=f'{x*25}x{y*25+30}'

    root = Tk()
    root.title("扫雷")
    root.geometry(size)
    
    menubar=Menu(root)
    filemenu=Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Menu', menu=filemenu)
    filemenu.add_command(label='Easy', command=restarteasy)
    filemenu.add_command(label='Medium', command=restartmedium)
    filemenu.add_command(label='Hard', command=restarthard)
    filemenu.add_command(label='custom', command=custom1)

    but = Button(root, text='😊', command=restartmedium)
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
            
    root.config(menu=menubar)

    root.mainloop()


# In[12]:


def hard():
    global x
    global y
    global mine_num
    global root
    global frame
    global but
    global game_on
    global di
    
    try:
        root.destroy()
    except:
        pass
    
    x=30
    y=16
    mine_num=99

    size=f'{x*25}x{y*25+30}'

    root = Tk()
    root.title("扫雷")
    root.geometry(size)
    
    menubar=Menu(root)
    filemenu=Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Menu', menu=filemenu)
    filemenu.add_command(label='Easy', command=restarteasy)
    filemenu.add_command(label='Medium', command=restartmedium)
    filemenu.add_command(label='Hard', command=restarthard)
    filemenu.add_command(label='custom', command=custom1)

    but = Button(root, text='😊', command=restarthard)
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
            
    root.config(menu=menubar)

    root.mainloop()


# In[13]:


def max_mine(event):
    global e1
    global e2
    global m
    global l4
    
    try:
        m=int(int(e1.get())*int(e2.get())*0.9)
        l4.config(text=f'Number of mines: \n(5~{m})')
    except:
        pass


# In[14]:


def custom1():
    global x
    global y
    global mine_num
    global root
    global e1
    global e2
    global e3
    global l4
    global m
    
    try:
        root.destroy()
    except:
        pass
    
    root=Tk()
    root.title('Custom Mineboard')
    root.geometry('400x300')
    
    l0=Label(root, text='Custom Mineboard', font=('宋体',20))
    l0.pack()
    
    l1=Label(root, text='Number of colums: \n(9~30)', font=('宋体',15))
    l1.place(relx=0.0, rely=0.15, relwidth=0.5)
    
    l2=Label(root, text='Number of rows: \n(9~24)', font=('宋体',15))
    l2.place(relx=0.5, rely=0.15, relwidth=0.5)
    
    l3=Label(root, text='x', font=('宋体',15))
    l3.place(relx=0.4, rely=0.32, relwidth=0.2)
    
    e1=Entry(root, font=('宋体',15))
    e1.place(relx=0.1, rely=0.34, relwidth=0.3)
    e1.bind('<KeyRelease>', max_mine)
    
    e2=Entry(root, font=('宋体',15))
    e2.place(relx=0.6, rely=0.34, relwidth=0.3)
    e2.bind('<KeyRelease>', max_mine)
    
    l4=Label(root, text='Number of mines: \n(5~ )', font=('宋体',15))
    l4.place(rely=0.5, relwidth=1.0)
    
    e3=Entry(root, font=('宋体',15))
    e3.place(relx=0.35, rely=0.69, relwidth=0.3)
    
    b=Button(root, text='Confirm', font=('宋体',15), command=lambda: custom2(e1.get(),e2.get(),e3.get()))
    b.place(relx=0.4, rely=0.82, relwidth=0.2)
    
    root.mainloop()


# In[15]:


def restartcustom():
    global x
    global y
    global mine_num
    custom2(x,y,mine_num)


# In[16]:


def custom2(one, two, three):
    global x
    global y
    global mine_num
    global root
    global frame
    global but
    global game_on
    global di
    global m
    
    try:
        if float(one)%1==0 and float(two)%1==0 and float(three)%1==0 and float(three)>=5 and float(three)<=m and float(one)>=9 and float(one)<=30 and float(two)>=9 and float(two)<=24:
            root.destroy()

            x=int(one)
            y=int(two)
            mine_num=int(three)

            size=f'{x*25}x{y*25+30}'

            root = Tk()
            root.title("扫雷")
            root.geometry(size)

            menubar=Menu(root)
            filemenu=Menu(menubar, tearoff=0)
            menubar.add_cascade(label='Menu', menu=filemenu)
            filemenu.add_command(label='Easy', command=easy)
            filemenu.add_command(label='Medium', command=medium)
            filemenu.add_command(label='Hard', command=hard)
            filemenu.add_command(label='custom', command=custom1)

            but = Button(root, text='😊', command=restartcustom)
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

            root.config(menu=menubar)

            root.mainloop()
        else:
            tkinter.messagebox.showinfo("", "Invalid input!")
    except:
        tkinter.messagebox.showinfo("", "Invalid input!")


# In[17]:


easy()

