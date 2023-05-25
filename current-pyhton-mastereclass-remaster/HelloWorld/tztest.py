try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x400+8+400")

label = tkinter.Label(mainWindow, text="Hello world")
label.pack(side="top")

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side="left")

canvas = tkinter.Canvas(mainWindow, relief="raised", borderwidth=1)
canvas.pack(side="left",)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side="right")

button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")
button4 = tkinter.Button(mainWindow, text="button4")
button5 = tkinter.Button(mainWindow, text="button5")
button4.pack(side="right", anchor="center")
button1.pack(side="right", anchor="n")
button2.pack(side="left", anchor="s")
button3.pack(side="left", anchor="e")

mainWindow.mainloop()