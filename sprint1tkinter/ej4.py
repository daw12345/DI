import tkinter as tk

def state():

    if var1.get():
        tag1.config(text="Madrugar selected")
    else:
        tag1.config(text="(Madrugar no selected)")

    if var2.get():
        tag2.config(text="Bostezar selected")
    else:
        tag2.config(text="(Bostezar no selected)")

    if var3.get():
        tag3.config(text="Llorar selected")
    else:
        tag3.config(text="(Llorar no selected)")

root = tk.Tk()
root.geometry("300x300")


var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

check1 = tk.Checkbutton(root, text="Madrugar", variable=var1, command=state)
check2 = tk.Checkbutton(root, text="Bostezar", variable=var2, command=state)
check3 = tk.Checkbutton(root, text="LLorar", variable=var3, command=state)

check1.pack()
check2.pack()
check3.pack()


tag1 = tk.Label(root, text=f"(Madrugar no selected)")
tag2 = tk.Label(root, text=f"(Bostezar no selected)")
tag3 = tk.Label(root, text=f"(Llorar no selected)")

tag1.pack()
tag2.pack()
tag3.pack()

root.mainloop()
