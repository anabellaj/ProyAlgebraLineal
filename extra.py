import numpy as np

def convertir_a_matriz(sistema_ecuaciones):
    matriz = []
    for ecuacion in sistema_ecuaciones:
        ecuacion = ecuacion.replace(' ', '')  # Eliminar espacios en blanco
        coeficientes, resultado = ecuacion.split('=')
        coeficientes = coeficientes.split('+')
        fila = []
        for coeficiente in coeficientes:
            coef, variable = obtener_coeficiente_variable(coeficiente)
            if coef != '':
                fila.append(float(coef))
            else:
                fila.append(1)
        fila.append(float(resultado))
        matriz.append(fila)
    return matriz

def obtener_coeficiente_variable(coeficiente):
    variable = ''
    coef = ''
    for char in coeficiente:
        if char.isalpha():
            variable += char
        elif char.isnumeric() or char == '.':
            coef += char
    return coef, variable

def es_estricamente_dominante(matriz):
    diagonales = np.abs(np.diag(matriz))
    suma_filas = np.sum(np.abs(matriz), axis=1) - diagonales
    return np.all(diagonales > suma_filas)

def metodo_jacobi(matriz, iteraciones):
    n = len(matriz)
    x = np.zeros(n)
    resultados = []
    for _ in range(iteraciones):
        x_nuevo = np.zeros(n)
        for i in range(n):
            suma = np.dot(matriz[i][:n], x) - matriz[i][i] * x[i]
            x_nuevo[i] = (matriz[i][-1] - suma) / matriz[i][i]
        resultados.append(x_nuevo)
        x = x_nuevo
    return resultados

# Pedir cantidad de ecuaciones
print("Ingrese la cantidad de ecuaciones en el sistema:")
cantidad_ecuaciones = int(input())

# Pedir ecuaciones
print("Ingrese las ecuaciones en el siguiente formato: ax + by = c")
sistema_ecuaciones = []
for i in range(cantidad_ecuaciones):
    num_ecuacion = i + 1
    ecuacion = input(f"Ingrese la ecuación {num_ecuacion}: ")
    sistema_ecuaciones.append(ecuacion)

# Convertir a matriz
matriz = convertir_a_matriz(sistema_ecuaciones)
print("La matriz del sistema es:")
print(np.array(matriz))

# Verificar si la matriz es estrictamente dominante
if not es_estricamente_dominante(matriz):
    print("El sistema no cumple con la condición de estricta dominancia.")
    print("Por favor, ingrese un nuevo sistema.")
    exit()

# Pedir cantidad de iteraciones
print("Ingrese la cantidad de iteraciones:")
cantidad_iteraciones = int(input())

# Realizar el método de Jacobi
resultados_jacobi = metodo_jacobi(matriz, cantidad_iteraciones)

# Mostrar resultados de cada iteración
print("Resultados de cada iteración:")
for i, resultado in enumerate(resultados_jacobi):
    print(f"Iteración {i+1}: {resultado}")


