def suma(num1, num2):
    return num1 + num2 if type(num1) == int and type(num2) == int else print(f"Introduce números válidos, melón")

def resta(num1, num2):
    return num1 - num2 if type(num1) == int and type(num2) == int else print(f"Introduce números válidos, melón")

def producto(num1, num2):
    return num1 * num2 if type(num1) == int and type(num2) == int else print(f"Introduce números válidos, melón")

def division(num1, num2):
    return "indefinido" if num1 == 0 and num2 == 0 else (0 if num1 == 0 and isinstance(num2, int) else num1 / num2 if isinstance(num1, int) and isinstance(num2, int) and num2 != 0 else "∞" if num2 == 0 and isinstance(num1, int) else "Introduce números válidos, melón")
