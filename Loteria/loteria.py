# -*- coding: utf-8 -*-
"""
La Lotería Mexicana - Simulador v0.2
Autor: Francisco Ruvalcaba
Licencia: Public Domain
"""

import random

# Constantes
TOTAL_CARTAS = 54
CARTAS_POR_TABLA = 16
NUMERO_TABLAS = 4

# Mazo completo de 54 cartas con nombres tradicionales
cartas = [
    'El Gallo', 'El Diablo', 'La Dama', 'El Catrín', 'El Paraguas',
    'La Sirena', 'La Escalera', 'La Botella', 'El Barril', 'El Árbol',
    'El Melón', 'El Valiente', 'El Gorrito', 'La Muerte', 'La Pera',
    'La Bandera', 'El Bandolón', 'El Violoncello', 'La Garza', 'El Pájaro',
    'La Mano', 'La Bota', 'La Luna', 'El Cotorro', 'El Borracho',
    'El Negrito', 'El Corazón', 'La Sandía', 'El Tambor', 'El Camarón',
    'Las Jaras', 'El Músico', 'La Araña', 'El Soldado', 'La Estrella',
    'El Cazo', 'El Mundo', 'El Apache', 'El Nopal', 'El Alacrán',
    'La Rosa', 'La Calavera', 'La Campana', 'El Cantarito', 'El Venado',
    'El Sol', 'La Corona', 'La Chalupa', 'El Pino', 'El Pescado',
    'La Palma', 'La Maceta', 'El Arpa', 'La Rana'
]

# Validar que el mazo tenga las cartas correctas
if len(cartas) != TOTAL_CARTAS:
    raise ValueError(f"El mazo debe tener {TOTAL_CARTAS} cartas, tiene {len(cartas)}")

# Crear tablas con nombres descriptivos
tabla_1 = random.sample(cartas, CARTAS_POR_TABLA)
tabla_2 = random.sample(cartas, CARTAS_POR_TABLA)
tabla_3 = random.sample(cartas, CARTAS_POR_TABLA)
tabla_4 = random.sample(cartas, CARTAS_POR_TABLA)

print("\n", tabla_1, "\n", tabla_2, "\n", tabla_3, "\n", tabla_4, "\n\n SE VA Y SE CORRE ...\n")

# Simulación del juego
cartas_cantadas = 0
hubo_ganador = False

for c in cartas:
    print(c)
    cartas_cantadas += 1

    if c in tabla_1:
        tabla_1.remove(c)
    if c in tabla_2:
        tabla_2.remove(c)
    if c in tabla_3:
        tabla_3.remove(c)
    if c in tabla_4:
        tabla_4.remove(c)

    print("T1 = {} T2 = {} T3 = {} T4 = {}".format(
        len(tabla_1), len(tabla_2), len(tabla_3), len(tabla_4)))

    if len(tabla_1) == 0 or len(tabla_2) == 0 or len(tabla_3) == 0 or len(tabla_4) == 0:
        print("\n\n¡BUENAS!")
        print("Cartas Cantadas = {}".format(cartas_cantadas))
        print("Quedaron en el mazo por cantar = {}".format(TOTAL_CARTAS - cartas_cantadas))
        hubo_ganador = True
        break

# Nota: Este bloque es defensivo. En teoría nunca se ejecuta porque
# al cantar las 54 cartas, todas las tablas deberían completarse.
if not hubo_ganador:
    print("\n\n¡Juego terminado! Nadie ganó con las {} cartas.".format(TOTAL_CARTAS))