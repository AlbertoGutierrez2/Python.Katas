# %%
"""Ejercicio 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
    de cada letra en la cadena. Los espacios no deben ser considerados"""

# %%
texto = str(input('Frase: ')) #Aqui input de la cadena de texto que se desee
texto1 = texto.replace(' ', '')

letras_dic = dict() # Guarda repetición de letras
contador = 0 # Caracteres que se repiten

for letra in texto1: # Por cada letra
    if letra in letras_dic: # Si ya estaba en el dic () significa que se repite
        if letras_dic [letra] == 1:
            contador += 1 # Se agrega al contador
        letras_dic[letra] += 1 # Continua el conteo
    else:
        letras_dic[letra] = 1 # Si la letra no está en el diccionario, la agrega
        
print(texto1)
print(letras_dic)
print(contador)

  
    
    
    

# %%
"""Ejercicio 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()"""

# %%
def doblar(numero):
    return numero*2

numeros = [2, 4, 8, 12, 28, 40, 60]

list(map(doblar, numeros))


# %%
"""3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo."""

# %%
Lista = ['perro', 'gato', 'caballo', 'oso', 'pudoroso']
palabra_objetivo = 'oso'

def objetivo  (palabra):
    if (palabra_objetivo in palabra):
        return True
    else:
        return False
    
Filtro_palabra = filter(objetivo, Lista)

print(list(Filtro_palabra))
    

# %%
"""4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()"""

# %%
a = [7, 10, 14, 8, 26]
b = [6, 7, 7, 4, 24]

list (map(lambda x,y : x-y, a,b))

# %%
"""5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado."""

# %%
lista = [2,4,6,8,10,9]
nota_aprobado = 5

suma = 0

for num in lista:
    suma += num
media = suma /len(lista)

if media >= nota_aprobado:
   print ('Aprobado', media)
else:
    print ('Suspenso', media)
    




# %%
"""6. Escribe una función que calcule el factorial de un número de manera recursiva."""

# %%

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)
    
factorial_recursivo(6)


# %%
"""7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()"""

# %%
tupla = ('rojo', 'azul', 'amarillo')

print(tupla)
print(type(tupla))

def convert(tupla):
    return list(tupla)

lista = convert(tupla)
print (lista)
print (type(lista))



# %%

"""8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no."""

# %%

while True:
      try:
         x = int(input("Introduzca el primer número positivo;  "))
         if x < 0:
            print("Por favor, introduzca un número positivo")
            continue
         y = int(input("Introduzca el segundo número positivo;  "))
         if y < 0:
            print("Por favor, introduzca un número positivo")  
            continue
         division = x/y
         print("División correcta!, el resultado es", division)
         break
      except ValueError:
        print("Debe ingresar un valor numérico")
      except ZeroDivisionError:
        print("El divisor no puede ser cero, por favor introduzca el segundo número mayor que cero")   
        
   

# %%
"""9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()"""

# %%
Animales = ["perro", "gato", "léon", "Hipopótamo", "Mapache", "Tigre",
"Serpiente Pitón", "Vaca", "Cocodrilo", "Oso", "Cabra"]

def Exclusion_animal(x):
    if x in ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]:
        return False
    else:
        return True
    
Animales_1 = filter(Exclusion_animal, Animales)

for x in Animales_1:
    print(x)

# %%
"""10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente."""

# %%

valores = []
while True:
    valor = float(input("Introduzca su lista de números distintos de cero y pulse 0 cuando termine; "))
    if valor == 0:
        break
    else:
        valores.append(valor)
    prom = 0
    for i in valores:
            prom += i
    promedio = prom / len(valores)
if len(valores) == 0:
    print("La lista está vacía. Introduzca al menos dos valores para calcular el promedio")
else:
    print(valores)
    print("Su promedio es de:", round(promedio,2))


# %%
"""11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
adecuadamente."""

# %%

