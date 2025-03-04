# -*- coding: utf-8 -*-

# Reiniciar lista de variables


# --------- Tipos de datos en Python ---------
# Entero (int)
edad = 25
print("Edad (int):", edad)

# Decimal (float)
pi = 3.1416
print("Pi (float):", pi)

# Cadena de texto (str, habitualmente llamado string)
nombre = "Juan"
print("Nombre (str):", nombre)

# Booleano (bool)
es_mayor = True
es_menor = False
print("Es mayor de edad (bool):", es_mayor)


# Mostrar el tipo de variable
type(edad)
type(pi)
type(nombre)
type(es_mayor)


# Convertir una variable de un tipo a otro (casting)
# Las funciones más habituales para hacer casting son: int(), float(), str()
# Utilizamos input para leer una entrada en la consola y así introducir un dato

edad = input("Introduce tu edad: ")
print(edad * 2) # Lo estamos mostrando en formato texto

edad = int(edad)
print(edad * 2)

edad_entero = int(input("Introduce tu edad: "))
print(edad_entero * 2)

# --------- Operadores matemáticos ---------


# Calculadora: se realiza la operación y se muestra el valor, pero no se almacena ni trabaja con él
25 + 3
0.1 + 0.2
# Por qué el resultado da decimales inexactos: https://explodat.cl/Analytics/data-science/cuidado-con-los-decimales-en-python/

# Utilizar variables para las operaciones
a = 10
b = 3

# Suma
suma = a + b
print("Suma:", suma)

# Resta
resta = a - b
print("Resta:", resta)

# Multiplicación
multiplicacion = a * b
print("Multiplicación:", multiplicacion)


# Raíz cúbica porque b = 3
raiz = a * 1/b
print("Multiplicación:", raiz)


# División
division = a / b
print("División:", division)

# Exponente
exponente = a ** b
print("Exponente:", exponente)

# División entera
division_entera = a // b
print("División entera:", division_entera)

# Módulo (resto de la división)
modulo = a % b
print("Módulo:", modulo)


# --------- Operadores comparativos ---------

c = 15
d = 20

# Igual que
es_igual = c == d
print("c == d:", es_igual)

# Distinto de
print("c != d:", c != d)

# Mayor que
print("c > d:", c > d)

# Menor que
print("c < d:", c < d)

# Mayor o igual que
print("c >= d:", c >= d)

# Menor o igual que
print("c <= d:", c <= d)


# --------- Operadores lógicos ---------

x = True
y = False

# and
print("x and y:", x and y)

# or
print("x or y:", x or y)

# not
print("not x:", not x)


# --------- Comentarios ---------

# Esto es un comentario de una sola línea
# Explica lo que hace el código sin ser ejecutado

"""
Este es un comentario de múltiples líneas.
Puedes usarlo para explicar secciones más largas del código
o para documentar cómo funciona un bloque de instrucciones.
"""



# --------- Entrada de datos y operaciones ---------

mi_edad = int(input("Introduce tu edad: "))
aita_edad = int(input("Introduce la edad de tu aita: "))

suma = mi_edad + aita_edad  
print("La suma de vuestras edades es:", suma)

resta_orden = mi_edad - aita_edad 
print("La resta de vuestras edades es:", resta_orden)
resta_desorden = aita_edad - mi_edad
print("La resta de vuestras edades es:", resta_desorden)

diferencia = abs(mi_edad - aita_edad)
print("La diferencia de vuestras edades es de", diferencia, "años")
