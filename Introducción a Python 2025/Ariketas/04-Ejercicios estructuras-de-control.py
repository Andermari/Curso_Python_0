# Ejercicios sobre Condicionales (if, elif, else)
# Comparación de números:

"""
Pide al usuario que ingrese dos números. 
Compara los números y muestra un mensaje indicando cuál es mayor o si son iguales.
"""
num1 = int(input("Mete el primer número: "))
num2 = int(input("Mete el segundo número: "))    
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num1} es menor que {num2}")




"""
Verificación de edad:

Pide al usuario que ingrese su edad. 
Si es mayor o igual a 18, muestra "Eres mayor de edad". 
Si es menor, muestra "Eres menor de edad".
"""
edad = int(input("Cuántos años tienes tu, puta vieja!! "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

"""
Clasificación de notas:
Pide al usuario que ingrese una nota (entre 0 y 10). Clasifica la nota en:
"Suspenso" si es menor que 5.
"Aprobado" si es entre 5 y 6.
"Notable" si es entre 7 y 8.
"Sobresaliente" si es 9 o 10.
"""
mensaje = "Mete la nota: "
while True:
    nota = float(input(mensaje))
    if nota < 5:
        print("Penkaste notario")
        break
    elif nota >= 5 and nota < 7:
        print("Sufi, ala, a celebrarlo")
        break
    elif nota >= 7 and nota < 9:
        print("Ni tan mal")
        break
    elif nota >= 9 and nota <= 10:
        print("Deberías salir a vivir...")
        break
    else:
        mensaje = "La nota tiene que ser entre 0 y 10, no seas tonto"
        print("La nota tiene que ser entre 0 y 10, no seas tonto")



"""
Días de la semana:

Pide al usuario que ingrese un número del 1 al 7. 
Muestra el día de la semana correspondiente (1 = Lunes, 2 = Martes, etc.). 
Si el número no está en ese rango, muestra "Número inválido".
"""

dia_semana = int(input("Mete un número del 1 al 7: "))
if dia_semana == 1:
    print("Lunes")
elif dia_semana == 2:
    print("Martes")
elif dia_semana == 3:
    print("Miércoles")
elif dia_semana == 4:
    print("Jueves")
elif dia_semana == 5:
    print("Viernes")
elif dia_semana == 6:
    print("Sábado")
elif dia_semana == 7:
    print("Domingo")
else:
    print("Pero tu cunatos dias crees que tiene la semana?")

# Ejercicios sobre Bucles (while y for)
"""
Contador con while:

Usa un bucle while para mostrar los números del 1 al 10.
"""
contador = 1
while contador <= 10:
    print(contador, end=" - ")
    contador += 1

"""
Suma de números:

Pide al usuario que ingrese números hasta que ingrese el número 0. 
Luego, muestra la suma de todos los números ingresados.
"""

suma = 0
contador_numeros_metidos = 0
while True:
    num = int(input("Mete un número: "))
    if num == 0:
        break
    suma += num
    contador_numeros_metidos += 1
print(f"La suma de los números es {suma} y has metido un total de {contador_numeros_metidos} números")  


"""
Tabla de multiplicar:

Pide al usuario que ingrese un número y muestra la tabla de multiplicar de ese número del 1 al 10 usando un bucle for.
"""
numero_a_multiplicar = int(input("Mete un número: "))
for i in range(1, 11):
    print(f"- {numero_a_multiplicar} x {i} = {numero_a_multiplicar * i}")

"""
Bucle for con range:

Usa un bucle for para mostrar los números pares del 2 al 20.
"""
for i in range(2, 21, 2):
    print(i, end=" ")

for i in range(2, 21):
    if i % 2 == 0:
        print(f"El número {i} es PAR y lo sabes...")   


"""
Bucle for con enumerate:

Crea una lista de nombres (por ejemplo, ["Ana", "Juan", "Luis"]). 
Usa un bucle for con enumerate para mostrar el índice y el nombre de cada persona.

"""

lista_nombres = ["Ana", "Juan", "Luis", "Pedro", "María", "José", "Lola", "Manolo", "Pepa", "Paco","Anders", "Johan", "Lars", "Sven", "Greta", "Ingrid", "Bjorn", "Karl", "Erik", "Olaf", "Sofia", "Astrid", "Inga", "Lena", "Sara", "Hanna", "Karin", "Emma", "Elsa", "Anna", "Johanna", "Kerstin", "Linnéa", "Maja", "Malin", "Elin", "Ida", "Eva", "Kristina", "Margareta", "Elisabeth", "Maria", "Birgitta", "Ingegerd", "Katarina", "Helena", "Sofia", "Agnes", "Hedvig", "Lovisa", "Ebba", "Jenny", "Johanna", "Klara", "Matilda", "Sara", "Emilia", "Julia", "Linnea", "Maja", "Wilma", "Alma", "Ella", "Alicia", "Olivia", "Elsa", "Ester", "Ellen", "Signe", "Selma", "Hilda", "Agda", "Gurli", "Greta", "Ingrid", "Birgit", "Karin", "Märta", "Britt", "Gun", "Ulla", "Annika", "Lena", "Anette", "Lotta", "Lena","Miroslav", "Jiří", "Jan", "Petr", "Pavel", "Václav", "Josef", "Jaroslav", "Martin", "Marek", "Tomáš", "Zdeněk", "Jiří", "Petr", "Pavel", "Lukáš", "Miroslav", "Jan", "Josef", "Jaroslav", "Martin", "Marek", "Tomáš", "Zdeněk", "Jiří", "Petr", "Pavel", "Václav", "Josef", "Jaroslav", "Martin", "Marek", "Tomáš", "Zdeněk", "Jiří", "Petr", "Pavel", "Lukáš", "Miroslav", "Jan", "Josef", "Jaroslav", "Martin", "Marek", "Tomáš", "Zdeněk", "Jiří", "Petr", "Pavel", "Václav", "Josef", "Jaroslav", "Martin", "Marek", "Tomáš", "Zdeněk", "Jiří", "Petr", "Pavel", "Lukáš", "Miroslav", "Jan", "Josef", "Jaroslav", "Martin", "Marek", "Tomáš", "Zdeněk", "Jiří", "Petr", "Pavel", "Václav", "Josef", "Jaroslav", "Martin", "Marek", "Tomáš", "Zdeněk", "Jiří", "Petr", "Pavel", "Lukáš", "Miroslav", "Jan", "Josef", "Jaroslav", "Martin", "Marek", "Tomáš", "Zdeněk", "Jiří", "Petr", "Pavel", "Václav", "Josef", "Jaroslav", "Martin", "Marek", "Tomáš", "Zdeněk", "Jiří", "Petr", "Pavel", "Lukáš", "Miroslav", "Jan"]

for indice, nombre in enumerate(lista_nombres):
    print(f"Índice: {indice}, Nombre loco: {nombre}")




"""
Ejercicios sobre break, continue, y pass
Búsqueda en una lista:

Crea una lista de números (por ejemplo, [10, 20, 30, 40, 50]). Pide al usuario que ingrese un número y usa un bucle for para buscar ese número en la lista. Si lo encuentra, usa break para detener el bucle y muestra "Número encontrado". Si no lo encuentra, muestra "Número no encontrado".
"""

lista_numeros = [120,12,51,46,87,1,51,32,6,98,46,32,514,51,2514]
numero_usuario = int(input("Mete un número: "))
for numero in lista_numeros:
    if numero == numero_usuario:
        print("Número encontrado")
        break
else:
    print("Número no encontrado")


"""
Saltar números impares:

Usa un bucle for para mostrar los números del 1 al 10, pero usa continue para saltar los números impares.
"""

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i, end=" - ")

"""
Uso de pass:

Crea un condicional que verifique si un número es mayor que 10. 
Si es mayor, no hagas nada (usa pass). 
Si no, muestra "El número es menor o igual a 10".
"""

numero = 100
if numero > 10:
    pass    
else:
    print("El número es menor o igual a 10")


# Ejercicios avanzados (Bucles anidados y condiciones)
"""
Matriz de números:

Crea una matriz 3x3 (una lista de listas) con números del 1 al 9. 
Usa bucles anidados para recorrer la matriz y mostrar cada elemento.
"""

matriz_a = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"], 
    ["C1", "C2", "C3"]
]

