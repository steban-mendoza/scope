import this

def suma (a,b):
    c = a + b
    print("La suma de a + b es: ", c)

def multi (a,b):
    c = a * b
    print("La suma de a + b es: ", c)

def resta (a,b):
    c = a - b
    print("La suma de a + b es: ", c)

suma(10,5)
multi(10,5)
resta(10,5)

# variables locales
def imprimir_nombre():
    mi_nombre="Esteman"
    print("El nombre de la funcion es: ", mi_nombre, id(mi_nombre), sep="-->")
imprimir_nombre()
#print("El nombre de la variable local es: ", mi_nombre)

# Variables enclosing
mi_nombre = "Esteban"

def imprimir_nombre():
    global mi_nombre
    mi_nombre="Esteman"
    print("El nombre de la funcion es: ", mi_nombre, id(mi_nombre), sep="-->")

print("El nombre fuera de la funcion es: ", mi_nombre, id(mi_nombre), sep="-->")
imprimir_nombre()

# Variable global

mi_nombre = "Esteban"
def imprimir_nombre():
    print("El nombre de la funcion es: ", mi_nombre, id(mi_nombre), sep="-->")

print("El nombre fuera de la funcion es: ", mi_nombre, id(mi_nombre), sep="-->")
imprimir_nombre()

    