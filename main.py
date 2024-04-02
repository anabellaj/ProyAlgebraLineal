from funciones import *    
  
def main ():  
    print('Bienvenido! A partir de este programa ud. podrá resolver sistemas de ecuaciones con la cantidad de iteraciones deseadas utilizando el sistema Jacobí')
    dimension = pedir_dimension()
    ecuaciones = pedir_ecuaciones(dimension)
    matriz_a, matriz_x, matriz_b = convertir_matricial(ecuaciones, dimension)
    iteraciones = pedir_iteraciones()
    resultado = metodo_jacobi(matriz_a, matriz_x, matriz_b, iteraciones)
    imprimir_resultados(resultado, iteraciones)

    if es_matriz_bien_condicionada(matriz_a):
        print("La matriz que proporcionaste está bien condicionada.")
    else:
        print("La matriz que proporcionaste no está bien condicionada.")


main ()