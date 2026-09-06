"""
Forma de modificar o 'adornar' una funcion sin cambiar su codigo
directamente. Es como ponerle un 'envoltorio'
a una funcion para añadir algo extra(como resgistros, validaciones, etc)
"""

def mi_decorador(func):
    def envoltorio():
        print("Antes de ejecutar la funcion")
        func()
        print("Despues de ejecutar la funcion")
    return envoltorio

@mi_decorador
def saludar():
    print("Hola")

saludar()

# Simulacion de un sistema de utenticacion

usuario_autenticado = False

# Decorador para verificar si el usuario esta autenticado
def verificar_aunteticacion(func):
    def wraper(*args, **kwargs):
        if not usuario_autenticado:
            print("Acceso denegado: El usuario no esta autenticado.")
            return
        return func(*args, **kwargs)
    return wraper


# Aplicamos el decorador a una funcion
@verificar_aunteticacion
def realizar_accion_secreta():
    print("Accion secreta realizad con exito")


# Intentamos realizar la accion

realizar_accion_secreta()

usuario_autenticado = True

realizar_accion_secreta()