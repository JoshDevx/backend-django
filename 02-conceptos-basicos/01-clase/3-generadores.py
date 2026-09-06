def generador_impares(limite):
    num = 1
    while num <= limite:
        yield num
        num += 2


# Aplicacion practica: Obtener los primeros 10 numeros impares
for numero in generador_impares(20):
    print(numero)


def generador_pares(limite):
    num = 2
    while num <= limite:
        yield num
        num += 2

xd = generador_pares(10)

print(next(xd))
print(next(xd))
print(next(xd))

def fibonacci():
    a , b = 0 , 1
    while True:
        yield a
        a, b = b, a+b

fib_gen = fibonacci()

for _ in range(10):
    print(next(fib_gen))