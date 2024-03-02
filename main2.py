import random

def generar_pregunta():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    respuesta_correcta = num1 * num2
    return f"¿Cuánto es {num1} multiplicado por {num2}?", respuesta_correcta

def turno_jugador():
    pregunta, respuesta_correcta = generar_pregunta()
    print(pregunta)
    respuesta_jugador = input("Respuesta: ")
    try:
        respuesta_jugador = int(respuesta_jugador)
        if respuesta_jugador == respuesta_correcta:
            print("¡Respuesta correcta!")
            return True
        else:
            print("Respuesta incorrecta. La respuesta correcta era:", respuesta_correcta)
            return False
    except ValueError:
        print("Por favor ingresa un número válido.")
        return False

def turno_IA():
    pregunta, respuesta_correcta = generar_pregunta()
    print("Turno de la IA:")
    print(pregunta)
    print("La IA está pensando...")
    # Simulación simple de la IA
    respuesta_IA = respuesta_correcta
    print("La IA responde:", respuesta_IA)

def jugar():
    print("Bienvenido al juego de tablas de multiplicar!")
    while True:
        # Turno del jugador
        jugador_correcto = turno_jugador()
        if not jugador_correcto:
            break
        
        # Turno de la IA
        turno_IA()

        continuar = input("¿Quieres continuar jugando? (s/n): ")
        if continuar.lower() != 's':
            print("¡Gracias por jugar!")
            break

# Iniciar el juego
jugar()
