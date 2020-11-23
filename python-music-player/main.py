#!/usr/bin/env python3
# this is main.py file
# we will build our gui here

import tkinter as tk
import guiCommand.menubarCommand as menubarAction 

# =======================================================================
# build main window
# =======================================================================
main_window = tk.Tk()
main_window.title('my recorder')
main_window.geometry('800x600')
main_window.configure(background = 'white')

# =======================================================================
# build menubar
# =======================================================================
menubar = tk.Menu(main_window)
menubar.configure(background = 'white')
# Adding File Menu and commands 
file = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='New File', command = menubarAction.openNewFile) 
file.add_command(label ='Open...', command = menubarAction.openFile) 
file.add_command(label ='Save', command = menubarAction.save) 
file.add_separator() 
file.add_command(label ='Exit', command = main_window.destroy) 
  
# Adding Edit Menu and commands 
edit = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = None) 
edit.add_command(label ='Copy', command = None) 
edit.add_command(label ='Paste', command = None) 
edit.add_command(label ='Select All', command = None) 
edit.add_separator() 
edit.add_command(label ='Find...', command = None) 
edit.add_command(label ='Find again', command = None) 
  
# Adding Help Menu 
help_ = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Tk Help', command = None) 
help_.add_command(label ='Demo', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = None) 

# =======================================================================
# build some important fumction button( play, stop, pause, add track, record)
# top header
# =======================================================================
topFrame = tk.Frame(main_window)
topFrame.configure(background = "white")
play_img = tk.PhotoImage(file = "./../docs/images/button_images/play_button.png")
stop_img = tk.PhotoImage(file = "./../docs/images/button_images/stop_button.png")
pause_img = tk.PhotoImage(file = "./../docs/images/button_images/pause_button.png")

play_button = tk.Button(topFrame, text='Play')
play_button.config(image = play_img)
play_button.configure(background="white")
play_button.pack(side=tk.LEFT, padx=2)

stop_button = tk.Button(topFrame, text='Stop')
stop_button.config(image = stop_img)
stop_button.configure(background="white")
stop_button.pack(side=tk.LEFT,padx=2)

pause_button = tk.Button(topFrame, text='Pause')
pause_button.config(image = pause_img)
pause_button.configure(background="white")
pause_button.pack(side=tk.LEFT, padx=2)  
topFrame.pack(side=tk.TOP, anchor = tk.NW, pady=2)

# =======================================================================
#run
# =======================================================================
main_window.config(menu = menubar)
main_window.mainloop()
