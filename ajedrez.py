# Importamos los módulos requeridos para realizar la actividad.
from os import *
from time import *
from colorama import *

# Creamos las variables necesarias.
fichasAjedrez = {
    'RYB': {  # ♔
        'chr': 9812
    }, 'RAB': {  # ♕
        'chr': 9813
    }, 'TB': {  # ♖
        'chr': 9814
    }, 'AB': {  # ♗
        'chr': 9815
    }, 'CB': {  # ♘
        'chr': 9816
    }, 'PB': {  # ♙
        'chr': 9817
    }, 'RYN': {  # ♚
        'chr': 9818
    }, 'RAN': {  # ♛
        'chr': 9819
    }, 'TN': {  # ♜
        'chr': 9820
    }, 'AN': {  # ♝
        'chr': 9821
    }, 'CN': {  # ♞
        'chr': 9822
    }, 'PN': {  # ♟
        'chr': 9823
    }
}

# # Creación del Tablero
# rawTablero = []
# for i in range(17):
#     rawTablero.append(([' ']*17))

# for a in range(17):
#     for b in range(17):
#         if (b % 2) == 0:
#             if a == 0 or a == 16:
#                 rawTablero[a][b] = '--'
#             else:
#                 rawTablero[a][b] = '||'
#         elif (a % 2) == 0:
#             rawTablero[a][b] = '---'
#         elif (b % 2) != 0 or (a % 2) != 0:
#             rawTablero[a][b] = '   '

# rawTablero[1][1] = ' ' + chr(9820) + ' '

# for r in range(17):
#     print(' '.join(rawTablero[r]))


class Ajedrez():
    def __init__(self):
        self.tablero = []
        self.jugador1 = ''
        self.jugador2 = ''

    def crearTablero(self):
        for i in range(17):
            self.tablero.append(([' ']*17))
        for a in range(17):
            for b in range(17):
                if (b % 2) == 0:
                    if a == 0 or a == 16:
                        self.tablero[a][b] = '--'
                    else:
                        self.tablero[a][b] = '||'
                elif (a % 2) == 0:
                    self.tablero[a][b] = '---'
                elif (b % 2) != 0 or (a % 2) != 0:
                    self.tablero[a][b] = '   '

    def pedirNombres(self):
        self.jugador1 = str(input('¿Cuál es el nombre del primer jugador?: ' + Fore.RED))
        self.jugador2 = str(input(Fore.RESET + '¿Y el nombre del segundo jugador?: ' + Fore.BLUE))

    def inciarJuego(self):
        a = Ajedrez()
        print(Back.CYAN + Fore.BLACK + Style.DIM + '♔ Bienvenidos al Ajedrez ♚' +
              Back.RESET + Fore.RESET + Style.RESET_ALL)
        a.pedirNombres()
        print(Fore.RESET)


a = Ajedrez()
a.inciarJuego()
