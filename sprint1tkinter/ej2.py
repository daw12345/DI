import tkinter as tk


def showText():
    tag.pack()


def closeWindow():
    root.destroy()

root = tk.Tk()
root.geometry("300x300")

tag= tk.Label(root, text="tachan!")

button1 = tk.Button(root, text="button one",command=showText)
button1.pack()

button2 = tk.Button(root, text="button two",command=closeWindow)
button2.pack()


root.mainloop()