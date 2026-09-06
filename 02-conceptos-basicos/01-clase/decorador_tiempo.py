import time


def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time() # Tiempo antes de la ejecucion
        resultado = func(*args, **kwargs) # Ejecuta la funcion original
        fin = time.time() # Tiempo despues de la ejecucion
        print(f"Tiempo de ejecucion de {func.__name__}: {fin-inicio:.4f} segundos")
        return resultado
    return wrapper


# Aplicamos el decorador a la funcion
@medir_tiempo
def hacer_calculo():
    total = 0
    for i in range(1,10000):
        total += 1
    return total


#Llamamos a la funcion
hacer_calculo()