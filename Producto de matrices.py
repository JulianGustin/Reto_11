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

def producto_matrices(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])
    #Verificar si las dimensiones son compatibles para el producto
    if columnas1 != filas2:
        print("El numero de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")
        return None
    #Inicializa la matriz del resultado para el producto
    matriz_producto = [[0]* columnas2 for _ in range(filas1)]

    for i in range(filas1):
        for j in range(columnas2):
            #Calcular el valor del elemento en la posicion (i,j)
            suma = 0
            for k in range(columnas1):
                suma += matriz1[i][k] * matriz2[k][j]
            matriz_producto[i][j] = suma
    return matriz_producto

if __name__ == "__main__":
    print("Escribe la primera matriz")
    matriz1 = crear_matriz()
    if matriz1 is None:
        print("La primera matriz no se creó correctamente.")
    else:
        print("Escribe la segunda matriz")
        matriz2 = crear_matriz()
        if matriz2 is None:
            print("La segunda matriz no se creó correctamente.")
        else:
            matriz_producto = producto_matrices(matriz1, matriz2)
            if matriz_producto is not None:
                print("Producto de matrices:")
                for fila in matriz_producto:
                    print(fila)