matriz_b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz_a:
    print("|", end="")
    for elemento in fila:
        print(elemento, end="|")
    print()

print()

for fila in matriz_b:
    print("|", end="")
    for elemento in fila:
        print(elemento, end="|")
    print()

"""
Números primos:

Pide al usuario que ingrese un número. 
Usa un bucle for para verificar si el número es primo (solo divisible por 1 y por sí mismo). 
Muestra "Es primo" o "No es primo".
"""

numero = int(input("Mete un número: "))
es_primo = True
for i in range(2, numero): #porque el 1 hace que todo se vaya a la mierda
    if numero % i == 0:
        es_primo = False
        break
if es_primo:
    print("Es primo")   
else:
    print("No es primo")


"""
Bucle for con else:

Usa un bucle for para recorrer una lista de números. 
Si encuentras un número negativo, usa break para detener el bucle. 
Si no encuentras ningún número negativo, muestra "Todos los números son positivos" 
usando el bloque else.
"""
lista_numeros = [120,12,51,46,87,1,51,32,-6,98,46,32,514,51,2514]
posicion = 0
for numero in lista_numeros:
    posicion += 1
    if numero < 0:
        print(f"Número negativo encontrado.\nEn la posición {posicion} hay un {numero}")
        break
else:
    print("Todos los números son positivos")


"""
Detección de múltiplos:

Usa un bucle for para recorrer los números del 1 al 20. Si el número es múltiplo de 3, muestra "Múltiplo de 3". Si es múltiplo de 5, muestra "Múltiplo de 5". Si es múltiplo de ambos, muestra "Múltiplo de 3 y 5".
"""

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} es múltiplo de 3 y 5")
    elif i % 3 == 0:
        print(f"{i} es múltiplo de 3")
    elif i % 5 == 0:
        print(f"{i} es múltiplo de 5")

"""
Juego de adivinanza:

Crea un juego en el que el usuario tenga que adivinar un número secreto entre 1 y 100. Usa un bucle while para permitir múltiples intentos. Si el usuario adivina, muestra "¡Adivinaste!" y termina el juego. Si no, da pistas como "El número es mayor" o "El número es menor".
"""

numero_secreto = 50
while True:
    numero_usuario = int(input("Adivina el número (entre 1 y 100): "))
    if numero_usuario == numero_secreto:
        print("La has clavado man!!!")
        break
    if numero_usuario < numero_secreto:
        print("El número es menor")
    else:
        print("El número es mayor")

    diferencia = numero_usuario - numero_secreto
    print(f"Te has quedado a {abs(diferencia)} numers de acertar... sigue probando")

    