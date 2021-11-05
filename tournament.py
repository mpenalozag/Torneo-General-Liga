from mathFunctions import closestPower
import random

class Tournament:
    # Recibe como input una lista con los participantes del torneo y un int con la cantidad de participantes.
    def __init__(self, participantes, cantidad_participantes):
        self.participantes = participantes
        self.participantes_sin_asignar = cantidad_participantes
        self.cantidad_participantes = cantidad_participantes
        self.points = {}


    # Función que describe el torneo.
    def describeTournament(self):
        print(f"Torneo con {self.cantidad_participantes}\n")
        print(" Participantes ")
        print("---------------")
        for i in range(self.cantidad_participantes):
            print(f"{i+1}) {self.participantes[i]}")

    # Función que setea la tabla de posiciones.
    def setLeaderboard(self):
        # A cada participante le asignamos un espacio en el diccionario.
        # El value asignado a cada participante corresponde a los 
        for participante in self.participantes:


    # Función que enfreta a 2 competidores y permite seleccionar quien gana
    def matchUp(self, player_1, player_2):
        pass