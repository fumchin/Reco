#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog

def openNewFile():
    print(filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))
def openFile():
    print("openFile")
def save():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))