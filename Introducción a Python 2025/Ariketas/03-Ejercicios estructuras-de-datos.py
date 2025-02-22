### Ejercicios basados en `03-estructuras-de-datos.py`
# 1. **Listas**:
"""
    - Crea una lista con los números del 1 al 5. Luego, añade el número 6 al final de la lista y el número 0 al principio. Muestra la lista resultante.
    - Pide al usuario que ingrese 3 nombres y almacénalos en una lista. Luego, muestra el segundo nombre de la lista.
    - Crea una lista con varios elementos y usa slicing para extraer una sublista que contenga los elementos desde el segundo hasta el cuarto.
"""

lista = [1,2,3,4,5]
lista.append(6)
lista.insert(0, 0)
print(lista)    

nombres = []
for i in range(3):
    nombre = input("Introduce un nombre: ")
    nombres.append(nombre)
print(nombres[1])   



lista_loca = ["Maikel", "Nahikari", "Borja", "Daniel", "Ane", "Iker", "Aitor", "Iñaki", "Ander", "Genaro", "Mikel", "Iñigo"]
lista_loca = list(["Maikel", "Nahikari", "Borja", "Daniel", "Ane", "Iker", "Aitor", "Iñaki", "Ander", "Genaro", "Mikel", "Iñigo"])
numeros_locos = list(range(2,2300,2))

sublista = lista_loca[1:4]
sublista = lista_loca[1:9]
print(sublista)


# 2. **Tuplas**:
"""
    - Crea una tupla con los días de la semana. Intenta modificar uno de los elementos y observa qué sucede.
    - Convierte una tupla en una lista, añade un nuevo elemento y luego convierte la lista de nuevo en una tupla.
"""

dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
# dias_semana[0] = "Astelehena"  # Esto lanzará un error, ya que las tuplas son inmutables  
lista_desde_tupla = list(dias_semana)
lista_desde_tupla.append("No queda mas dinas tio!")
dias_semana = tuple(lista_desde_tupla)
print(dias_semana)



# 3. **Diccionarios**:
"""
    - Crea un diccionario que represente a una persona con las claves "nombre", "edad" y "ciudad". Luego, añade una nueva clave "profesión" y modifica el valor de la clave "edad".
    - Pide al usuario que ingrese su nombre y edad, y almacena estos valores en un diccionario. Luego, muestra el diccionario.
"""

persona = {
    "nombre": "Ander",
    "edad": 28,
    "ciudad": "Errenteria"
}

persona["profesión"] = "Informático"
persona["edad"] = 38    
print(persona)

nombre_usuario = {}
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
nombre_usuario["nombre"] = nombre
nombre_usuario["edad"] = edad
print(nombre_usuario["nombre"][5])


# 4. **Conjuntos**:
"""
    - Crea dos conjuntos con números del 1 al 5 y del 3 al 7. Realiza las siguientes operaciones y muestra los resultados:
        - Unión de ambos conjuntos
        - Intersección de ambos conjuntos
        - Diferencia entre el primer y el segundo conjunto
    - Pide al usuario que ingrese varios números y almacénalos en un conjunto. Luego, muestra cuántos números únicos ingresó el usuario.
"""

#set_1 = {1, 2, 3, 4, 5}
set_1 = set(range(1, 6))
#set_2 = {3, 4, 5, 6, 7}
set_2 = set(range(3, 8))

union = set_1.union(set_2)
print("Unión:", union)
interseccion = set_1.intersection(set_2)
print("Intersección:", interseccion)
diferencia = set_1.difference(set_2)
print("Diferencia:", diferencia)

#En un SET aunque tenga diferentes numeros, solo se queda con los unicos
numeros_usuario = {1,5,3,2,5,6,9,8,8,8,5,4,5,6,3,2,1,1,4,7,8}
print("Números únicos:", len(numeros_usuario))  

