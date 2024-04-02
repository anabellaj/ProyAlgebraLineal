from funciones import *    
  
def main ():  
    print('\n\nBienvenido! A partir de este programa ud. podrá resolver sistemas de ecuaciones con la cantidad de iteraciones deseadas utilizando el sistema Jacobí')
    while True:
        dimension = pedir_dimension()
        ecuaciones = pedir_ecuaciones(dimension)
        matriz_a, matriz_x, matriz_b = convertir_matricial(ecuaciones, dimension)
        print (f'Se convierte el sistema a su forma matricial y resulta:\n')
        print ('Matriz A: ')
        print_matriz (matriz_a)
        print ('\nMatriz X: ')
        print_matriz(matriz_x)
        print ('\nMatriz b: ')
        print_matriz(matriz_b)
        if es_matriz_bien_condicionada(matriz_a):
            print("\nLa matriz proporcionada está bien condicionada.")
            iteraciones = pedir_iteraciones()
            resultado = metodo_jacobi(matriz_a, matriz_x, matriz_b, iteraciones)
            imprimir_resultados(resultado, iteraciones)
            break
        else:
            print("\nLa matriz proporcionada no está bien condicionada. Por favor vuelva a intentarlo.")
    
main ()