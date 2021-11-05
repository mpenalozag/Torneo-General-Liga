# Función que permite saber que potencia de 2 está mas cerca del número que ingresamos como input.
def closestPower(numero):
    selected_power = 0
    while (2 ** selected_power < numero):
        selected_power += 1
    return 2**selected_power


if __name__ == "__main__":
    print(closestPower(6))
