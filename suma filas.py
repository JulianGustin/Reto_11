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

def sumar_fila(matriz, fila):
    if matriz is None:
        return None
    #Verificar si el indice es valido
    if fila < 0 or fila > len(matriz[0]):
        print("Indice fuera del rango valido")
        return None
    suma = 0
    for num in matriz[fila]:
        suma += num
    return suma

if __name__ == "__main__":
    matriz = crear_matriz()
    if matriz is None:
        print("La matriz no se creo correctamente")
    else: 
        fila = int(input("Ingrese la fila a sumar: ")) - 1
        resultado = sumar_fila(matriz, fila)
        if resultado is not None:
            print(f"La suma de los elementos de la columna {fila+1} es {resultado}")