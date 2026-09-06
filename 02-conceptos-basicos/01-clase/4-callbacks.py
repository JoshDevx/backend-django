"""
Es una funcion que se pasa como
un argumento a otra funcion y que se ejecuta en algun punto
durante la ejecucion de esa funcion.
es comun en eventos asincronicos, como al trabajar
con interfaces graficas o procesos que no se
ejecutan secuencialmente
"""


# mostrar_resultado es un callback que se ejecuta despues de que se procesan los datos

def procesar_datos(datos, callback):
    print("Procesando datos...")
    callback(datos)


def mostrar_resultados(resultado):
    print(f"Resultado: {resultado}")


procesar_datos([1,2,3], mostrar_resultados)