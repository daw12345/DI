import tkinter as tk

def swapText():
    tag3.config(text="oH!")
    

root = tk.Tk()
root.geometry("300x300")


tag1 = tk.Label(root, text="Welcome")
tag1.pack()
tag2 = tk.Label(root, text="Carlos")
tag2.pack()
tag3 = tk.Label(root, text="Change this text")
tag3.pack()


buttom = tk.Button(root, text="a simple buttom", command=swapText)
buttom.pack()

root.mainloop()