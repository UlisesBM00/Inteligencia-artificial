# Sistema Experto de Recomendación de Juegos de Mesa 🎲

Este proyecto implementa un **sistema experto en Prolog** que recomienda juegos de mesa en función de las preferencias del usuario, utilizando reglas de inferencia basadas en número de jugadores, duración, complejidad y temática.

---

## 📌 ¿Qué hace?

Con base en las respuestas del usuario, el sistema recomienda uno o varios juegos de mesa adecuados. El usuario debe proporcionar:

- Número de jugadores
- Duración del juego (corta, media, larga)
- Nivel de complejidad (baja, media, alta)
- Temática del juego

---

## 🧠 Ejemplo de uso

```prolog
?- menu.
==========================================
      Sistema Experto: Juegos de Mesa
==========================================
Ingresa los siguientes datos:
Numero de jugadores: 4.
Duracion (corta, media, larga): media.
Complejidad (baja, media, alta): media.
Tematica: estrategia.

Juegos recomendados:
- ticket_to_ride
```

---

## 🛠️ Requisitos

- [SWI-Prolog](https://www.swi-prolog.org/Download.html) instalado
- VS Code (opcional) con extensión Prolog
- Archivo `juegos.pl` con el sistema experto cargado

---

## 🚀 Cómo ejecutar

1. Abre una terminal.
2. Ejecuta Prolog:

   ```bash
   swipl
   ```

3. Carga el archivo:

   ```prolog
   ?- [juegos].
   ```

4. Ejecuta el sistema experto:

   ```prolog
   ?- menu.
   ```

5. Responde las preguntas siguiendo este formato:

   - Usa punto final (`.`) en cada respuesta.
   - Escribe los valores en **minúsculas** y sin comillas.

---

## 🎯 Temáticas disponibles

```
estrategia, cooperativo, azar, familiar, social, bluff, deduccion, traicion,
ciencia_ficcion, humor, fantasia, misterio, economia, virus, cartas, historia, confrontacion
```

---

## 📚 Autor

- Nombre: Beltrán Magaña Ulises
- Materia: Inteligencia Artificial
- Carrera: Ingeniería en Sistemas Computacionales
