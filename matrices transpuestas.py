def crear_matriz():
    filas = int(input("Ingresa el número de filas: "))
    columnas = int(input("Ingresa el número de columnas: "))
    
    # Inicializa la matriz
    matriz = []  
    
    for i in range(filas):
        # Solicita los elementos de la fila
        fila = input(f"Introduce los elementos de la fila {i+1} separados por espacios: ").split()
        # Valida que el número de elementos de la fila sea igual al número de columnas
        if len(fila) != columnas:
            print("Número de elementos de la fila no coinciden con el número de columnas.")
            return None  # Devuelve None si la fila no es válida
        # Convierte los elementos de la fila a flotantes
        fila = [float(elemento) for elemento in fila]
        matriz.append(fila)  # Agrega la fila a la matriz
    
    return matriz

def transponer_matriz(matriz):
    if matriz is None:
        return None
    filas = len(matriz)
    columnas = len(matriz[0])
    #Inicializa la matriz transpuesta
    matriz_transpuesta = [[0]* filas for _ in range(columnas)]
    for i in range(filas):
        for j in range(columnas):
            #Asignar el valor transpuesto
            matriz_transpuesta[j][i] = matriz[i][j]
    return matriz_transpuesta

if __name__ == "__main__":
    matriz = crear_matriz()
    if matriz is None:
        print("La matriz no se creo correctamente")
    else:
        matriz_transpuesta = transponer_matriz(matriz)
        if matriz_transpuesta is not None:
            print("Matriz transpuesta")
            for fila in matriz_transpuesta:
                print(fila)