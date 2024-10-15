import tkinter as tk

def mostrar():
    if entry and tag3:
        tag3.config(text=entry.get())
        tag3.pack()

def borrar():
    if tag3:
        tag3.pack_forget()

root = tk.Tk()
root.geometry("300x300")

frame1 = tk.Frame(root, bg="red", bd=2, relief="sunken")
frame1.pack()

tag1 = tk.Label(frame1, text="Etiqueta 1" ,bg="orange")
tag1.pack()

tag2 = tk.Label(frame1, text="Etiqueta 2" ,bg="brown")
tag2.pack()

entry = tk.Entry(frame1)
entry.pack()

frame2 = tk.Frame(root, bg="blue", bd=2, relief="sunken")
frame2.pack()

button1 = tk.Button(frame2, text="mostrar", command=mostrar)
button1.pack()

button2 = tk.Button(frame2, text="borrar", command=borrar)
button2.pack()

tag3 = tk.Label(frame2, text="")

root.mainloop()
