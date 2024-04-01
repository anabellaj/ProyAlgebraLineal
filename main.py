from funciones import *    
  
def main ():  
    dimension = pedir_dimension()
    ecuaciones = pedir_ecuaciones(dimension)
    matriz_a, matriz_x, matriz_b = convertir_matricial(ecuaciones, dimension)
    print(matriz_a, matriz_x, matriz_b)


main ()