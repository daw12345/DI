import tkinter as tk

def changeColor():

    root.config(bg=v1.get())

root = tk.Tk()
root.geometry("300x300")


v1 = tk.StringVar(value="none")


button1 = tk.Radiobutton(root, text="green", variable=v1, value="green", command=changeColor)
button1.pack()

button2 = tk.Radiobutton(root, text="red", variable=v1, value="red", command=changeColor)
button2.pack()

button3 = tk.Radiobutton(root, text="blue", variable=v1, value="blue", command=changeColor)
button3.pack()




root.mainloop()
