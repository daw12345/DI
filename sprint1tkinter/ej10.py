import tkinter as tk


root = tk.Tk()
root.geometry("2000x2000")



frame = tk.Frame(root)
frame.pack(expand=True, fill="both")


text_widget = tk.Text(frame, wrap="word", undo=True)
text_widget.pack(side="left", expand=True, fill="both")


scrollbar = tk.Scrollbar(frame, orient="vertical", command=text_widget.yview)
scrollbar.pack(side="right", fill="y")


text_widget.config(yscrollcommand=scrollbar.set)


texto_largo = """Este es un texto largo que contiene varios párrafos.
Puedes usar la barra de desplazamiento para moverte a través del contenido.

Párrafo 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ultrices arcu in justo sollicitudin, et dapibus nunc scelerisque. Integer non lorem eget metus condimentum efficitur. Fusce ac suscipit felis.

Párrafo 2: Aenean ac tincidunt enim. Nulla vitae justo in magna malesuada sollicitudin. Curabitur faucibus metus eget lacus scelerisque, nec malesuada mi tincidunt. Nam aliquam odio id felis fermentum, nec lobortis erat vehicula.

Párrafo 3: Cras accumsan turpis nec metus vehicula vehicula. Quisque dignissim lacus at magna tempus, non dignissim enim elementum. Nam eu varius mi. Mauris luctus nibh at purus fringilla, a pulvinar sem bibendum.

Párrafo 4: Fusce fringilla risus id lorem interdum gravida. Ut vel venenatis purus. Donec sed dapibus mauris, a finibus lectus. Nullam pharetra, ligula et luctus fringilla, erat libero sollicitudin risus, vel facilisis nunc orci ac dui.

Párrafo 5: Proin aliquet turpis sit amet lectus condimentum, sit amet malesuada purus consequat. Nulla facilisi. Nam congue fringilla sapien, id euismod velit pharetra ut.

Párrafo 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ultrices arcu in justo sollicitudin, et dapibus nunc scelerisque. Integer non lorem eget metus condimentum efficitur. Fusce ac suscipit felis.

Párrafo 2: Aenean ac tincidunt enim. Nulla vitae justo in magna malesuada sollicitudin. Curabitur faucibus metus eget lacus scelerisque, nec malesuada mi tincidunt. Nam aliquam odio id felis fermentum, nec lobortis erat vehicula.

Párrafo 3: Cras accumsan turpis nec metus vehicula vehicula. Quisque dignissim lacus at magna tempus, non dignissim enim elementum. Nam eu varius mi. Mauris luctus nibh at purus fringilla, a pulvinar sem bibendum.

Párrafo 4: Fusce fringilla risus id lorem interdum gravida. Ut vel venenatis purus. Donec sed dapibus mauris, a finibus lectus. Nullam pharetra, ligula et luctus fringilla, erat libero sollicitudin risus, vel facilisis nunc orci ac dui.

Párrafo 5: Proin aliquet turpis sit amet lectus condimentum, sit amet malesuada purus consequat. Nulla facilisi. Nam congue fringilla sapien, id euismod velit pharetra ut.

Párrafo 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ultrices arcu in justo sollicitudin, et dapibus nunc scelerisque. Integer non lorem eget metus condimentum efficitur. Fusce ac suscipit felis.

Párrafo 2: Aenean ac tincidunt enim. Nulla vitae justo in magna malesuada sollicitudin. Curabitur faucibus metus eget lacus scelerisque, nec malesuada mi tincidunt. Nam aliquam odio id felis fermentum, nec lobortis erat vehicula.

Párrafo 3: Cras accumsan turpis nec metus vehicula vehicula. Quisque dignissim lacus at magna tempus, non dignissim enim elementum. Nam eu varius mi. Mauris luctus nibh at purus fringilla, a pulvinar sem bibendum.

Párrafo 4: Fusce fringilla risus id lorem interdum gravida. Ut vel venenatis purus. Donec sed dapibus mauris, a finibus lectus. Nullam pharetra, ligula et luctus fringilla, erat libero sollicitudin risus, vel facilisis nunc orci ac dui.

Párrafo 5: Proin aliquet turpis sit amet lectus condimentum, sit amet malesuada purus consequat. Nulla facilisi. Nam congue fringilla sapien, id euismod velit pharetra ut.

Párrafo 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ultrices arcu in justo sollicitudin, et dapibus nunc scelerisque. Integer non lorem eget metus condimentum efficitur. Fusce ac suscipit felis.

Párrafo 2: Aenean ac tincidunt enim. Nulla vitae justo in magna malesuada sollicitudin. Curabitur faucibus metus eget lacus scelerisque, nec malesuada mi tincidunt. Nam aliquam odio id felis fermentum, nec lobortis erat vehicula.

Párrafo 3: Cras accumsan turpis nec metus vehicula vehicula. Quisque dignissim lacus at magna tempus, non dignissim enim elementum. Nam eu varius mi. Mauris luctus nibh at purus fringilla, a pulvinar sem bibendum.

Párrafo 4: Fusce fringilla risus id lorem interdum gravida. Ut vel venenatis purus. Donec sed dapibus mauris, a finibus lectus. Nullam pharetra, ligula et luctus fringilla, erat libero sollicitudin risus, vel facilisis nunc orci ac dui.

Párrafo 5: Proin aliquet turpis sit amet lectus condimentum, sit amet malesuada purus consequat. Nulla facilisi. Nam congue fringilla sapien, id euismod velit pharetra ut.

Párrafo 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ultrices arcu in justo sollicitudin, et dapibus nunc scelerisque. Integer non lorem eget metus condimentum efficitur. Fusce ac suscipit felis.

Párrafo 2: Aenean ac tincidunt enim. Nulla vitae justo in magna malesuada sollicitudin. Curabitur faucibus metus eget lacus scelerisque, nec malesuada mi tincidunt. Nam aliquam odio id felis fermentum, nec lobortis erat vehicula.

Párrafo 3: Cras accumsan turpis nec metus vehicula vehicula. Quisque dignissim lacus at magna tempus, non dignissim enim elementum. Nam eu varius mi. Mauris luctus nibh at purus fringilla, a pulvinar sem bibendum.

Párrafo 4: Fusce fringilla risus id lorem interdum gravida. Ut vel venenatis purus. Donec sed dapibus mauris, a finibus lectus. Nullam pharetra, ligula et luctus fringilla, erat libero sollicitudin risus, vel facilisis nunc orci ac dui.

Párrafo 5: Proin aliquet turpis sit amet lectus condimentum, sit amet malesuada purus consequat. Nulla facilisi. Nam congue fringilla sapien, id euismod velit pharetra ut.

Párrafo 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ultrices arcu in justo sollicitudin, et dapibus nunc scelerisque. Integer non lorem eget metus condimentum efficitur. Fusce ac suscipit felis.

Párrafo 2: Aenean ac tincidunt enim. Nulla vitae justo in magna malesuada sollicitudin. Curabitur faucibus metus eget lacus scelerisque, nec malesuada mi tincidunt. Nam aliquam odio id felis fermentum, nec lobortis erat vehicula.

Párrafo 3: Cras accumsan turpis nec metus vehicula vehicula. Quisque dignissim lacus at magna tempus, non dignissim enim elementum. Nam eu varius mi. Mauris luctus nibh at purus fringilla, a pulvinar sem bibendum.

Párrafo 4: Fusce fringilla risus id lorem interdum gravida. Ut vel venenatis purus. Donec sed dapibus mauris, a finibus lectus. Nullam pharetra, ligula et luctus fringilla, erat libero sollicitudin risus, vel facilisis nunc orci ac dui.

Párrafo 5: Proin aliquet turpis sit amet lectus condimentum, sit amet malesuada purus consequat. Nulla facilisi. Nam congue fringilla sapien, id euismod velit pharetra ut.

Párrafo 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ultrices arcu in justo sollicitudin, et dapibus nunc scelerisque. Integer non lorem eget metus condimentum efficitur. Fusce ac suscipit felis.

Párrafo 2: Aenean ac tincidunt enim. Nulla vitae justo in magna malesuada sollicitudin. Curabitur faucibus metus eget lacus scelerisque, nec malesuada mi tincidunt. Nam aliquam odio id felis fermentum, nec lobortis erat vehicula.

Párrafo 3: Cras accumsan turpis nec metus vehicula vehicula. Quisque dignissim lacus at magna tempus, non dignissim enim elementum. Nam eu varius mi. Mauris luctus nibh at purus fringilla, a pulvinar sem bibendum.

Párrafo 4: Fusce fringilla risus id lorem interdum gravida. Ut vel venenatis purus. Donec sed dapibus mauris, a finibus lectus. Nullam pharetra, ligula et luctus fringilla, erat libero sollicitudin risus, vel facilisis nunc orci ac dui.

Párrafo 5: Proin aliquet turpis sit amet lectus condimentum, sit amet malesuada purus consequat. Nulla facilisi. Nam congue fringilla sapien, id euismod velit pharetra ut.

Párrafo 1: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ultrices arcu in justo sollicitudin, et dapibus nunc scelerisque. Integer non lorem eget metus condimentum efficitur. Fusce ac suscipit felis.

Párrafo 2: Aenean ac tincidunt enim. Nulla vitae justo in magna malesuada sollicitudin. Curabitur faucibus metus eget lacus scelerisque, nec malesuada mi tincidunt. Nam aliquam odio id felis fermentum, nec lobortis erat vehicula.

Párrafo 3: Cras accumsan turpis nec metus vehicula vehicula. Quisque dignissim lacus at magna tempus, non dignissim enim elementum. Nam eu varius mi. Mauris luctus nibh at purus fringilla, a pulvinar sem bibendum.

Párrafo 4: Fusce fringilla risus id lorem interdum gravida. Ut vel venenatis purus. Donec sed dapibus mauris, a finibus lectus. Nullam pharetra, ligula et luctus fringilla, erat libero sollicitudin risus, vel facilisis nunc orci ac dui.

Párrafo 5: Proin aliquet turpis sit amet lectus condimentum, sit amet malesuada purus consequat. Nulla facilisi. Nam congue fringilla sapien, id euismod velit pharetra ut.
"""

text_widget.insert(tk.END, texto_largo)


root.mainloop()
