import heapq
import tkinter as tk
from time import sleep, time

# Representación del tablero de 3x3
meta = [[1, 2, 3], 
        [8, 0, 4], 
        [7, 6, 5]]  

# encontrar la posición del 0 (espacio vacío)
def encontrar_espacio(tablero):
    for i, fila in enumerate(tablero):
        if 0 in fila:
            return i, fila.index(0)

# Calcular la distancia
def distancia_manhattan(tablero, meta):
    distancia = 0
    for i in range(3):
        for j in range(3):
            valor = tablero[i][j]
            if valor != 0:
                x_meta, y_meta = [(idx, fila.index(valor)) for idx, fila in enumerate(meta) if valor in fila][0]
                distancia += abs(i - x_meta) + abs(j - y_meta)
    return distancia

# Función para generar nuevos estados posibles
def generar_sucesores(estado):
    tablero, g = estado
    i, j = encontrar_espacio(tablero)
    
    movimientos = []
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha
    
    for di, dj in direcciones:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            nuevo_tablero = [fila[:] for fila in tablero]  # Copia del tablero
            nuevo_tablero[i][j], nuevo_tablero[ni][nj] = nuevo_tablero[ni][nj], nuevo_tablero[i][j]
            movimientos.append((nuevo_tablero, g + 1))
    
    return movimientos

# algoritmo A*
def a_estrella(inicial, meta):
    inicio_tiempo = time()  # Tiempo de inicio
    prioridad = []
    heapq.heappush(prioridad, (distancia_manhattan(inicial, meta), 0, inicial, []))
    visitados = set()

    while prioridad:
        _, g, actual, camino = heapq.heappop(prioridad)
        
        if actual == meta:
            fin_tiempo = time()  # Tiempo de finalización
            tiempo_total = fin_tiempo - inicio_tiempo
            print(f"Tiempo total de ejecución: {tiempo_total:.6f} segundos")
            return camino
        
        # Convertir el tablero en tupla para ser inmutable y usable en el set
        estado_tupla = tuple(map(tuple, actual))
        if estado_tupla in visitados:
            continue
        visitados.add(estado_tupla)
        
        for sucesor, costo in generar_sucesores((actual, g)):
            if tuple(map(tuple, sucesor)) not in visitados:
                nuevo_camino = camino + [sucesor]
                f = costo + distancia_manhattan(sucesor, meta)
                heapq.heappush(prioridad, (f, costo, sucesor, nuevo_camino))
    
    return None  # No se encontró solución

def introducirNumeros():
    numeros=[]
    print("Introduce números del 0 al 8: ")
    
    while len(numeros)<9:
        try:
            num=int(input(f"valor {len(numeros)+1}: "))
            
             # Verificar que el valor esté en el rango de 0 a 8 y no se haya ingresado previamente
            if num < 0 or num > 8:
                print("El valor debe estar entre 0 y 8. Inténtalo de nuevo.")
            elif num in numeros:
                print("Ese valor ya ha sido ingresado. Introduce uno diferente.")
            else:
                numeros.append(num)
        except ValueError:
            print("Entrada inválida. Debes introducir un número entero.")
            
    tablero_usuario = [numeros[i:i+3] for i in range(0, 9, 3)]
    return tablero_usuario

class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Puzzle-8")
        
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Tablero inicial vacío
        self.botones = []
        self.entradas = []
        
        # Establecer el tamaño de la ventana
        self.root.geometry("350x400")

        # Crear los cuadros de texto para que el usuario introduzca los números
        self.introducirValores()

        # Botón para resolver el puzzle
        self.boton_resolver = tk.Button(root, text="Resolver Puzzle", font=("Helvetica", 16) ,command=self.resolverTablero)
        self.boton_resolver.grid(row=4, column=0, columnspan=3)
        
        # Botón para limpiar el tablero
        self.boton_limpiar = tk.Button(root, text="Nuevo Puzzle", font=("Helvetica", 16), command=self.limpiarTablero)
        self.boton_limpiar.grid(row=5, column=0, columnspan=3, pady=10)

        # Etiqueta para mostrar el número de movimientos
        self.etiqueta_movimientos = tk.Label(root, text="", font=("Helvetica", 14))
        self.etiqueta_movimientos.grid(row=8, column=0, columnspan=3)
    
    def introducirValores(self):
        # Crear entradas para que el usuario teclee los valores
        for i in range(3):
            fila_entradas = []
            for j in range(3):
                entrada = tk.Entry(root, width=3, font=("Helvetica", 40), justify="center")
                entrada.grid(row=i, column=j, padx=5, pady=10)
                fila_entradas.append(entrada)
            self.entradas.append(fila_entradas)

    def introducirTablero(self):
        # Extrae el tablero desde las entradas de texto
        tablero_usuario = []
        for i in range(3):
            fila = []
            for j in range(3):
                valor = self.entradas[i][j].get()
                try:
                    valor_int = int(valor)
                    fila.append(valor_int)
                except ValueError:
                    fila.append(0)  # Si hay un valor inválido, se convierte en 0 (espacio vacío)
            tablero_usuario.append(fila)
        return tablero_usuario

    # Actualiza el nuevo tablero
    def actualizarTablero(self, tablero):
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == 0:
                    self.entradas[i][j].delete(0, tk.END)
                    self.entradas[i][j].insert(0, "")
                    self.entradas[i][j].config(bg="black")
                else:
                    self.entradas[i][j].delete(0, tk.END)
                    self.entradas[i][j].insert(0, str(tablero[i][j]))
                    self.entradas[i][j].config(bg="lightgray")
      
    # Limpiar todas las entradas del tablero              
    def limpiarTablero(self):
        for i in range(3):
            for j in range(3):
                self.entradas[i][j].delete(0, tk.END)
                self.entradas[i][j].config(bg="white")  # Restablecer el color de fondo

        # Restablecer la etiqueta de movimientos
        self.etiqueta_movimientos.config(text="")

    def resolverTablero(self):
        # Obtener el tablero desde las entradas de usuario
        inicial = self.introducirTablero()
        
        # Resolvemos el puzzle
        solucion = a_estrella(inicial, meta)

        if solucion:
            self.etiqueta_movimientos.config(text=f"Solución encontrada en {len(solucion)} movimientos.")
            # Mostrar la solución paso a paso en la interfaz gráfica
            for paso in solucion:
                self.actualizarTablero(paso)
                self.root.update()
                sleep(1)  # Pausa de 1 segundo entre cada movimiento
        else:
            self.etiqueta_movimientos.config(text="No se encontró solución.")

root = tk.Tk()
# Crear la interfaz
gui = PuzzleGUI(root)
root.mainloop()
