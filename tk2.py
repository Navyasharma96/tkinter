from tkinter import *
def donothing():
  filewin = Toplevel(root)
  button = Button( text="Do nothing button")
  button.pack()
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = donothing)
filemenu.add_command(label = "Open", command = donothing)
filemenu.add_command(label = "Save", command = donothing)
filemenu.add_command(label = "Save as...", command = donothing)
filemenu.add_command(label = "Close", command = donothing)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Undo", command = donothing)
editmenu.add_separator()
editmenu.add_command(label = "Cut", command = donothing)
editmenu.add_command(label = "Copy", command = donothing)
editmenu.add_command(label = "Paste", command = donothing)
editmenu.add_command(label = "Delete", command = donothing)
editmenu.add_command(label = "Select All", command = donothing)
menubar.add_cascade(label = "Edit", menu = editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Help Index", command = donothing)
helpmenu.add_command(label = "About...", command = donothing)
menubar.add_command(label="Navigate", command=donothing)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "clas....", command = donothing)
editmenu.add_command(label = "File.....", command = donothing)
editmenu.add_command(label = "Symbol", command = donothing)
editmenu.add_command(label = "Custtom Foldinf....", command = donothing)
menubar.add_cascade(label="Code", command=donothing)
edditmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label = "Gentrate", command = donothing)
menubar.add_cascade(label="Refactor",command=donothing)
menubar.add_cascade(label="Run",command=donothing)
menubar.add_cascade(label="Tools",command=donothing)
menubar.add_cascade(label = "Help", menu = helpmenu)
root.config(menu = menubar)
root.mainloop()