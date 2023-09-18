import random

# Diccionario de criaturas mágicas en el bosque
criaturas_magicas = {
    "duende": "¡Un duende apareció y te lanzó un hechizo!",
    "hada": "Te encontraste con un hada que te concedió un deseo.",
    "dragón": "Un dragón bloquea tu camino. ¿Qué harás?",
    "gnomo": "Un pequeño gnomo te desafía a un juego de adivinanzas.",
    "unicornio": "Un majestuoso unicornio aparece y te ofrece su ayuda.",
}

# Lista de objetos que el jugador puede encontrar
objetos = ["poción mágica", "mapa del tesoro", "espada afilada", "antorcha"]

# Tupla de caminos posibles
caminos = ("izquierda", "derecha")

# Inventario del jugador
mochila = []

# Nivel actual del jugador
nivel = 1

# Función para iniciar el juego
def jugar_aventura():
    print("Bienvenido a la Aventura en el Bosque Encantado")
    print("Estás en la entrada del bosque. Debes tomar decisiones para avanzar.")
    print("Tu objetivo es encontrar el tesoro oculto al final del bosque.\n")

    while nivel <= 3:
        print(f"Nivel {nivel}:")
        eleccion = input("¿Qué camino tomarás, izquierda o derecha? ").lower()

        if eleccion not in caminos:
            print("¡Esa no es una elección válida! Elige izquierda o derecha.")
        else:
            if eleccion == "izquierda":
                encuentro_criatura()
            else:
                encontrar_objeto()
        
        nivel += 1

    print("¡Felicidades! Has llegado al final del bosque y encontrado el tesoro.")
    print("Tu aventura ha llegado a su fin.")

# Función para el encuentro con una criatura mágica
def encuentro_criatura():
    criatura = random.choice(list(criaturas_magicas.keys()))
    print(f"\n¡{criatura.capitalize()}!")
    print(criaturas_magicas[criatura])
    
    decision = input("¿Qué harás? (atacar/huir): ").lower()
    
    if decision == "atacar":
        print(f"¡Has derrotado al {criatura} y puedes continuar!")
    elif decision == "huir":
        print("Escapas del peligro y continuas tu camino.")
    else:
        print("Decisión no válida. Elige atacar o huir.")

# Función para encontrar un objeto
def encontrar_objeto():
    objeto_encontrado = random.choice(objetos)
    print(f"\nEncontraste un {objeto_encontrado}.")
    decision = input("¿Deseas recogerlo? (si/no): ").lower()
    
    if decision == "si":
        mochila.append(objeto_encontrado)
        print(f"Has recogido el {objeto_encontrado} y lo guardaste en tu mochila.")
    elif decision == "no":
        print("Decides dejar el objeto y continuar tu camino.")
    else:
        print("Decisión no válida. Elige si o no.")

# Iniciar el juego
jugar_aventura()
