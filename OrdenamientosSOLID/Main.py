import random
import time
#from OrdenableAbstract import Ordenamiento
from Burbuja import Burbuja
from BurbujaMejorado import BurbujaMejorado
from Seleccion import Seleccion
from Insercion import Insercion


def generar_aleatorios():
    data = []
    for i in range(1000):
        #https://docs.python.org/3/library/random.html
        data.append(random.randint(1,10000000))
    
    return data


if __name__ == '__main__':
        data = [4,3,2,1,5]
        #data = ["quicksort","burbuja","seleccion","inserción"]
        print("Burbuja normal...")
        burbuja = Burbuja()
        tiempo_inicio = time.time()
        #burbuja.ordenar(data);
        tiempo_fin = time.time()-tiempo_inicio
        print("Tiempo para burbuja normal: ", tiempo_fin)
        
        print("\nBurbuja mejorado...")
        data = [1,7,11,2,0,5,10,3,4]
        burbuja_mejorado = BurbujaMejorado()
        tiempo_inicio = time.time()
        #burbuja_mejorado.ordenar(data)
        tiempo_fin = time.time()-tiempo_inicio
        print("\nTiempo para burbuja mejorado: ", tiempo_fin)
        
        print("\nSeleccion...")
        data = [1,2,3,4,5]
        seleccion = Seleccion()
        tiempo_inicio = time.time()
        seleccion.ordenar(data)
        tiempo_fin = time.time()-tiempo_inicio
        print("\nTiempo para seleccion: ", tiempo_fin)
        
        print("\nInserción...")
        data = [1,2,3,4,5]
        insercion = Insercion()
        tiempo_inicio = time.time()
        insercion.ordenar(data)
        tiempo_fin = time.time()-tiempo_inicio
        print("\nTiempo para insercion: ", tiempo_fin)
        

        