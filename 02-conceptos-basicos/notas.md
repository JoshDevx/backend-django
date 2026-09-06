# Módulo 2 · Conceptos básicos

## Contenido

### Clase 01

**Qué aprendí:**

**Problemas que encontré:**

**Comandos / código clave:**
```
```

### Clase 02

**Qué aprendí:**

**Problemas que encontré:**
- Adivina qué imprime antes de correrlo. La intuición dice "A", porque B va primero y B hereda de A. Pero imprime C.

- Python usa un algoritmo llamado linealización C3, cuya regla clave es que una clase padre nunca aparece antes que sus hijas. Como A es padre de C, tiene que ir después, y el orden real queda D → B → C → A → object. Por eso gana el saludar de C.
**Comandos / código clave:**
```
class A:
    def saludar(self):
        print("A")

class B(A):
    pass

class C(A):
    def saludar(self):
        print("C")

class D(B, C):
    pass

d = D()
d.saludar()
print(D.__mro__)
```

### Clase 03

**Qué aprendí:**

**Problemas que encontré:**

**Comandos / código clave:**
```
```

