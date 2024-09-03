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

def sumar_matrices(matriz1, matriz2):
    #Obtiene el numero de filas y columnas de la matriz 1
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_suma = [] #Inicializa la matriz del resultado
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            #Suma los elementos correspondientes de ambas matrices
            fila_suma.append(matriz1[i][j] + matriz2[i][j])
        matriz_suma.append(fila_suma) #Agrega la fila resultante a la matriz
    return matriz_suma

def restar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_resta = []
    for i in range(filas):
        fila_resta = []
        for j in range(columnas):
            fila_resta.append(matriz1[i][j] - matriz2[i][j])
        matriz_resta.append(fila_resta)
    return matriz_resta

def igual_tamaño(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]): #Verifica que tanto las filas como las columnas sean iguales en tamaño
        print("Las matrices deben ser de igual tamaño.")
        return False
    return True

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
            if igual_tamaño(matriz1, matriz2):
                print("Suma de matrices:")
                matriz_suma = sumar_matrices(matriz1, matriz2)
                for fila in matriz_suma:
                    print(fila)
                
                print("Resta de matrices:")
                matriz_resta = restar_matrices(matriz1, matriz2)
                for fila in matriz_resta:
                    print(fila)