try:
        x = int(input("Introduzca su edad:"))
        if x < 0 or x > 120:
                print("Por favor introduzca un valor entre 0 y 120")
        else:
                try:
                        print(f'Su edad es de: {x} años')
                except ValueError:
                        print("Ha introducito un valor no numérico")
    
                
except ValueError:
                print("Por favor introduzca un valor numérico")


# %%
"""12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()"""

# %%
Frase = input("Introduzca aquí su frase: ")
palabras = Frase.split()
Lista_palabras = list(palabras)
print (Lista_palabras)

Longitudes = list(map(len, Lista_palabras))
print (Longitudes)



# %%
"""13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()"""

# %%
Conjunto_caracteres = ("a", "b", "c", "d", "e", "f", "g")
print(Conjunto_caracteres)

Mayus = list(map(str.upper, Conjunto_caracteres))
print(Mayus)


def Lista_tuplas(Conjunto_caracteres, Mayus):
    return list(map(lambda x,y: (x,y), Conjunto_caracteres, Mayus))

print(Lista_tuplas(Conjunto_caracteres, Mayus))





# %%
"""14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
función filter()"""

# %%
Lista_palabras = ("perro", "gato", "camión", "casa", "murciélago")

letra = "c"

Lista_palabras_filtradas = list(filter(lambda x: x[0] == letra, Lista_palabras))
print(Lista_palabras_filtradas)


# %%
"""15. Crea una función lambda que sume 3 a cada número de una lista dada."""

# %%
Lista_de_numeros = (4, 8 ,25 , 10)

Resultado = list(map(lambda x: x+3, Lista_de_numeros))
print(Resultado)

# %%
"""16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
todas las palabras que sean más largas que n. Usa la función filter()"""

# %%
Texto = "Esto es un texto para resolver el ejercicio dieciseis"
Lista = str.split(Texto)
n = 5

Lista_palabras = list(filter(lambda x: len(x) > n, Lista))
print(Lista_palabras)



# %%
"""17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
corresponde al número quinientos setenta y dos (572). Usa la función reduce()"""

# %%
from functools import reduce

def digitos_a_numero(digitos):
    return reduce(lambda x,y: x*10 + y, digitos)

digitos_a_numero([5, 7, 3])

# %%
"""18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()"""

# %%
  class Estudiante:
      def __init__(self, nombre, edad, calificacion):
          self.nombre = nombre
          self.edad = edad
          self.calificacion = calificacion
          
      def __str__(self):
           return f"{self.nombre} tiene {self.edad} y tuvo una calificación de {self.calificacion}."
          
  lista_estudiantes = [
      Estudiante("Pepe", 25, 91),
      Estudiante("Juan", 40, 57),
      Estudiante("Ana", 28, 90),
      Estudiante("Antonio", 42, 80)
  ]
 
  estudiantes_superiores = filter(lambda e: e.calificacion >= 90, lista_estudiantes)
  [print (e.__str__()) for e in estudiantes_superiores]
  

# %%
"""19. Crea una función lambda que filtre los números impares de una lista dada"""

# %%
numeros = list(range(1 , 11))
print (numeros)

impares = list(filter(lambda n: n % 2 != 0, numeros))
print (impares)

# %%
"""20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
filter()"""

# %%
Lista = ["Pepe", 24,  "Elefante", 48, "Ratón", 35]

Resultado = list(filter(lambda x: isinstance(x, int), Lista))
print(Resultado)


# %%
"""21. Crea una función que calcule el cubo de un número dado mediante una función lambda"""

# %%
numero = 3

cubo = lambda x: x ** 3
print(cubo(3))

# %%
"""22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() ."""

# %%
from functools import reduce

numeros = list(range(1, 6))
print(numeros)

producto = reduce(lambda x,y: x*y, numeros)
print (producto)

# %%
"""23. Concatena una lista de palabras.Usa la función reduce() ."""

# %%
lista = ('H','o','l','a','_','P','e','p','e')

def concatenar(a,b):
    return a+b

Resultado = reduce(concatenar, lista)

