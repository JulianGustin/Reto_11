# Reto_11
Reto 11 de la clase de programación de computadores
***
## 1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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

```
### Desde este momento, se omite la funcion para crear la matriz
***
## 2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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

```
***
## 3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
```python
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
```
***
## 4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.
```python
def sumar_columna(matriz, columna):
    if matriz is None:
        return None
    #Verificar si el indice es valido
    if columna < 0 or columna > len(matriz[0]):
        print("Indice fuera del rango valido")
        return None
    suma = 0
    for fila in matriz:
        suma += fila[columna]
    return suma

if __name__ == "__main__":
    matriz = crear_matriz()
    if matriz is None:
        print("La matriz no se creo correctamente")
    else: 
        columna = int(input("Ingrese la columna a sumar: ")) - 1
        resultado = sumar_columna(matriz, columna)
        if resultado is not None:
            print(f"La suma de los elementos de la columna {columna+1} es {resultado}")
```
***
## 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.
```python
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
```


