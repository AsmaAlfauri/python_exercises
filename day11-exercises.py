# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:14:16 2019

@author: Asma Alfauri
"""
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.colorchooser import *

#Ex-1:
def fun ():
    if value1.get() == "Orange" and value2.get() == "CodingAcademy" :
         z = messagebox.showinfo("Login", "Successful login")
         print (z)
         if z == "ok":
             parent.destroy()
    else:
         messagebox.showinfo("Login", "Wrong User Name or Password")

parent = Tk()
value1 = StringVar()
value2 = StringVar()
name = Label(parent, text = "Name").grid(row=0, column = 0)
e1 = Entry(parent, textvariable= value1).grid(row = 0, column =1)
password = Label(parent, text ="Password").grid(row = 1, column = 0)
e2 = Entry(parent, textvariable= value2).grid(row = 1, column =1)
submit = Button(parent, text="Submit", command= fun).grid(row = 4, column = 0)
parent.mainloop()

#Ex-2: 
def open_child1():
    dialog_title=""
    dialog_text="This is a message"
    answer=messagebox.showinfo(dialog_title,dialog_text)

def open_child2():
    top=Tk()
    top.title('Child window 2')
    top.geometry('400x250')
    name=Label(top,text="Emy Number").place(x=30,y=50)
    email=Label(top,text="Emy Name").place(x=30,y=90)
    e1=Entry(top).place(x=100,y=50)
    e2=Entry(top).place(x=100,y=90)
    button=Button(top,text="Quit",command=top.destroy).place(x=150,y=150)
    button.pack()
    top.mainloop()

def open_child3():
    win=Tk()
    win.title("Welcome")
    win.geometry('350x200')
    txt=scrolledtext.ScrolledText(win,width=40,height=10)
    txt.grid(column=0,row=0)
    textBox=scrolledtext.ScrolledText(win,width=40,height=20,wrap=WORD)
    for r in range(20):
       textBox.insert(END,"The count is : "+str(r)+"/n")
    textBox()
    win.mainloop()


root = Tk()
root.title('Root window')

Button(root, text = 'open child window 1', command = open_child1).grid()
Button(root, text = 'open child window 2', command = open_child2).grid()
Button(root, text = 'open child window 3', command = open_child3).grid()

root.mainloop()

#Ex-3:

root = Tk()
def getcolor():
    color=askcolor()
    root.config(background=color[1])
Button(root,text="select",command=getcolor).pack()
mainloop()






































































