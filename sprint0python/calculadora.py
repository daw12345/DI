import operaciones

while True:
    print("Introduce dos números para realizar operaciones:")
    answer1 = input("(Primer número):\n ")
    answer2 = input("(Segundo número):\n ")

    try:
        answer1 = int(answer1)
        answer2 = int(answer2)
        
    except ValueError:
        print("Por favor, introduce números válidos, esto es una calculadora seria.")
        continue

    while True:
        options = ['suma', 'resta', 'producto', 'division']

        print("Pipiolo, ¿qué operación deseas realizar? (Introduce 'suma', 'resta', 'producto' o 'division'):")
        answer3 = input().strip()

        if answer3 in options:
            result = getattr(operaciones, answer3)(answer1, answer2)
            print(f"El resultado de la {answer3} es: {result}\n")
        else:
            print('Has introducido mal el tipo de operación...')
            continue

        while True:
            answer4 = input('¿Deseas seguir con más operaciones? (responde "s" para sí, "n" para no): \n').strip().lower()
            
            if answer4 == 's':
                break  # Rompe el bucle y vuelve a pedir números y operación
            elif answer4 == 'n':
                print("¡Hasta luego!")
                exit()  # Termina el programa
            else:
                print('Error, introduce "s" para sí, "n" para no:')
                continue
        break  # Rompe el bucle interior para volver al inicio del programa
