import tkinter as tk

def show():
    tag2= tk.Label(root, text=f"Hi {entry.get()}, you are güelcom")
    tag2.pack()




root = tk.Tk()
root.geometry("300x300")

tag= tk.Label(root, text="Enter your name")

entry = tk.Entry(root, width=30)
entry.pack()

button1 = tk.Button(root, text="enter",command=show)
button1.pack()




root.mainloop()