from tournament import Tournament

# Queremos que el usuario ingrese la cantidad de participante en este torneo a muerte 1v1.
from abc import abstractproperty


#cantidad_participantes = int(input("Ingresa la cantidad de participantes\n"))

# Creamos una lista para guardar a los participantes.
participantes = []

# Tomamos a los participantes de un archivo .txt
with open("contestants.txt", "r") as participantes_file:
    contenido = participantes_file.readlines()
    cantidad_participantes = int(contenido[0])
    
    for i in range(0, cantidad_participantes):
        nuevo_participante = contenido[i]
        participantes.append(nuevo_participante)
        print("\n")

# Creamos el torneo con los participantes.
torneo = Tournament(participantes, cantidad_participantes)
# Realizamos todos los enfrentamientos
torneo.allMatchUps()
# Printeamos la tabla del torneo
torneo.printLeaderboard()