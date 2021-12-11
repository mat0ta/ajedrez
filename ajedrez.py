# Importamos los módulos requeridos para realizar la actividad.
import os
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
    def printTablero(self):
        for r in range(18):
            print(' '.join(self.tablero[r]))
    def pedirNombres(self):
        self.jugador1 = str(input('¿Cuál es el nombre del primer jugador?: ' + Fore.GREEN))
        self.jugador2 = str(input(Fore.RESET + '¿Y el nombre del segundo jugador?: ' + Fore.BLUE))
        print(Fore.RESET)
        aj.printTablero()
    def movimiento(self):
        if self.jungando == 0:
            print('Turno de ' + Fore.GREEN + self.jugador1 + Fore.RESET)
            self.jungando = 1
        else:
            print('Turno de ' + Fore.BLUE + self.jugador2 + Fore.RESET)
            self.jungando = 0
        ficha = input('Introduce las coordenadas de la posición de la Ficha que quieres mover: ')
        destino = input('Introduce las coordenadas de la posición de la Casilla a donde quieres mover la Ficha: ')
        xold = ord(ficha[:1].upper()) - 64
        yold = ficha[1:2]
        y = xold + (xold - 1)
        x = 8 - (int(yold) - 1)
        x = x + (x - 1)
        print(x, y)
        for i in range(9812, 9823):
            if i == ord(self.tablero[int(x)][int(y)][1:2]):
                print('Hay una ficha')
                xold2 = ord(destino[:1].upper()) - 64
                yold2 = destino[1:2]
                y2 = xold2 + (xold2 - 1)
                x2 = 8 - (int(yold2) - 1)
                x2 = x2 + (x2 - 1)
                for i in range(9812, 9823):
                    if i == ord(self.tablero[int(x2)][int(y2)][1:2]):
                        if self.jungando == 0:
                            self.jungando = 1
                        else:
                            self.jungando = 0
                        print('Aqui hay una ficha, prueba con otra casilla.')
                        return aj.movimiento()
                self.tablero[int(x2)][int(y2)] = self.tablero[int(x)][int(y)]
                self.tablero[int(x)][int(y)] = '   '
                os.system('cls')
                aj.printTablero()
                return aj.movimiento()
    def inciarJuego(self):
        print(Back.CYAN + Fore.BLACK + Style.DIM + '♔ Bienvenidos al Ajedrez ♚' +
              Back.RESET + Fore.RESET + Style.RESET_ALL)
        aj.pedirNombres()
        print(Fore.RESET)
        aj.crearTablero()

aj = Ajedrez()
aj.crearTablero()
aj.pedirNombres()
aj.movimiento()