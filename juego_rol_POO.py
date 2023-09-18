import random

class Jugador:
    def __init__(self):
        self.mochila = []
        self.nivel = 1

    def avanzar_nivel(self):
        self.nivel += 1

class Bosque:
    def __init__(self):
        self.caminos = ("izquierda", "derecha")
        self.criaturas_magicas = {
            "duende": "¡Un duende apareció y te lanzó un hechizo!",
            "hada": "Te encontraste con un hada que te concedió un deseo.",
            "dragón": "Un dragón bloquea tu camino. ¿Qué harás?",
            "gnomo": "Un pequeño gnomo te desafía a un juego de adivinanzas.",
            "unicornio": "Un majestuoso unicornio aparece y te ofrece su ayuda.",
        }
        self.objetos = ["poción mágica", "mapa del tesoro", "espada afilada", "antorcha"]

    def tomar_decision(self):
        return input("¿Qué camino tomarás, izquierda o derecha? ").lower()

class Juego:
    def __init__(self):
        self.jugador = Jugador()
        self.bosque = Bosque()

    def jugar(self):
        print("Bienvenido a la Aventura en el Bosque Encantado")
        print("Estás en la entrada del bosque. Debes tomar decisiones para avanzar.")
        print("Tu objetivo es encontrar el tesoro oculto al final del bosque.\n")

        while self.jugador.nivel <= 3:
            print(f"Nivel {self.jugador.nivel}:")
            eleccion = self.bosque.tomar_decision()

            if eleccion not in self.bosque.caminos:
                print("¡Esa no es una elección válida! Elige izquierda o derecha.")
            else:
                if eleccion == "izquierda":
                    self.encuentro_criatura()
                else:
                    self.encontrar_objeto()

            self.jugador.avanzar_nivel()

        print("¡Felicidades! Has llegado al final del bosque y encontrado el tesoro.")
        print("Tu aventura ha llegado a su fin.")

    def encuentro_criatura(self):
        criatura = random.choice(list(self.bosque.criaturas_magicas.keys()))
        print(f"\n¡{criatura.capitalize()}!")
        print(self.bosque.criaturas_magicas[criatura])

        decision = input("¿Qué harás? (atacar/huir): ").lower()

        if decision == "atacar":
            print(f"¡Has derrotado al {criatura} y puedes continuar!")
        elif decision == "huir":
            print("Escapas del peligro y continuas tu camino.")
        else:
            print("Decisión no válida. Elige atacar o huir.")

    def encontrar_objeto(self):
        objeto_encontrado = random.choice(self.bosque.objetos)
        print(f"\nEncontraste un {objeto_encontrado}.")
        decision = input("¿Deseas recogerlo? (si/no): ").lower()

        if decision == "si":
            self.jugador.mochila.append(objeto_encontrado)
            print(f"Has recogido el {objeto_encontrado} y lo guardaste en tu mochila.")
        elif decision == "no":
            print("Decides dejar el objeto y continuar tu camino.")
        else:
            print("Decisión no válida. Elige si o no.")

# Iniciar el juego
juego = Juego()
juego.jugar()
