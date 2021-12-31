#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import random
import tkinter.messagebox
import time


# In[2]:


def win_check():
    global x
    global y
    global board
    global di
    
    for a in range(x):
        for b in range(y):
            if board[b][a]==0 and di[(a,b)]['relief']=='raised':
                return False
    return True


# In[3]:


def click(x, y):
            
    global di
    global board
    global game_on
    global game_over
    global start_time
    
    di[(x, y)]['relief']='sunken'
    di[(x, y)]['bd']='1'
    
    if not game_on:
        game_on=True
        board=generate_mine(x,y)
        start_time=time.time()
        gettime()
            
    if board[y][x]==1:
        show_all()
        game_over=True
        tkinter.messagebox.showinfo("", "You lost the game!")
        di[(x, y)]['state']='disabled'
        for i in di.values():
            if i['state']=='normal' and i['relief']=='raised':
                i['state']='disabled'
        
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
            if count==1:
                di[(x, y)]['fg']='blue'
            elif count==2:
                di[(x, y)]['fg']='green'
            elif count==3:
                di[(x, y)]['fg']='red'
            elif count==4:
                di[(x, y)]['fg']='darkblue'
            elif count==5:
                di[(x, y)]['fg']='darkred'
            elif count==6:
                di[(x, y)]['fg']='mediumaquamarine'
            elif count==7:
                di[(x, y)]['fg']='sienna'
            elif count==8:
                di[(x, y)]['fg']='yellow'
            
        else:
            di[(x, y)]['text']=''
            for p in range(x-1,x+2):
                for q in range(y-1, y+2):
                    if p>=0 and q>=0:
                        try:
                            if di[(p, q)]['state']=='disabled':
                                di[(p, q)]['state']='normal'
                            if di[(p, q)]['relief']!='sunken':
                                di[(p, q)].invoke()
                        except:
                            pass
    
    c2=0
    for i in di.values():
            if i['text']=='🚩':
                c2+=1
    mineleft['text']=f'{mine_num-c2}'
    
    if not game_over:
        if win_check():
            game_over=True
            tkinter.messagebox.showinfo("", "Congratulations! You won the game!")
            for i in di.keys():
                if board[i[1]][i[0]]==1:
                    di[i]['state']='disabled'


# In[4]:


class s_Button(Button):
    def __init__(self, x, y, **args):
        Button.__init__(self, **args)
        self.x=x
        self.y=y
    def flag(self, event):
        global c
        global x
        global y
        global mine_num
        global mineleft
        global game_on
        global game_over
        if self['relief']!='sunken' and not game_over:
            if self['text']=='':
                self['text']='🚩'
                self['state']='disabled'
            elif self['text']=='🚩':
                self['text']='?'
            elif self['text']=='?':
                self['text']=''
                self['state']='normal'
        c+=1
        c2=0
        for a in range(x):
            for b in range(y):
                if di[(a,b)]['text']=='🚩':
                    c2+=1
        mineleft['text']=f'{mine_num-c2}'
    def plus(self, event):
        global c
        c+=1
    def minus(self, event):
        global c
        global game_on
        global game_over
        global board
        global di
        if c==0:
            pass
        else:
            fc=c
            c=c-1
            sc=c
            if fc==2 and sc==1:
                if not game_over:
                    if self['relief']=='sunken':
                        numf=0
                        numm=0
                        for p in range(self.x-1, self.x+2):
                            for q in range(self.y-1, self.y+2):
                                if p>=0 and q>=0:
                                    try:
                                        if di[(p,q)]['text']=='🚩':
                                            numf+=1
                                        numm+=board[q][p]
                                    except:
                                        pass
                        if numf==numm:
                            for p in range(self.x-1, self.x+2):
                                for q in range(self.y-1, self.y+2):
                                    if p>=0 and q>=0:
                                        try:
                                            if di[(p,q)]['relief']=='raised' and di[(p,q)]['text']!='🚩':
                                                di[(p,q)].invoke()
                                        except:
                                            pass
    def mid(self,event):
        if not game_over:
            if self['relief']=='sunken':
                numf=0
                numm=0
                for p in range(self.x-1, self.x+2):
                    for q in range(self.y-1, self.y+2):
                        if p>=0 and q>=0:
                            try:
                                if di[(p,q)]['text']=='🚩':
                                    numf+=1
                                numm+=board[q][p]
                            except:
                                pass
                if numf==numm:
                    for p in range(self.x-1, self.x+2):
                        for q in range(self.y-1, self.y+2):
                            if p>=0 and q>=0:
                                try:
                                    if di[(p,q)]['relief']=='raised' and di[(p,q)]['text']!='🚩':
                                        di[(p,q)].invoke()
                                except:
                                    pass
    def operate(self):
        self['command']=lambda: click(self.x, self.y)
        self.bind('<Button-3>', self.flag)
        self.bind('<Button-1>',self.plus)
        self.bind('<ButtonRelease-1>',self.minus)
        self.bind('<ButtonRelease-3>',self.minus)
        self.bind('<Button-2>', self.mid)
        self.bind('<Double-Button-1>', self.mid)


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


