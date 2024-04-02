from funciones import *    
  
def main ():  
    dimension = pedir_dimension()
    ecuaciones = pedir_ecuaciones(dimension)
    matriz_a, matriz_x, matriz_b = convertir_matricial(ecuaciones, dimension)
    print(matriz_a, matriz_x, matriz_b)

    if es_matriz_bien_condicionada(matriz_a):
        print("La matriz que proporcionaste está bien condicionada.")
    else:
        print("La matriz que proporcionaste no está bien condicionada.")


main ()