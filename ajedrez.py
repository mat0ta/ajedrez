# Importamos los módulos requeridos para realizar la actividad.
from os import *
from time import *

# Creamos las variables necesarias.
fichasAjedrez = {
    9812: {  # ♔
        'x': 5,
        'y': 5
    }, 9813: {  # ♕
        'x': 5,
        'y': 5
    }, 9814: {  # ♖
        'x': 5,
        'y': 5
    }, 9815: {  # ♗
        'x': 5,
        'y': 5
    }, 9816: {  # ♘
        'x': 5,
        'y': 5
    }, 9817: {  # ♙
        'x': 5,
        'y': 5
    }, 9818: {  # ♚
        'x': 5,
        'y': 5
    }, 9819: {  # ♛
        'x': 5,
        'y': 5
    }, 9820: {  # ♜
        'x': 5,
        'y': 5
    }, 9821: {  # ♝
        'x': 5,
        'y': 5
    }, 9822: {  # ♞
        'x': 5,
        'y': 5
    }, 9823: {  # ♟
        'x': 5,
        'y': 5
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
            rawTablero[a][b] = '--'
        elif (b % 2) != 0 or (a % 2) != 0:
            rawTablero[a][b] = '  '

for r in range(17):
    # print(' '.join(rawTablero[r]))
    print(' '.join(rawTablero[r]))
