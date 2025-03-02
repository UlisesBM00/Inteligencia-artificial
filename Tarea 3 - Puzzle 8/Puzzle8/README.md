# Puzzle 8 con Algoritmo A* y GUI en Tkinter

Este es un programa en Python que resuelve el clásico *Puzzle 8* utilizando el algoritmo de búsqueda A* (*A-Star*). Además, cuenta con una interfaz gráfica desarrollada con Tkinter para que el usuario pueda ingresar el tablero inicial y visualizar la solución paso a paso.

## Características

- Implementación del algoritmo **A*** con **distancia de Manhattan** como heurística.
- **Interfaz gráfica (GUI)** con Tkinter para ingresar el tablero y mostrar la solución.
- **Validación de entrada de datos** para asegurar que los números ingresados sean únicos y dentro del rango permitido (0-8).
- **Animación paso a paso** de la solución en la GUI.

## Uso

1. **Ejecuta el programa** y aparecerá una ventana donde puedes ingresar los números del tablero inicial.
2. **Introduce los números del 0 al 8**, sin repetir, representando el estado inicial del puzzle.
3. **Presiona el botón "Resolver Puzzle"** y el programa calculará la solución.
4. **Observa la animación** de los movimientos hasta alcanzar la solución.
5. Si deseas probar otro puzzle, **presiona "Nuevo Puzzle"** para limpiar el tablero.

## Funcionamiento del Algoritmo A*

El algoritmo A* busca la solución óptima utilizando la función de evaluación:

```
f(n) = g(n) + h(n)
```

Donde:
- `g(n)`: Costo del camino desde el estado inicial hasta el estado actual.
- `h(n)`: Estimación del costo restante hasta la solución (heurística de Manhattan).

## Estructura del Código

- **`encontrar_espacio(tablero)`**: Encuentra la posición del número 0 (espacio vacío).
- **`distancia_manhattan(tablero, meta)`**: Calcula la heurística de Manhattan.
- **`generar_sucesores(estado)`**: Genera los movimientos posibles intercambiando el 0 con una celda adyacente.
- **`a_estrella(inicial, meta)`**: Implementa el algoritmo A* para encontrar la solución óptima.
- **`PuzzleGUI`**: Clase que maneja la interfaz gráfica con Tkinter.
