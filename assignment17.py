#Q1.
from Tkinter import *
root= Tk.Tk()
bt=Tk.Button(root, text='close',width=25,command=root.destroy)
w = Tk.Label(root, text="Hello World")
bt.pack()
w.pack()
root.mainloop()
 #Q2.

def callback():
    print "click!"
b = Tk.Button(root, text="OK", command=callback)
b.pack()
root.mainloop()

#Q3.

from Tkinter import *

root = Tk()
frame = Frame(root)#create frame
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

w = Tk.Label(root, text="HUGABUGABUGA")#create label
bt=Tk.Button(root, text='close',width=25,command=root.destroy)#create button
bt=Tk.Button(root, text='close',width=25,command=Label)
root.mainloop()#used to hold output

#Q4
def printtext(): #function to extract the text from the widget
    global e
    string = e.get()
    print string

from Tkinter import *
root = Tk()

root.title('Name')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='okay',command=printtext) #button which will print text
b.pack(side='bottom')
root.mainloop()