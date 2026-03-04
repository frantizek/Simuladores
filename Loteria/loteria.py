#!/usr/bin/env python3
"""
La Lotería Mexicana - Simulador

Un simulador del juego tradicional mexicano La Lotería.
Genera tablas aleatorias y simula el proceso de cantar las cartas.

Autor: [Contribuidor]
Licencia: Dominio Público
Fecha: 2026-03-04
"""

import random

# ============================================================================
# CONFIGURACIÓN DE CARTAS
# ============================================================================

# Lista de 54 cartas de La Lotería Mexicana (sustantivos únicos)
CARTAS = [
    'Gallo', 'Diablo', 'Dama', 'Catrín', 'Paraguas', 'Sirena', 'Escalera',
    'Botella', 'Barril', 'Árbol', 'Melón', 'Valiente', 'Gorrito', 'Muerte',
    'Pera', 'Bandera', 'Bandolón', 'Violoncello', 'Garza', 'Pájaro', 'Mano',
    'Bota', 'Luna', 'Cotorro', 'Borracho', 'Negrito', 'Corazón', 'Sandía',
    'Tambor', 'Camarón', 'Jaras', 'Músico', 'Araña', 'Soldado', 'Estrella',
    'Cazo', 'Mundo', 'Apache', 'Nopal', 'Alacrán', 'Rosa', 'Calavera',
    'Campana', 'Cantarito', 'Venado', 'Sol', 'Corona', 'Chalupa', 'Pino',
    'Pescado', 'Palma', 'Maceta', 'Arpa', 'Rana'
]

# ============================================================================
# FUNCIONES DEL JUEGO
# ============================================================================


def crear_tablas(cartas, num_tablas=4):
    """
    Crea tablas de juego con cartas aleatorias.

    Args:
        cartas (list): Lista de cartas disponibles.
        num_tablas (int): Número de tablas a crear (default: 4).

    Returns:
        list: Lista de tablas, cada una con 16 cartas.
    """
    return [random.sample(cartas, 16) for _ in range(num_tablas)]


def jugar_loteria(cartas, tablas):
    """
    Simula el juego de La Lotería cantando cartas hasta que alguien gane.

    Args:
        cartas (list): Lista de cartas barajadas.
        tablas (list): Lista de tablas de los jugadores.

    Returns:
        tuple: (cartas_cantadas, cartas_restantes)
    """
    cartas_cantadas = 0

    for carta in cartas:
        print(carta)

        # Remover la carta de todas las tablas
        for tabla in tablas:
            if carta in tabla:
                tabla.remove(carta)

        # Mostrar estado de las tablas
        estado = " ".join([f"T{i+1}={len(t)}" for i, t in enumerate(tablas)])
        print(f"  {estado}")

        # Verificar si alguien ganó (tabla vacía)
        if any(len(tabla) == 0 for tabla in tablas):
            print("\n\n¡BUENAS!")
            cartas_restantes = 54 - cartas_cantadas
            return cartas_cantadas, cartas_restantes

        cartas_cantadas += 1

    return cartas_cantadas, 0


# ============================================================================
# EJECUCIÓN PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    # Barajar las cartas
    cartas_barajadas = CARTAS.copy()
    random.shuffle(cartas_barajadas)

    # Crear 4 tablas de juego
    t1, t2, t3, t4 = crear_tablas(CARTAS)

    # Mostrar las tablas
    print("\n=== TABLAS DE LA LOTERÍA ===\n")
    print(f"Tabla 1: {t1}\n")
    print(f"Tabla 2: {t2}\n")
    print(f"Tabla 3: {t3}\n")
    print(f"Tabla 4: {t4}\n")
    print("¡SE VA Y SE CORRE CON LA LOTERÍA!\n")

    # Jugar
    cantadas, restantes = jugar_loteria(cartas_barajadas, [t1, t2, t3, t4])

    # Mostrar resultado final
    print(f"\nCartas Cantadas: {cantadas}")
    print(f"Quedaron en el mazo por cantar: {restantes}")
