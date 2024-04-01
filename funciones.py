import numpy as np

def pedir_dimension():
    while True:
        try:
            dimension = int(input('Por favor ingrese la cantidad de ecuaciones a proporcional al programa\n>> '))
            if dimension not in range (2, 7):
                print('\nERROR - Únicamente se permiten de 2 a 7 ecuaciones')
            else:
                break
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
        
      
