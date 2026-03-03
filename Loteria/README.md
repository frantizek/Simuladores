# 🎲 La Lotería Mexicana - Simulador (MVP)

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-Public%20Domain-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Estado-Prototype-orange.svg)]()

> Prototipo inicial de simulador del juego tradicional mexicano **La Lotería**. 
> Versión de consola automática para validación de lógica.

---

## 📋 Índice

- [🎮 ¿Qué es La Lotería?](#-qué-es-la-lotería)
- [⚡ Estado Actual](#-estado-actual)
- [🚀 Ejecución Rápida](#-ejecución-rápida)
- [🃏 Cartas y Versos (Referencia)](#-cartas-y-versos-referencia)
- [🗺️ Roadmap](#-roadmap)
- [🤝 Cómo Contribuir](#-cómo-contribuir)
- [📜 Licencia](#-licencia)

---

## 🎮 ¿Qué es La Lotería?

**La Lotería** es un juego de mesa tradicional mexicano que combina azar, memoria y cultura popular. 

### 🎯 Objetivo del juego:
1. Se utiliza un mazo de **54 cartas únicas** que se barajan aleatoriamente.
2. Un "gritador" nombra las cartas una por una, tradicionalmente mediante versos o rimas populares.
3. Los jugadores marcan las cartas que aparecen en sus **tablas de juego** (cartones de 4x4).
4. **Gana** quien complete su tabla primero, gritando *"¡Lotería!"*.

> 🇲🇽 *Este proyecto busca preservar y digitalizar esta hermosa tradición cultural mexicana.*

---

## ⚡ Estado Actual (v0.1 - Prototype)

### ✅ Lo que SÍ funciona:
- [x] Mazo de 54 cartas con barajado aleatorio (`random.shuffle`)
- [x] Generación de 4 tablas de juego con 16 cartas cada una
- [x] Simulación automática: canto de cartas y detección de ganador
- [x] Output en consola con conteo de cartas restantes por tabla
- [x] Código funcional sin dependencias externas

### ❌ Lo que AÚN NO está implementado:
- [ ] Interfaz interactiva (el juego corre solo, sin input del usuario)
- [ ] Argumentos de línea de comandos (`--help`, `--modo`, etc.)
- [ ] Visualización de tablas en formato grid 4x4
- [ ] Nombres completos de cartas ("El Gallo" vs "Gallo")
- [ ] Versos/coplas tradicionales en el output
- [ ] Manejo de errores o validaciones
- [ ] Tests unitarios o documentación de código

> 💡 **Nota**: Esta es una versión mínima viable (MVP) para validar la lógica central. 
> ¡Las mejoras están en el roadmap!

---

## 🚀 Ejecución Rápida

### Requisitos
- Python 3.6 o superior
- Sin dependencias externas (solo librería estándar)

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/frantizek/Simuladores.git
cd Simuladores/Loteria

# 2. Ejecutar el simulador
python loteria.py
```

### 📤 Output esperado

```
['Gallo', 'Diablo', 'Dama', ...]  # Tabla 1
['Barril', 'Árbol', 'Melón', ...]  # Tabla 2
...

SE VA Y SE CORRE ...

Gallo
T1 = 15 T2 = 16 T3 = 16 T4 = 16
Diablo
T1 = 14 T2 = 16 T3 = 16 T4 = 16
...

BUENAS!!!
Cartas Cantadas = 32 
Quedaron en el mazo por cantar = 22
```

> ⚠️ **Nota**: El juego se ejecuta automáticamente de principio a fin. 
> No hay interacción del usuario en esta versión.

---

## 🃏 Cartas y Versos (Referencia Cultural)

<details>
<summary><strong>📜 Ver las 54 cartas completas (clic para expandir)</strong></summary>

> 📌 *Estos versos son parte de la tradición oral mexicana. 
> Actualmente NO están implementados en el código, pero se incluyen aquí como referencia para futuras versiones.*

| # | Carta | Verso tradicional |
|---|-------|------------------|
| 1 | 🐓 El Gallo | *"El que le cantó a san Pedro, no le volverá a cantar."* |
| 2 | 😈 El Diablo | *"El diablo son las mujeres, cuando se quieren casar."* |
| 3 | 👩 La Dama | *"La chula de Severiana, un tacón quería empeñar."* |
| 4 | 🎩 El Catrín | *"Don Ferruco en la Alameda, su bastón quería empeñar."* |
| 5 | ☂️ El Paraguas | *"El paraguas quitasol."* |
| 6 | 🧜 La Sirena | *"Medio cuerpo de sirena, medio cuerpo de mujer."* |
| 7 | 🪜 La Escalera | *"La escalera, siete palos, la escalera del pintor."* |
| 8 | 🍾 La Botella | *"La botella del tequila, la botella del mezcal."* |
| 9 | 🛢️ El Barril | *"El barril es quintaleño, el barril del mezcal."* |
| 10 | 🌳 El Árbol | *"El árbol de la esperanza, que de venir no se cansa."* |
| 11 | 🍈 El Melón | *"El melón y sus olores, un pedazo me has de dar."* |
| 12 | 🗡️ El Valiente | *"'Tate quieto, Valentín, no te vayas a pelear."* |
| 13 | 🧢 El Gorrito | *"El gorrito ponle al nene, no se te vaya a resfriar."* |
| 14 | 💀 La Muerte | *"La muerte siriquiflaca, montada en su burra flaca."* |
| 15 | 🍐 La Pera | *"Me esperas donde quedamos, para poder platicar."* |
| 16 | 🇲🇽 La Bandera | *"Bonito cinco de mayo, el pabellón nacional."* |
| 17 | 🎸 El Bandolón | *"El bandolón ya no suena, hay que llevarlo a afinar."* |
| 18 | 🎻 El Violoncello | *"El violoncello del maistro, que no deja de sonar."* |
| 19 | 🦢 La Garza | *"Llegaron los picos largos de la feria de San Juan."* |
| 20 | 🐦 El Pájaro | *"El pájaro churlumirlo, que no deja de cantar."* |
| 21 | ✋ La Mano | *"La mano del escribano, la mano del criminal."* |
| 22 | 👢 La Bota | *"La bota rechina, la bota del general."* |
| 23 | 🌙 La Luna | *"La luna tuerta de un ojo, que no deja de brillar."* |
| 24 | 🦜 El Cotorro | *"Perico, da'cá la pata y empiézame a platicar..."* |
| 25 | 🍺 El Borracho | *"Al borracho, mi compañero, ya se lo van a cargar."* |
| 26 | 👦 El Negrito | *"Para negros, en La Habana; uno acaba de llegar."* |
| 27 | ❤️ El Corazón | *"El corazón de una ingrata, yo lo voy a traspasar."* |
| 28 | 🍉 La Sandía | *"La sandía y su rebanada, un pedazo me has de dar."* |
| 29 | 🥁 El Tambor | *"No te arrugues, cuero viejo, que te quiero pa' tambor."* |
| 30 | 🦐 El Camarón | *"Camarón que se duerme, se lo lleva la corriente."* |
| 31 | 🏹 Las Jaras | *"Las jaras o no las jaras, o las dejas de jalar."* |
| 32 | 🎺 El Músico | *"El músico, trompa de hule."* |
| 33 | 🕷️ La Araña | *"La araña teje su tela."* |
| 34 | 🪖 El Soldado | *"Centinela, ponte alerta, que te habla tu general."* |
| 35 | ⭐ La Estrella | *"La estrella polar del norte, que no deja de brillar."* |
| 36 | 🍶 El Cazo | *"El caso que te hago es poco; el caso es averiguar."* |
| 37 | 🌍 El Mundo | *"El mundo es una bola, y nosotros, un bolón."* |
| 38 | 🪶 El Apache | *"Para apaches, en Chihuahua; uno acaba de llegar."* |
| 39 | 🌵 El Nopal | *"El auxilio de San Luis, que le llaman el nopal."* |
| 40 | 🦂 El Alacrán | *"¡No levantes esa piedra, que te pica ese animal!"* |
| 41 | 🌹 La Rosa | *"Rosa, Rosita, Rosaura, Rosita se ha de llamar."* |
| 42 | 💀 La Calavera | *"Ya te vide an ca' la güera."* |
| 43 | 🔔 La Campana | *"La campana, y tú, debajo."* |
| 44 | 🏺 El Cantarito | *"Todo cabe en un jarrito, sabiéndolo acomodar."* |
| 45 | 🦌 El Venado | *"Don Venancio, a la carrera, un balazo le han de dar."* |
| 46 | ☀️ El Sol | *"Solito me estoy quedando, solito me he de quedar."* |
| 47 | 👑 La Corona | *"Si te mueres, te la pongo, la coronita imperial."* |
| 48 | 🚣 La Chalupa | *"Rema y rema, Joaquinita, y no dejes de remar."* |
| 49 | 🌲 El Pino | *"Te empino y me voy de paso, y empinado has de quedar."* |
| 50 | 🐟 El Pescado | *"Me pescaron vacilando en la puerta del zaguán."* |
| 51 | 🌴 La Palma | *"Sube a la palma, palmero, y bájame un cocotal."* |
| 52 | 🪴 La Maceta | *"En la maceta me dieron, por no saber barajar."* |
| 53 | 🎻 El Arpa | *"El arpa vieja de mi suegra."* |
| 54 | 🐸 La Rana | *"¡Qué saltos pega tu hermana en la puerta del zaguán!"* |

</details>

> 📚 **Fuente de los versos**: [México Desconocido - Historia del juego de la Lotería](https://www.mexicodesconocido.com.mx/historia-del-juego-de-la-loteria-y-los-54-versos-para-cantarla.html)

---

## 🗺️ Roadmap

### 🔜 Próximamente (v0.2)
- [ ] Agregar nombres completos a las cartas ("El/La + nombre")
- [ ] Formato de tablas en grid 4x4 para mejor legibilidad
- [ ] Opción de modo manual: avanzar carta por carta con input
- [ ] Agregar versos tradicionales al output del "gritador"

### 🚀 Futuro (v1.0)
- [ ] Refactorizar código: funciones, clases, separación de responsabilidades
- [ ] Agregar interfaz gráfica con Tkinter o PyQt
- [ ] Sistema de múltiples jugadores humanos en red
- [ ] Audio/voz para los versos cantados
- [ ] Tests unitarios y documentación técnica

### 💡 ¿Tienes ideas?
¡Abre un issue o contribuye con un PR! Todas las sugerencias son bienvenidas.

---

## 🤝 Cómo Contribuir

¡Las contribuciones son bienvenidas! 🎉

### Para empezar:
1. Haz **fork** del proyecto
2. Crea tu rama: `git checkout -b feature/tu-idea`
3. Commit: `git commit -m 'Add: descripción clara'`
4. Push: `git push origin feature/tu-idea`
5. Abre un **Pull Request**

### 💡 Ideas para contribuir (principiantes):
- [ ] Agregar encoding UTF-8 al inicio del archivo
- [ ] Crear constantes para números mágicos (54, 16, 4)
- [ ] Extraer lógica a funciones reutilizables
- [ ] Agregar docstrings básicos
- [ ] Corregir formato de output de tablas
- [ ] Restaurar nombres completos de cartas

### 🔧 Ideas para contribuyentes avanzados:
- [ ] Implementar interfaz gráfica con Tkinter
- [ ] Agregar sistema de argumentos con `argparse`
- [ ] Crear tests con `pytest` o `unittest`
- [ ] Implementar modo multijugador en red

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia **Dominio Público** / **CC0 1.0 Universal**.  
Esto significa que eres libre de:

- ✅ Usar, modificar y distribuir el código
- ✅ Utilizarlo con fines comerciales
- ✅ Adaptarlo a tus necesidades

> ⚠️ **Nota cultural**: Aunque el código es libre, las imágenes tradicionales de La Lotería pueden tener derechos de autor. Se recomienda usar ilustraciones propias o de dominio público.

---

## 🙏 Agradecimientos

- 🇲🇽 A las comunidades que han preservado esta tradición por generaciones.
- 📚 [México Desconocido](https://www.mexicodesconocido.com.mx) por la documentación histórica.
- 👥 A todos los contribuyentes que hacen posible este proyecto.

---

<div align="center">
  <sub>Hecho con ❤️ y tradición mexicana por <a href="https://github.com/frantizek">@frantizek</a></sub><br>
  <sub>Versión MVP • ¡Mejoras en camino! 🎲✨</sub>
</div>