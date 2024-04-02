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
            intentos = 0
            while not es_matriz_bien_condicionada(matriz_a) and intentos < 10:
                print("\nLa matriz proporcionada no está bien condicionada. Intentando reordenar la matriz...")
                matriz_a, matriz_b = reordenar_matriz(matriz_a, matriz_b)
                print(f'Se reordena la matriz y resulta:\n')
                print('Matriz A: ')
                print_matriz(matriz_a)
                print('\nMatriz X: ')
                print_matriz(matriz_x)
                print('\nMatriz b: ')
                print_matriz(matriz_b)
                intentos += 1

            if es_matriz_bien_condicionada(matriz_a):
                print("\nLa matriz reordenada está bien condicionada.")
                iteraciones = pedir_iteraciones()
                resultado = metodo_jacobi(matriz_a, matriz_x, matriz_b, iteraciones)
                imprimir_resultados(resultado, iteraciones)
            else:
                print(
                    "\nLa matriz reordenada sigue sin estar bien condicionada después de 10 intentos. Por favor vuelva a intentarlo.")
    
main ()