# 5. **Listas y diccionarios anidados**:
"""
    - Crea una lista anidada que represente una matriz 3x3 (3 filas y 3 columnas). Luego, accede al elemento en la segunda fila y tercera columna.
    - Crea un diccionario anidado que represente a dos estudiantes, cada uno con su nombre, edad y lista de cursos. Luego, añade un nuevo curso a uno de los estudiantes y muestra el diccionario actualizado.
"""
fila1 = [1, 2, 3]
fila2 = [4, 5, 6]   
fila3 = [7, 8, 9]
matriz = [fila1, fila2, fila3]
print(matriz)
print(matriz[1][2])



lista_anidada = [
    ["A1", "B1", "C1"],
    ["A2", "B2", "C2"],
    ["A3", "B3", "C3"]
]
objetivo = lista_anidada[1][2]
print(objetivo)



estudiantes = {
    "estudiante1": {
        "nombre": "Ander",
        "edad": 38,
        "cursos": ["Python"]
    },
    "estudiante2": {
        "nombre": "Genaro",
        "edad": 75,
        "cursos": ["Cosas de la vida", "Arar el campo", "Bocata de panceta"]
    }
}
estudiantes["estudiante1"]["cursos"].append("La universidad de la vida")
print(estudiantes)


### Ejercicio 6: Manipulación de Datos

# 1. **Listas**:
"""
    - Crea una lista con los nombres de cinco ciudades. Luego, pide al usuario que ingrese el nombre de una ciudad y añade esa ciudad al final de la lista. Muestra la lista resultante.
    - Usa slicing para extraer una sublista que contenga las tres primeras ciudades de la lista.
"""

ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"]
nueva_ciudad = input("Introduce el nombre de una ciudad: ")
ciudades.append(nueva_ciudad)
print("Lista de ciudades:", ciudades)

sublista_ciudades = ciudades[0:3]
print("Sublista de las tres primeras ciudades:", sublista_ciudades)

# 2. **Tuplas**:
"""
    - Crea una tupla con los nombres de cinco frutas. Convierte la tupla en una lista, añade una nueva fruta y luego convierte la lista de nuevo en una tupla. Muestra la tupla resultante.
"""

frutas = ("Manzana", "Banana", "Cereza", "Durazno", "Fresa")
lista_frutas = list(frutas)
lista_frutas.append("Mango")
frutas = tuple(lista_frutas)
print("Tupla de frutas modificada:", frutas)

# 3. **Diccionarios**:
"""
    - Crea un diccionario que represente a un libro con las claves "título", "autor" y "año". Luego, añade una nueva clave "género" y modifica el valor de la clave "año".
    - Pide al usuario que ingrese el título y el autor de un libro, y almacena estos valores en un diccionario. Luego, muestra el diccionario.
"""

libro = {
    "título": "Cien Años de Soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967
}
libro["género"] = "Realismo mágico"
libro["año"] = 1970
print("Diccionario del libro:", libro)

titulo = input("Introduce el título de un libro: ")
autor = input("Introduce el autor del libro: ")
nuevo_libro = {
    "título": titulo,
    "autor": autor
}
print("Nuevo diccionario del libro:", nuevo_libro)

# 4. **Conjuntos**:
"""
    - Crea dos conjuntos con los nombres de cinco colores cada uno. Realiza las siguientes operaciones y muestra los resultados:
        - Unión de ambos conjuntos
        - Intersección de ambos conjuntos
        - Diferencia entre el primer y el segundo conjunto
    - Pide al usuario que ingrese varios colores y almacénalos en un conjunto. Luego, muestra cuántos colores únicos ingresó el usuario.
"""

colores_1 = {"rojo", "verde", "azul", "amarillo", "negro"}
colores_2 = {"blanco", "verde", "azul", "morado", "gris"}

union_colores = colores_1.union(colores_2)
print("Unión de colores:", union_colores)

interseccion_colores = colores_1.intersection(colores_2)
print("Intersección de colores:", interseccion_colores)

diferencia_colores = colores_1.difference(colores_2)
print("Diferencia de colores:", diferencia_colores)

colores_usuario = set()
for i in range(5):
    color = input("Introduce un color: ")
    colores_usuario.add(color)
print("Número de colores únicos ingresados:", len(colores_usuario))