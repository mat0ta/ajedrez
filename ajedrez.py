# Importamos los módulos requeridos para realizar la actividad.
from os import *
from time import *
from colorama import *

# Creamos las variables necesarias.
fichasAjedrez = {
    'RYB': {  # ♔
        'chr': 9812,
        'x': 8,
        'y': 5
    }, 'RAB': {  # ♕
        'chr': 9813,
        'x': 8,
        'y': 4
    }, 'TB': {  # ♖
        'chr': 9814,
        'x': 8,
        'y': 1
    }, 'AB': {  # ♗
        'chr': 9815,
        'x': 8,
        'y': 3
    }, 'CB': {  # ♘
        'chr': 9816,
        'x': 8,
        'y': 2
    }, 'PB': {  # ♙
        'chr': 9817,
        'x': 7,
        'y': 1
    }, 'RYN': {  # ♚
        'chr': 9818,
        'x': 1,
        'y': 5
    }, 'RAN': {  # ♛
        'chr': 9819,
        'x': 1,
        'y': 4
    }, 'TN': {  # ♜
        'chr': 9820,
        'x': 1,
        'y': 1
    }, 'AN': {  # ♝
        'chr': 9821,
        'x': 1,
        'y': 3
    }, 'CN': {  # ♞
        'chr': 9822,
        'x': 1,
        'y': 2
    }, 'PN': {  # ♟
        'chr': 9823,
        'x': 2,
        'y': 1
    }
}

class Ajedrez():
    def __init__(self):
        self.tablero = []
        self.jugador1 = ''
        self.jugador2 = ''
        self.jungando = 0

    def crearTablero(self):
        n1 = 8
        n2 = 65
        for i in range(18):
            self.tablero.append(([' ']*18))
        for a in range(18):
            for b in range(18):
                if b != 17 and a != 17:
                    if (b % 2) == 0:
                        if a == 0 or a == 16:
                            self.tablero[a][b] = '--'
                        else:
                            self.tablero[a][b] = '||'
                    elif (a % 2) == 0:
                        self.tablero[a][b] = '---'

                    elif (b % 2) != 0 or (a % 2) != 0:
                        self.tablero[a][b] = '   '
                if a == 17 and (b % 2) == 0 and n2 != 73:
                    self.tablero[a][b] = '   ' + chr(n2)
                    n2 += 1
                self.tablero[17][0] = '    A'
                if b == 17 and (a % 2) != 0 and n1 > 0:
                    self.tablero[a][b] = ' ' + str(n1)
                    n1 -= 1
        for value in fichasAjedrez:
            x = fichasAjedrez[value]['x'] + (fichasAjedrez[value]['x'] - 1)
            y = fichasAjedrez[value]['y'] + (fichasAjedrez[value]['y'] - 1)
            self.tablero[x][y] = ' ' + chr(fichasAjedrez[value]['chr']) + ' '
            if value == 'CN' or value == 'CB':
                self.tablero[x][y + 10] = ' ' + chr(fichasAjedrez[value]['chr']) + ' '
            elif value == 'AN' or value == 'AB':
                self.tablero[x][y + 6] = ' ' + chr(fichasAjedrez[value]['chr']) + ' '
            elif value == 'TN' or value == 'TB':
                self.tablero[x][y + 14] = ' ' + chr(fichasAjedrez[value]['chr']) + ' '
            elif value == 'PN' or value == 'PB':
                for i in range(17):
                    if (i % 2) != 0 and i != 0:
                        self.tablero[x][i] = ' ' + chr(fichasAjedrez[value]['chr']) + ' '
        for r in range(18):
            print(' '.join(self.tablero[r]))
    def pedirNombres(self):
        self.jugador1 = str(input('¿Cuál es el nombre del primer jugador?: ' + Fore.RED))
        self.jugador2 = str(input(Fore.RESET + '¿Y el nombre del segundo jugador?: ' + Fore.BLUE))
    # def movimiento(self):
    #     self.tablero[]

    def inciarJuego(self):
        print(Back.CYAN + Fore.BLACK + Style.DIM + '♔ Bienvenidos al Ajedrez ♚' +
              Back.RESET + Fore.RESET + Style.RESET_ALL)
        a.pedirNombres()
        print(Fore.RESET)
        a.crearTablero()



a = Ajedrez()
a.crearTablero()