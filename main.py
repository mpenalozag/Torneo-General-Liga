from tournament import Tournament

# Queremos que el usuario ingrese la cantidad de participante en este torneo a muerte 1v1.
from abc import abstractproperty


cantidad_participantes = int(input("Ingresa la cantidad de participantes\n"))

# Creamos una lista para guardar a los participantes.
participantes = []

# Le pedimos al usuario que ingrese los nombres de cada participante.
for i in range(cantidad_participantes):
    nuevo_participante = input(f"Ingrese al participante número {i+1}\n")
    participantes.append(nuevo_participante)
    print("\n")

# Creamos el torneo con los participantes.
torneo = Tournament(participantes, cantidad_participantes)
# Realizamos todos los enfrentamientos
torneo.allMatchUps()
# Printeamos la tabla del torneo
torneo.printLeaderboard()