import random

#cartas = ['El Gallo', 'El Diablo', 'La Dama', 'El Catrín', 'El Paraguas', 'La Sirena', 'La Escalera', 'La Botella', 'El Barril', 'El Árbol', 'El Melón', 'El Valiente', 'El Gorrito', 'La Muerte', 'La Pera', 'La Bandera', 'El Bandolón', 'El Violoncello', 'La Garza', 'El Pájaro', 'La Mano', 'La Bota', 'La Luna', 'El Cotorro', 'El Borracho', 'El Negrito', 'El Corazón', 'La Sandía', 'El Tambor', 'El Camarón', 'Las Jaras', 'El Músico', 'La Araña', 'El Soldado', 'La Estrella', 'El Cazo', 'El Mundo', 'El Apache', 'El Nopal', 'El Alacrán', 'La Rosa', 'La Calavera', 'La Campana', 'El Cantarito', 'El Venado', 'El Sol', 'La Corona', 'La Chalupa', 'El Pino', 'El Pescado', 'La Palma', 'La Maceta', 'El Arpa', 'La Rana']

cartas_nouns = ['Gallo', 'Diablo', 'Dama', 'Catrín', 'Paraguas', 'Sirena', 'Escalera', 'Botella', 'Barril', 'Árbol', 'Melón', 'Valiente', 'Gorrito', 'Muerte', 'Pera', 'Bandera', 'Bandolón', 'Violoncello', 'Garza', 'Pájaro', 'Mano', 'Bota', 'Luna', 'Cotorro', 'Borracho', 'Negrito', 'Corazón', 'Sandía', 'Tambor', 'Camarón', 'Jaras', 'Músico', 'Araña', 'Soldado', 'Estrella', 'Cazo', 'Mundo', 'Apache', 'Nopal', 'Alacrán', 'Rosa', 'Calavera', 'Campana', 'Cantarito', 'Venado', 'Sol', 'Corona', 'Chalupa', 'Pino', 'Pescado', 'Palma', 'Maceta', 'Arpa', 'Rana']

random.shuffle(cartas_nouns)

# agregar tablas

t1 = random.sample(cartas_nouns, 16)
t2 = random.sample(cartas_nouns, 16)
t3 = random.sample(cartas_nouns, 16)
t4 = random.sample(cartas_nouns, 16)

print ("\n", t1, "\n", t2, "\n", t3, "\n", t4, "\n\n SE VA Y SE CORRE ...\n")


cartas_cantadas = 0
for c in cartas_nouns:
    print(c)
    if c in t1:
        t1.remove(c)
    if c in t2:
        t2.remove(c)
    if c in t3:
        t3.remove(c)
    if c in t4:
        t4.remove(c)
    print("T1 = {} T2 = {} T3 = {} T4 = {}".format(len(t1), len(t2), len(t3), len(t4)))
    if len(t1) == 0 or len(t2) == 0 or len(t3) == 0 or len(t4) == 0:
        print("\n\nBUENAS!!!")
        print("Cartas Cantadas = {} \nQuedaron en el mazo por cantar = {}".format(cartas_cantadas, 54-cartas_cantadas))
        break
    else:
        cartas_cantadas += 1
