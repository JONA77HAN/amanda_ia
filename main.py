import random

def preguntar_pregunta(pregunta):
    respuesta = input(pregunta + " (responde sí o no): ").lower().strip()
    while respuesta not in ["si", "no"]:
        respuesta = input("Por favor, responde sí o no: ").lower().strip()
    return respuesta

def main():
    print("Hola, soy Amanda, una IA. ¿Cómo estás?")
    respuesta = preguntar_pregunta("¿Te gustaría jugar un juego?")
    
    if respuesta == "si":
        print("Genial, vamos a empezar.")
        print("Estoy pensando en un número del 1 al 10. Adivina cuál es.")
        numero_aleatorio = random.randint(1, 10)
        
        intentos = 0
        while True:
            intento = int(input("Introduce tu número: "))
            intentos += 1
            
            if intento < numero_aleatorio:
                print("El número que estoy pensando es mayor.")
            elif intento > numero_aleatorio:
                print("El número que estoy pensando es menor.")
            else:
                print(f"Felicidades, has adivinado el número en {intentos} intentos.")
                break
        
    else:
        print("Oh, bueno. Tal vez en otro momento. Adiós.")

if __name__ == "__main__":
    main()
