"""
Decorador para verificar que los parametros sean positivos
"""

def verificar_positivos(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                print(f"Error: {arg} no es un numero positivo.")
            return
        return func(*args, **kwargs)
    return wrapper


# Funcion que usa operacion
@verificar_positivos
def multiplicador(a, b):
    return a * b


# Intentar con numeros negativos
print(multiplicador(5,-3))

# Intentar con numeros positivos
print(multiplicador(4,4))