def gettime():
    global start_time
    global timecount
    global game_on
    if game_on and not game_over:
        ctime=time.time()
        timecount.configure(text=f'{int(ctime-start_time)}')
        root.after(1000,gettime)


# In[11]:


def easy():
    global x
    global y
    global mine_num
    global root
    global frame
    global but
    global game_on
    global game_over
    global di
    global c
    global mineleft
    global start_time
    global timecount
    
    c=0
    
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
    filemenu.add_command(label='Custom', command=custom1)

    but = Button(root, text='😊', command=restarteasy)
    but.pack()
    
    mineleft=Label(root, text=f'{mine_num}', font=('Calibri',16))
    mineleft.place(relx=0.0, rely=0.0)
    
    timecount = Label(root, text='0', font=("Calibri",16), anchor='e')
    timecount.place(rely=0.0, relx=0.8, relwidth=0.2)

    frame = Frame(root)
    frame.place(relx=0.0, rely=30/(25*y+30), relwidth=1.0, relheight=(25*y)/(25*y+30))

    game_on=False
    game_over=False

    di=dict()

    for a in range(x):
        for b in range(y):
            example=s_Button(master=frame, x=a, y=b, font=('Calibri',12,'bold'), bd=3)
            example.place(relx=a/x, rely=b/y, relwidth=1/x, relheight=1/y)
            example.operate()
            di[(a,b)]=example
    
    root.config(menu=menubar)

    root.mainloop()


# In[12]:


def medium():
    global x
    global y
    global mine_num
    global root
    global frame
    global but
    global game_on
    global game_over
    global di
    global c
    global mineleft
    global start_time
    global timecount
    
    c=0
    
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
    filemenu.add_command(label='Custom', command=custom1)

    but = Button(root, text='😊', command=restartmedium)
    but.pack()

    mineleft=Label(root, text=f'{mine_num}', font=('Calibri',16))
    mineleft.place(relx=0.0, rely=0.0)
    
    timecount = Label(root, text='0', font=("Calibri",16), anchor='e')
    timecount.place(rely=0.0, relx=0.8, relwidth=0.2)
    
    frame = Frame(root)
    frame.place(relx=0.0, rely=30/(25*y+30), relwidth=1.0, relheight=(25*y)/(25*y+30))

    game_on=False
    game_over=False

    di=dict()

    for a in range(x):
        for b in range(y):
            example=s_Button(master=frame, x=a, y=b, font=('Calibri',12,'bold'), bd=3)
            example.place(relx=a/x, rely=b/y, relwidth=1/x, relheight=1/y)
            example.operate()
            di[(a,b)]=example
            
    root.config(menu=menubar)

    root.mainloop()


# In[13]:


