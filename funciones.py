import numpy as np
from itertools import permutations

def pedir_dimension():
    while True:
        try:
            dimension = int(input('Por favor ingrese la cantidad de ecuaciones a proporcionar al programa\n>> '))
            if dimension not in range (2, 7):
                print('\nERROR - Únicamente se permiten de 2 a 7 ecuaciones')
            else:
                return dimension
        except:
            print('\nERROR - Por favor ingrese únicamente números, sin letras')
    # ecuaciones = pedir_ecuaciones(dimension)
    # matriz_a, matriz_x, matriz_b = convertir_matricial(ecuaciones, dimension)

    return dimension
            
def pedir_ecuaciones(dimension):
    ecuaciones = []
    for i in range(dimension):
        ecuacion = []
        print(f"\nEcuación {i+1}:")
        for j in range(0, dimension):
            while True:
                variable = input(f"Insert X{j+1}: ")
                try:
                    variable = float(variable)
                    break
                except:
                    print("\nERROR - Por favor ingrese únicamente números, sin letras ni espacios")
            ecuacion.append(variable)
        while True:
                valor_independiente = input("Inserte el valor independiente: ")
                try:
                    valor_independiente = float(valor_independiente)
                    break
                except:
                    print("\nERROR - Por favor ingrese únicamente números, sin letras ni espacios")
        ecuacion.append(valor_independiente)
        ecuaciones.append(ecuacion)
    return ecuaciones      
 
def convertir_matricial(ecuaciones, dimension):
    matriz_x = []
    for n in range(dimension):
        matriz_x.append(f'X{n+1}')
    matriz_a = []
    matriz_b = []
    for ecuacion in ecuaciones:
        eq = []
        cont = 0
        for number in ecuacion:
            if cont == len(ecuacion) - 1 :
                matriz_b.append(number)
                matriz_a.append(eq)
            else:
                eq.append(number)
                cont += 1
    return matriz_a, matriz_x, matriz_b
        
      
def pedir_iteraciones():
    while True:
        try:
            iteraciones = int(input('\nPor favor ingrese la cantidad de iteraciones a realizar\n>> '))
            if iteraciones not in range (1, 101):
                print('\nERROR - Únicamente se permiten de 1 a 100 ecuaciones')
            else:
                return iteraciones
        except:
            print('\nERROR - Por favor ingrese únicamente números, sin letras')
            


def metodo_jacobi(matriz_a, matriz_x, matriz_b, iteraciones):
    dimension = len(matriz_x)
    x_values = [0] * dimension  
    for y in range(iteraciones):
        new_x_values = [0] * dimension
        for i in range(dimension):
            sum_term = 0
            for j in range(dimension):
                if j != i:
                    sum_term += matriz_a[i][j] * x_values[j]
            new_x_values[i] = (matriz_b[i] - sum_term) / matriz_a[i][i]
        x_values = new_x_values
    return x_values


def imprimir_resultados(x_values, iteraciones):
    print(f'\nLuego de realizar {iteraciones} iteraciones utilizando el método jacobí, se obtuvieron los siguientes resultados: ')
    for i, x in enumerate(x_values):
        print(f'X{i+1}: {x}')
    print('\n\n\n')
        
        
def es_matriz_bien_condicionada(matriz):
    matriz_np = np.array(matriz)
    
    for i in range(matriz_np.shape[0]):
        suma = np.sum(np.abs(matriz_np[i, :])) - np.abs(matriz_np[i, i])
        if np.abs(matriz_np[i, i])  <= suma:
            return False
            
    return True


def reordenar_matriz(matriz, matriz_b):

    matriz_np = np.array(matriz)
    matriz_b_np = np.array(matriz_b)

    permutaciones = list(permutations(range(matriz_np.shape[0])))

    for permutacion in permutaciones:
        matriz_permutada_np = matriz_np[list(permutacion), :]
        if es_matriz_bien_condicionada(matriz_permutada_np):

            matriz_b_permutada_np = matriz_b_np[list(permutacion)]
            return matriz_permutada_np.tolist(), matriz_b_permutada_np.tolist()

    return matriz_np.tolist(), matriz_b

# def reordenar_matriz(matriz):
#     matriz_np = np.array(matriz)

#     indices = list(range(matriz_np.shape[0]))
#     permutaciones = list(permutations(indices))

#     for permutacion in permutaciones:
#         matriz_permutada = matriz_np[list(permutacion), :]
#         if es_matriz_bien_condicionada(matriz_permutada):
#             return matriz_permutada.tolist()

#     return matriz_np.tolist()

def print_matriz(matriz):   
    for row in matriz:
        print(f'[{row}]')
        
