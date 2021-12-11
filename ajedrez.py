# Importamos los módulos requeridos para realizar la actividad.
from os import *
from time import *

# Creamos las variables necesarias.
fichasAjedrez = {
    ord('♔'): {  # 9812
        'value': 5
    }, ord('♕'): {  # 9813
        'value': 5
    }, ord('♖'): {  # 9814
        'value': 5
    }, ord('♗'): {  # 9815
        'value': 5
    }, ord('♘'): {  # 9816
        'value': 5
    }, ord('♙'): {  # 9817
        'value': 5
    }, ord('♚'): {  # 9818
        'value': 5
    }, ord('♛'): {  # 9819
        'value': 5
    }, ord('♜'): {  # 9820
        'value': 5
    }, ord('♝'): {  # 9821
        'value': 5
    }, ord('♞'): {  # 9822
        'value': 5
    }, ord('♟'): {  # 9823
        'value': 5
    }
}
print(fichasAjedrez[0].keys())
