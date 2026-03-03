# 🎲 La Lotería Mexicana - Simulador

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-Public%20Domain-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Estado-En%20desarrollo-yellow.svg)]()

> Un simulador digital del clásico juego de mesa mexicano **La Lotería**, con sus 54 cartas tradicionales y versos auténticos.

---

## 📋 Índice

- [🎮 ¿Qué es La Lotería?](#-qué-es-la-lotería)
- [✨ Características](#-características)
- [🚀 Instalación y Uso](#-instalación-y-uso)
- [🃏 Cartas y Versos](#-cartas-y-versos)
- [🤝 Cómo Contribuir](#-cómo-contribuir)
- [📜 Licencia](#-licencia)
- [🙏 Agradecimientos](#-agradecimientos)

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

## ✨ Características

- ✅ Mazo completo de **54 cartas** con versos tradicionales auténticos
- ✅ Sistema de barajado aleatorio
- ✅ Interfaz de línea de comandos (CLI) intuitiva
- ✅ Código modular y fácil de extender
- ✅ Documentación en español
- ✅ Listo para agregar interfaz gráfica (GUI) o web

---

## 🚀 Instalación y Uso

### Requisitos previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/frantizek/Simuladores.git
cd Simuladores/Loteria

# 2. (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias (si existen)
pip install -r requirements.txt

# 4. Ejecutar el simulador
python main.py
```

### ▶️ Uso básico

```bash
# Iniciar nueva partida
python main.py --nuevo

# Ver lista de cartas
python main.py --cartas

# Ayuda completa
python main.py --help
```

> 💡 *Nota: Si el proyecto aún no tiene archivos ejecutables, esta sección se actualizará cuando estén disponibles.*

---

## 🃏 Cartas y Versos

<details>
<summary><strong>📜 Ver las 54 cartas completas (clic para expandir)</strong></summary>

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

## 🤝 Cómo Contribuir

¡Las contribuciones son bienvenidas! 🎉

1. Haz **fork** del proyecto
2. Crea tu rama de característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un **Pull Request**

### 💡 Ideas para contribuir:
- [ ] Agregar interfaz gráfica con Tkinter o PyQt
- [ ] Implementar modo multijugador en red
- [ ] Añadir voces o audio para los versos
- [ ] Crear generador de tablas aleatorias
- [ ] Traducir a otros idiomas
- [ ] Mejorar tests y documentación

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
  <sub>¡Que gane la mejor tabla! 🎲✨</sub>
</div>