print(Resultado)



# %%
"""24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() ."""

# %%

numeros = [10, 2, 3, 1]
print(numeros)

producto = reduce(lambda x,y: x-y, numeros)
print (producto)

# %%
"""25. Crea una función que cuente el número de caracteres en una cadena de texto dada."""

# %%
Texto = "Hola, este es un texto para resolver el ejercicio"
longitud = len(Texto)
print(f"Este texto tiene {longitud} caracteres")

# %%
"""26. Crea una función lambda que calcule el resto de la división entre dos números dados."""

# %%
x = 5
y = 4

Resto = lambda x, y: x % y
print(Resto(x, y))

# %%
"""27. Crea una función que calcule el promedio de una lista de números."""

# %%
lista = (1, 5, 8, 25, 12)

def calculate_average(a):
        x = sum(a)
        y = len(a)
        average = x / y
        return average
    
Resultado = calculate_average(lista)
print(f"El promedio de la lista de números dada es {Resultado}")




# %%
"""28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada."""


# %%
lista = []
repetidos = None
my_list= [1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8]

for i in my_list:
    if i in lista and not repetidos:
        repetidos = i
    lista.append(i)
if repetidos:
    print(f'El primer elemento duplicado de la lista es: {repetidos}')
else:
    print("No existen elementos duplicados en la lista")

    

# %%
"""29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
carácter '#', excepto los últimos cuatro."""

# %%
number = 123456789
cadena = str(number)
print(cadena)
masked = len(cadena[:-4])*"#"+cadena[-4:]
print(masked)



# %%
"""30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
pero en diferente orden."""

# %%
in_list = ['casa', 'roma', 'saca', 'perla', 'mora', 'regla']
anagramas = {}

for palabra in in_list:
    code = ' '. join(sorted(palabra))
    if code in anagramas:
        print(f'{anagramas[code]} = {palabra} Is an ANAGRAM')
    else:
        anagramas[code] = palabra
        print(f'{palabra} Is Not an ANAGRAM')
        
list_anagram = list(anagramas.values())
print(list_anagram)

# %%
"""31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción."""

# %%
    lista = []
    valor = str(input('Ingrese el nombre para la lista o pulse "x" para terminar'))
    while valor != "x":
        lista.append(valor)   
        valor = str(input('Ingrese el nombre para la lista o pulse "x" para terminar'))
    print(f'Los nombres de la lista de invitados son: {lista}')
    
    Nombre = input('Por favor, ingrese un nombre para buscar en la lista: ') 
    print(Nombre)
    
   
    if Nombre in lista:
            print(f'{Nombre} se encuentra en la lista')
    else:
            print(f'Lo sentimos, {Nombre} no está en la lista')
        
    

# %%
"""32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí."""

# %%
Lista_empleados = []

for a in range(3):
    nombre_completo = input('Ingrese su nombre completo: ') 
    puesto = input('Ingrese su profesión: ')
    Lista_empleados.append([nombre_completo, puesto])
print(f'Los nombre y profesiones de la lista de empleados son: {Lista_empleados}')

Lista_empleados_dict = dict(Lista_empleados)
type(Lista_empleados_dict)

nombre_completo_buscado = input('Por favor ingrese el nombre completo del empleado: ')
print(f'El nombre del empleado buscado es: {nombre_completo_buscado}')


if nombre_completo_buscado in Lista_empleados_dict:
            print(f'{nombre_completo_buscado} trabaja como {Lista_empleados_dict.get(nombre_completo_buscado)}')
            
else:
            print('El empleado buscado no trabaja aquí')
       
 
        


# %%
"""33. Crea una función lambda que sume elementos correspondientes de dos listas dadas."""

# %%
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [3, 4, 5, 6, 7]

resultado = list(map(lambda x, y: x + y, lista_1, lista_2))
print(resultado)

# %%
"""34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol.
Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método
info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
mismas.
Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol."""

# %%

class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento
        
