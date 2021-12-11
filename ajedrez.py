# Importamos los módulos requeridos para realizar la actividad.
from os import *
from time import *

# Creamos las variables necesarias.
fichasAjedrez = {
    'RYB': {  # ♔
        'chr': 9812
    }, 'RNB': {  # ♕
        'chr': 9813
    }, 'TN': {  # ♖
        'chr': 9814
    }, 'AN': {  # ♗
        'chr': 9815
    }, 'CB': {  # ♘
        'chr': 9816
    }, 'PB': {  # ♙
        'chr': 9817
    }, 'RYN': {  # ♚
        'chr': 9818
    }, 'RNN': {  # ♛
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


# Creación del Tablero
rawTablero = []
for i in range(17):
    rawTablero.append(([' ']*17))

for a in range(17):
    for b in range(17):
        if (b % 2) == 0:
            if a == 0 or a == 16:
                rawTablero[a][b] = '--'
            else:
                rawTablero[a][b] = '||'
        elif (a % 2) == 0:
            rawTablero[a][b] = '---'
        elif (b % 2) != 0 or (a % 2) != 0:
            rawTablero[a][b] = '   '

rawTablero[1][1] = ' ' + chr(9820) + ' '

for r in range(17):
    print(' '.join(rawTablero[r]))
