import random

# Base de datos de preguntas y respuestas
base_datos = {
    "¿Qué animal es conocido como el 'Rey de la selva'?": "León",
    "¿Qué animal tiene una joroba en la espalda?": "Camello",
    "¿Qué animal puede volar y hace 'pio pio'?": "Pájaro",
    "¿Qué animal es famoso por su trompa larga?": "Elefante",
    "¿Qué animal vive en el agua y respira a través de branquias?": "Pez",
    "¿Qué animal es el más rápido en tierra?": "Guepardo",
    "¿Qué animal es conocido por ser el 'Mejor amigo del hombre'?": "Perro",
    "¿Qué animal es famoso por su mancha en el cuerpo?": "Jirafa",
    "¿Qué animal tiene una bolsa en su vientre para llevar a sus crías?": "Canguro",
    "¿Qué animal es famoso por su melena?": "León",
    "¿Qué animal es conocido por su cola rayada y es propenso a comer zanahorias?": "Conejo",
    "¿Qué animal es famoso por ser un símbolo de sabiduría?": "Búho",
    "¿Qué animal tiene una armadura en su espalda?": "Tortuga",
    "¿Qué animal es famoso por su pelaje blanco y negro?": "Panda",
    "¿Qué animal es famoso por su largo cuello?": "Jirafa",
    "¿Qué animal es conocido por ser el más grande del mundo?": "Ballena Azul",
    "¿Qué animal es conocido por ser un depredador de la selva?": "Tigre",
    "¿Qué animal tiene una cola larga y prensil?": "Mono",
    "¿Qué animal es conocido por ser un roedor muy común en las ciudades?": "Ratón",
    "¿Qué animal tiene una corona de espinas en su cabeza?": "Erizo",
    "¿Qué animal tiene una melena en el cuello y es conocido por ser un cazador nocturno?": "Leopardo",
    "¿Qué animal es famoso por su velocidad y se utiliza en carreras?": "Caballo",
    "¿Qué animal tiene una cola larga y es capaz de trepar árboles?": "Ardilla",
    "¿Qué animal es famoso por su plumaje colorido?": "Pájaro",
    "¿Qué animal es conocido por ser un símbolo de longevidad?": "Tortuga",
    "¿Qué animal es conocido por ser un insecto con rayas amarillas y negras?": "Abeja",
    "¿Qué animal es famoso por su gran trompa y es el más grande del mundo?": "Elefante",
    "¿Qué animal es famoso por su habilidad para nadar y atrapar peces con sus garras?": "Oso",
    "¿Qué animal es conocido por ser un mamífero marino y realizar saltos acrobáticos?": "Delfín",
    "¿Qué animal es famoso por ser un depredador y aullar a la luna?": "Lobo",
    "¿Qué animal tiene una cola larga y es capaz de regenerarla si se corta?": "Lagarto",
    "¿Qué animal es famoso por ser el más grande de los felinos?": "Tigre",
    "¿Qué animal tiene una larga trompa y es conocido por ser un símbolo de buena suerte?": "Elefante"
}

def generar_pregunta():
    pregunta = random.choice(list(base_datos.keys()))
    respuesta_correcta = base_datos[pregunta]
    return pregunta, respuesta_correcta

def turno_jugador():
    pregunta, respuesta_correcta = generar_pregunta()
    print(pregunta)
    respuesta_jugador = input("Respuesta: ")
    if respuesta_jugador.lower() == respuesta_correcta.lower():
        print("¡Respuesta correcta!")
        return True
    else:
        print("Respuesta incorrecta. La respuesta correcta era:", respuesta_correcta)
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
    print("Bienvenido al juego de preguntas sobre animales!")
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