def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre);
    subarbol.hijos.append(Arbol(elemento))
def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if (arbolBuscado != None):
            return arbolBuscado
    return None 
        
abuela = "Jacqueline Gurney"
marge = "Marge Bouvier"
patty = "Patty Bouvier"
selma = "Selma Bouvier"
bart = "Bart Simpson"
lisa = "Lisa Simpson"
maggie = "Maggie Simpson"
ling = "Ling Bouvier"
arbol = Arbol(abuela)
agregarElemento(arbol, patty, abuela)
agregarElemento(arbol, selma, abuela)
agregarElemento(arbol, ling, selma)
agregarElemento(arbol, marge, abuela)
agregarElemento(arbol, bart, marge)
agregarElemento(arbol, lisa, marge)
agregarElemento(arbol, maggie, marge)

def profundidad(arbol):
    if len(arbol.hijos) == 0: 
        return 1
    return 1 + max(map(profundidad,arbol.hijos)) 
def grado(arbol):
    return max(map(grado, arbol.hijos) + [len(arbol.hijos)])

def ejecutarProfundidadPrimero(arbol, funcion):
    funcion(arbol.elemento)
    for hijo in arbol.hijos:
        ejecutarProfundidadPrimero(hijo, funcion)  
        
def printElement(element):
    print (element)
ejecutarProfundidadPrimero(arbol, printElement)

print(f'La profundidad de este arbol es {profundidad(arbol)}')

        
        

# %%
"""36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo.
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia"."""

# %%
class UsuarioBanco:    
    def __init__(self, username, balance, bank_account):
        self.username = username
        self.balance = balance
        self.bank_account = bank_account
        
Alicia = UsuarioBanco('Alicia', 100, True)
Bob = UsuarioBanco('Bob', 50, True)

print(f'El saldo inicial de {Alicia.username} es de {Alicia.balance}')
print(f'El saldo inicial de {Bob.username} es de {Bob.balance}')

def agregar_dinero(self):
        return self.balance + x

x= 20
Resultado = agregar_dinero(Bob)
print (f'Despues de agregar {x} el saldo de {Bob.username} es de {Resultado}')
 
def transferir_dinero (self):
        cantidad_a_transferir = y
        saldo_emisor = self.balance + x
        saldo_receptor = Alicia.balance
        nombre_emisor = self.username
        nombre_receptor =Alicia.username
        
        if cantidad_a_transferir > saldo_emisor:
                print(f'Lo siento {nombre_emisor}, no tiene suficiente saldo para hacer la transferencia de {cantidad_a_transferir}')
        else:
                Resultado1= saldo_emisor - cantidad_a_transferir
                Resultado2 = saldo_receptor + cantidad_a_transferir
                print(f'Se ha realizado la transferencia. Ahora el saldo de {nombre_emisor} es de {Resultado1} y el saldo de {nombre_receptor} es de {Resultado2}')

y= 80
Resultado3 = transferir_dinero(Bob)

def retirar_dinero(self):
        cantidad_a_retirar = z
        
        if cantidad_a_retirar > self.balance:
                print(f'Lo siento, no tiene suficiente saldo para retirar esa cantidad')
        else:
                Resultado4 = self.balance - cantidad_a_retirar
                print(f'{self.username}, despues de retirar {cantidad_a_retirar}, su saldo es de {Resultado4}')
                
z = 50
Resultado5 = retirar_dinero(Alicia)                
        

# %%
"""37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto .
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
número de argumentos variable según la opción indicada.
Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto"""

# %%
texto = 'Esto es un texto para completar el ejercicio treinta y siete, aunque no es un texto muy largo'

opcion = 0