def hard():
    global x
    global y
    global mine_num
    global root
    global frame
    global but
    global game_on
    global game_over
    global di
    global c
    global mineleft
    global start_time
    global timecount
    
    c=0
    
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
    filemenu.add_command(label='Custom', command=custom1)

    but = Button(root, text='😊', command=restarthard)
    but.pack()

    mineleft=Label(root, text=f'{mine_num}', font=('Calibri',16))
    mineleft.place(relx=0.0, rely=0.0)
    
    timecount = Label(root, text='0', font=("Calibri",16), anchor='e')
    timecount.place(rely=0.0, relx=0.8, relwidth=0.2)
    
    frame = Frame(root)
    frame.place(relx=0.0, rely=30/(25*y+30), relwidth=1.0, relheight=(25*y)/(25*y+30))

    game_on=False
    game_over=False

    di=dict()

    for a in range(x):
        for b in range(y):
            example=s_Button(master=frame, x=a, y=b, font=('Calibri',12,'bold'), bd=3)
            example.place(relx=a/x, rely=b/y, relwidth=1/x, relheight=1/y)
            example.operate()
            di[(a,b)]=example
            
    root.config(menu=menubar)

    root.mainloop()


# In[14]:


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


# In[15]:


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
    
    menubar=Menu(root)
    filemenu=Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Menu', menu=filemenu)
    filemenu.add_command(label='Easy', command=restarteasy)
    filemenu.add_command(label='Medium', command=restartmedium)
    filemenu.add_command(label='Hard', command=restarthard)
    filemenu.add_command(label='Custom', command=custom1)
    
    l0=Label(root, text='Custom Mineboard', font=('Calibri',20))
    l0.pack()
    
    l1=Label(root, text='Number of colums: \n(9~30)', font=('Calibri',15))
    l1.place(relx=0.0, rely=0.15, relwidth=0.5)
    
    l2=Label(root, text='Number of rows: \n(9~24)', font=('Calibri',15))
    l2.place(relx=0.5, rely=0.15, relwidth=0.5)
    
    l3=Label(root, text='x', font=('Calibri',15))
    l3.place(relx=0.4, rely=0.32, relwidth=0.2)
    
    e1=Entry(root, font=('Calibri',15))
    e1.place(relx=0.1, rely=0.34, relwidth=0.3)
    e1.bind('<KeyRelease>', max_mine)
    
    e2=Entry(root, font=('Calibri',15))
    e2.place(relx=0.6, rely=0.34, relwidth=0.3)
    e2.bind('<KeyRelease>', max_mine)
    
    l4=Label(root, text='Number of mines: \n(5~ )', font=('Calibri',15))
    l4.place(rely=0.5, relwidth=1.0)
    
    e3=Entry(root, font=('Calibri',15))
    e3.place(relx=0.35, rely=0.69, relwidth=0.3)
    
    b=Button(root, text='Confirm', font=('Calibri',15), command=lambda: custom2(e1.get(),e2.get(),e3.get()))
    b.place(relx=0.4, rely=0.82, relwidth=0.2)
    
    root.config(menu=menubar)
    
    root.mainloop()


# In[16]:


def restartcustom():
    global x
    global y
    global mine_num
    custom2(x,y,mine_num)


# In[17]:


def custom2(one, two, three):
    global x
    global y
    global mine_num
    global root
    global frame
    global but
    global game_on
    global game_over
    global di
    global m
    global c
    global mineleft
    global start_time
    global timecount
    
    c=0
    
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
            filemenu.add_command(label='Custom', command=custom1)

            but = Button(root, text='😊', command=restartcustom)
            but.pack()

            mineleft=Label(root, text=f'{mine_num}', font=('Calibri',16))
            mineleft.place(relx=0.0, rely=0.0)
            
            timecount = Label(root, text='0', font=("Calibri",16), anchor='e')
            timecount.place(rely=0.0, relx=0.8, relwidth=0.2)

            frame = Frame(root)
            frame.place(relx=0.0, rely=30/(25*y+30), relwidth=1.0, relheight=(25*y)/(25*y+30))

            game_on=False
            game_over=False

            di=dict()

            for a in range(x):
                for b in range(y):
                    example=s_Button(master=frame, x=a, y=b, font=('Calibri',12,'bold'), bd=3)
                    example.place(relx=a/x, rely=b/y, relwidth=1/x, relheight=1/y)
                    example.operate()
                    di[(a,b)]=example

            root.config(menu=menubar)

            root.mainloop()
        else:
            tkinter.messagebox.showinfo("", "Invalid input!")
    except:
        tkinter.messagebox.showinfo("", "Invalid input!")


# In[18]:


easy()

