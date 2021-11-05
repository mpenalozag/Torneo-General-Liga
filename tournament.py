from mathFunctions import closestPower
import random
from colorama import Fore, Style, Back


class Tournament:
    # Recibe como input una lista con los participantes del torneo y un int con la cantidad de participantes.
    def __init__(self, participantes, cantidad_participantes):
        self.participantes = participantes
        self.participantes_sin_asignar = cantidad_participantes
        self.cantidad_participantes = cantidad_participantes
        self.points = {}
        self.describeTournament()
        self.setLeaderboard()

    # Función para printear un Match Up

    def printMatchUp(self, player_1, player_2):
        print(" Match Up ")
        print("----------")
        print(f"{player_1} vs {player_2}\n")
        print("----------")
        print(f"Selecciona el resultado")
        print(f"1) Gana {player_1}")
        print(f"2) Gana {player_2}")
        print("3) Empate\n")


    # Función que describe el torneo.
    def describeTournament(self):
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        print(Fore.LIGHTMAGENTA_EX)
        print(f"Torneo con {self.cantidad_participantes} participantes!")
        print(Style.RESET_ALL)
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
        print(Fore.LIGHTYELLOW_EX)
        print(" Participantes ")
        print(Style.RESET_ALL)
        print("---------------")
        for i in range(self.cantidad_participantes):
            print(f"{i+1}) {self.participantes[i]}")
        print("---------------\n\n\n")

    # Función que setea la tabla de posiciones.
    def setLeaderboard(self):
        # A cada participante le asignamos un espacio en el diccionario.
        # El value asignado a cada participante corresponde a los puntos de ese participante.
        for participante in self.participantes:
            self.points[participante] = 0


    # Función que enfreta a 2 competidores y permite seleccionar quien gana
    def matchUp(self, player_1, player_2):
        # Printeamos el match up.
        self.printMatchUp(player_1, player_2)
        # Recibimos el resultado por parte del usuario.
        resultado = int(input())
        # Manejamos el resultado.
        if (resultado == 1):
            self.points[player_1] += 3
        elif (resultado == 2):
            self.points[player_2] += 3
        else:
            self.points[player_1] += 1
            self.points[player_2] += 1

    # Función que realiza todos los enfrentamientos del campeonato.
    def allMatchUps(self):
        print(Fore.CYAN)
        print("\x1B[3mC O M I E N Z A N   L O S   M A T C H   U P S\x1B[23m\n\n")
        print(Style.RESET_ALL)
        # Definimos una lista de participantes que ya compitieron contra todos.
        players_ready = []
        # Recorremos todos los participantes.
        for player_1 in self.participantes:
            for player_2 in self.participantes:
                # Si es que el participante no se ha enfrentado a todos entonces realizamos el matchUp
                if (player_2 not in players_ready and player_1 != player_2):
                    self.matchUp(player_1, player_2)
            # Luego de haber hecho todos los matchUps, agregamos al player_1 a la lista de jugadores listos.
            players_ready.append(player_1)
    
    # Función para imprimir la tabla de puntuación
    def printLeaderboard(self):
        print(Fore.LIGHTBLUE_EX)
        print(" Tabla de la Liga ")
        print(Style.RESET_ALL)
        print("------------------")
        # Recorremos el diccionario de puntos por participante.
        for participante, puntos in self.points.items():
            print ("{:<20} {:<5}".format(participante, puntos))