while opcion != 4:
        print('Menu de opciones: ')
        print('1.contar palabras')
        print('2.reemplazar palabra')
        print('3. eliminar palabra')
        print('4. Salir')
        opcion = int(input('Por favor ingresa tu opcion: '))

        if (opcion == 1):
                print('Ha elegido la opcion 1. contar palabras')
                contador = {}
                palabras = texto.replace(',', '').replace(',', '').lower().split()
    
                for elem in palabras:
                        if elem in contador:
                                contador[elem] += 1
                        else:
                                 contador[elem] = 1
            
                print (contador)
                
        elif (opcion == 2):
                print('Ha eledigo la opción 2. reemplazar palabra')
                Palabra_a_reemplazar = str(input(f'Por favor, indique la palabra del texto a reemplazar: '))
                Nueva_palabra = str(input(f'Por favor, indique la nueva palabra: '))
                texto_nuevo = texto.replace(Palabra_a_reemplazar, Nueva_palabra)
                print(texto_nuevo)
                
        elif (opcion == 3):
                print('Ha elegido la opción 3. eliminar palabra')
                Palabra_a_eliminar = str(input(f'Por favor, indique la palabra del texto a eliminar: '))
                texto_nuevo = texto.replace(Palabra_a_eliminar,'')
                print(texto_nuevo)
                
        elif (opcion == 4):
                
                print('Salir del programa')
                break
        else:
                print('Opción incorrecta')
                
        


# %%
"""38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario."""

# %%
Hora_usuario = int(input('Introduzca que hora es en formato (1 a 24h.): '))
print(f'Ha indicado que ahora son las {Hora_usuario}')

if 1 <= Hora_usuario <= 7 or 20 < Hora_usuario <= 24:
    print('Es de noche')
elif 7 < Hora_usuario <= 14:
    print('Es de día')
else:
    print("Es por la tarde")

# %%
"""39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente"""

# %%
calificacion_numerica = int(input('Introduzca su califación numérica: '))
print(f'Su calificación es de {calificacion_numerica}')

if 0 < calificacion_numerica < 69:
    print('Insuficiente')
elif 70 < calificacion_numerica < 79:
    print('bien')
elif 80 < calificacion_numerica < 89:
    print('muy bien')
else:
    print('excelente')

# %%
"""40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura)."""

# %%
figura_dada = input('Escoja una figura (rectangulo, circulo o triangulo): ')
print(f'La figura escogida es un {figura_dada}')

if figura_dada == 'triangulo':
            def calcular_area_triangulo (base, altura):
                area = (base * altura) / 2
                return area

            base = float(input('Introduzca la base de su triangulo (cm): '))
            altura = float(input('Introduzca la altura de su triangulo (cm): '))
 
            area_triangle = calcular_area_triangulo(base, altura)
            print (f'El area de su triangulo es de {area_triangle} cm')

elif figura_dada == 'circulo':
            diametro_circle = float(input('Introduzca el diametro de su circulo (cm): '))
            import math
            radio_circle = diametro_circle / 2
            area_circle = round(math.pi * (radio_circle**2),2)
            print (f'El area de su circulo es de {area_circle} cm')        
            
else:
            base_rectangle = float(input('Introduzca la base de su rectangulo (cm): '))
            altura_rectangle = float(input('Introduzca la altura de su rectangulo (cm): '))
            area_rectangle = (base_rectangle * altura_rectangle)
            print (f'El area de su rectangulo es de {area_rectangle} cm')
    
    

# %%
"""41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python."""

# %%
Precio_original = float(input('Por favor introduzca el precio original de su artículo: '))
Cupon_descuento = str(input('¿Tiene cupón de descuento? S/N: '))

if Cupon_descuento == 'S':
    valor_cupon_descuento = float(input('Por favor introduzca el valor de su cupón de descuento; '))
    if valor_cupon_descuento > 0:
                precio_final_compra = (Precio_original - valor_cupon_descuento)
                print (f'El precio final de su compra es de {precio_final_compra}€')
    else:
                print ('El valor de su cupón no es válido y no puede ser aplicado')
                print (f'El precio final de su compra es de {Precio_original}€')       
else:
    print('No dispone de cupón de descuento')
    print (f'El precio final de su compra es de {Precio_original}€')
    


