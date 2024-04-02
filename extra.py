import numpy as np

def es_matriz_bien_condicionada(matriz):
    # Convertir la lista de listas a un array de numpy
    matriz_np = np.array(matriz)
    
    # Verificar la condición para cada fila
    for i in range(matriz_np.shape[0]):
        suma = np.sum(np.abs(matriz_np[i, :])) - np.abs(matriz_np[i, i])
        if matriz_np[i, i] <= suma:
            return False
            
    return True

