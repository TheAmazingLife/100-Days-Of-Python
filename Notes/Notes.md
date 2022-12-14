# 100 Days Of Code

Start day: December 4, 2022

- [100 Days Of Code](#100-days-of-code)
  - [Day 1](#day-1)
  - [Day 2](#day-2)
    - [Primitive Data Types](#primitive-data-types)
    - [Type Error, Type Checking and Type Conversion](#type-error-type-checking-and-type-conversion)
    - [Mathematical Operators](#mathematical-operators)
    - [Number Manipulation and F Strings](#number-manipulation-and-f-strings)
  - [Day 3](#day-3)
    - [Control flow with if / else and Conditional Operators](#control-flow-with-if--else-and-conditional-operators)
    - [Nested if statements and elif statements](#nested-if-statements-and-elif-statements)
    - [Multiple If Statements in Succession](#multiple-if-statements-in-succession)
    - [Logical Operators](#logical-operators)
  - [Day 4](#day-4)
    - [Random Module](#random-module)
    - [Offset and Appending Items to List](#offset-and-appending-items-to-list)
    - [IndexErrors and Working with Nested Lists](#indexerrors-and-working-with-nested-lists)
  - [Day 5](#day-5)
    - [Using the for loop with Python Lists](#using-the-for-loop-with-python-lists)
  - [Day 6](#day-6)
    - [Defining and Calling Python Functions](#defining-and-calling-python-functions)
    - [Indentation in Python](#indentation-in-python)
    - [While Loops](#while-loops)


## Day 1

`print()` imprimir lo que esta dentro de los parentesis
> ex: `print("Hello World")`

Para hacer un salto de Linera
**String**, una cadena de caracteres, limitado por `" "` o `' '` demarcando el principio y el final.
Contatenar **Strings**, concatenarlas a travez de `+`, toma los string y los combina en una sola.

Arreglar errores tipeandolos en google, Q&A Stack Overflow

Indentar de manera adecuada el codigo, no tener espacios en el principio

`input()` ingresar datos al codigo, puede contener un string en dentro de sus parentesis para imprimirlo
> ex: `input("Ingresa tu nombre:")`

Para comentar codigo `#`

`len(var)` Para calcular la longitud de un **String**

Asignamos el valor el input a una **variable**, a la cual se le asigna el valor y puede ser referenciada en un futuro, esta puede ser reasignada
> `nombre = "Joaquin"`

Al nombrar variables hacer un codigo legible, elegir nombres con sentido y que sean significativos, No empezar con numeros al inicio, para espaciarlas usar `_`

Proyecto Dia 1: Band Name Generator

## Day 2

### Primitive Data Types

- String
- Integer
- Float
- Boolean

**String** delimitado por `''` o `""`, mediante subscripting, el numero entre `[]` determina el caracter que vamos a extraer, empezando desde 0

**Integer** numeros positivos o negativos sin decimales, pueden estar separados por `_`, solo para uso visual

**Float** numeros decimales, aquellos que tiene una punto flotante

**Boolean** True o False, verdadero o falso

### Type Error, Type Checking and Type Conversion

*TypeError* es el cual nos indica que hay un error de tipo de dato en el codigo

Para prevenir errores de tipos de datos podemos hacer **Type Cheking** y verificar el tipo de dato con la funcion `type()` la cual nos indica que tipo de dato es, ademas podemos convertir los tipos de datos en otros haciendo "Type Casting", podemos convertir con los siguientes prefijos:

> str(var), int(var), float(var), boolean(var)

### Mathematical Operators

- `+` suma 3 + 5
- `-` resta 7 - 4
- `*` multiplicacion 3 * 2
- `/` division 6 / 3
- `**` elevado 2 ** 3
- `%` modulo 2 % 5

Recordar el orden de las operaciones matematicas, PEMDAS Parentesis, Exponentes, (Multiplicacion, Division), (Adicion y Sustraccion), Desde la izquierda a la derecha

### Number Manipulation and F Strings

Para redondondear un numero usamos la funcion `round()`

> Ex: `round(2.666666, 2)` = 2.67

Podemos Usar la *Floor Division* `//` divide y retorna el resultado en un numero en entero, pero truncado

Para manipular un numeros y operarlos basados en su valor anterior, podemos hacerlo mediante `+=`, `/=`, etc

**f-Strings**, para poder imprimir sin problemas varios tipos de de datos, en vez de convertirlos todos en string

En frente de las dobles comillas o simples comillas escibimos el caracter `f`, usamos `{}` para colocar nuestras variables y hacer que todos los datos se conviertan en String

> Ex: `print(f"La variable es:" {var})`

**Proyecto Dia 2:** Tip Calculator

## Day 3

### Control flow with if / else and Conditional Operators

conditional
**if / else**, dependiendo de una condicion en particular, hariamos A o B

```python
if condition:
    do this
else:
    do this
```

Comparison Operators

| Operador | Significado   |
| -------- | ------------- |
| >        | Mayor que     |
| <        | Menor que     |
| >=       | Mayor o igual |
| <=       | Menor o igual |
| ==       | Igualdad      |

> RECORDAR que `=` es para asignar y `==` para comparar igualdad

Operacion modulo, retorna el resto de una division inexacta

### Nested if statements and elif statements

Podemos anidar declaraciones if/else, para poner multiples condiciones

```python
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
```

En vez de tener un if/else con solo una condicion, podemos agregar tantas condiciones **elif** queramos

if / elif / else

```python
if condition1:
    do A
elif condition2:
    do B
else:
    do this
```

> Solo una de las condiciones se ejecutara A, B o C, Si la condicion A es cierta entonces haz A, si no es cierto comprueba la condicion 2, en caso de que sea verdadero hace B, si ninguna de las condiciones es verdadera, realiza el ultimo else

### Multiple If Statements in Succession

Para comprobar multiples condiciones, aun que la anterior sea cierta

Multiple if

```python
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C
```

> Se comprueban las tres condiciones y si las tres son verdaderas, A, B, y C se ejecutan
> Recordar tener cuidado con la identacion de las condicionales

### Logical Operators

Podemos aplicar multiples if/else, o sentencias if/else anidadas, Es posible combinar diferentes condiciones

| Operador | Significado       |
| -------- | ----------------- |
| and      | ambos verdad      |
| or       | una verdadera     |
| not      | invierte el valor |

```python
if condition1 & condition2 & condition3:
    do this
else:
    do this
```

- The `lower()` function changes all the letters in a string to lowercase. [link](https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python)
- The `count()` function will give you the number of times a letter occurs in a string. [link](https://stackoverflow.com/questions/1155617/scount-the-number-occurrences-of-a-character-in-a-string)

**Proyecto Dia 3:** Juego Isla del tesoro

## Day 4

### Random Module

Para generar numeros pseeudo aleatoreos

Importamos el modulo (libreria) random

```python
import random
```

`random(a, b)` retorna un numero aleatoreo, entre el rango de a y b incluyendolos, a no puede ser mayor a b

```python
random.randint(a, b)
```

**Modulo**, dividimos un codigo extenso en modulos, importamos los modulos para usar su funcionalidad

> Podemos crear nuestras propios modulos y de esa manera estructurar mejor el codigo.
> Para ello creamos el archivo .py y en nuestro codigo lo importamos mediante la palabra clave `import`, y para acceder, mediante `nombre.atributo`

`random()?? retorna un numero aleatoreo en el intervalo [0,1)

Multiplicando el numero aleatoreo por un numero n, podemos modificar el intervalo entre [0, n)

### Offset and Appending Items to List

**Listas**, estructura de datos, es una manera de organizar y almacenar los datos.

> No basta con almacenar datos en variables individuales, tambien podemos almacenar datos agrupados, que tienes algun tipo de conexion entre si.
> Podemos almacenar datos agrupados y ordenados segun nuestra preferencia

**Listas**, conjunto de corchetes con elementos en su interior, puedesn ser de cualquier tipo de dato, incluso tipos de datos mixtos, como strings, ints booleans

```python
list = [item1, item2]
fruits = ["Cherry", "Apple", "Pear"]
```

> Corechete de apertura y cierre, entre ellos, elementos separados por una coma
> Asigamos la lista a una variable

Podemos utilizar una lista para almacenar muchos datos relacionados, pero a su vez tienen un orden, el cual es otorgado mediante el orden en la lista

Al acceder a la lista, recordar que se inicia con el **0**

Accedemos mediante `lista[i]` siendo i el indice (contando desde 0) de la posicion que queremos consultar. (posemos consultar con i negativos, lo que haria partir desde la parte de atras)

`.append()` para agregar valores al final de la lista

`.extends()` para agregar un monton de valores al final de la lista

`.remove(x)` remover el primer item de la lista igual a "x"

[Documentacion Listas](https://docs.python.org/3/tutorial/datastructures.html)

> `.split()` nos permite dividir una cadena en componentes separados, basados en un separador
>
> `random.choice(list)` aleatoreamente elige un elemento de la lista

[Convertir String a Lista](https://www.askpython.com/python/string/convert-string-to-list-in-python)

### IndexErrors and Working with Nested Lists

`IndexError: list index out of range` al intentar acceder a un indice inexistente, fuera de limites

> Buen habito a hacer es tener una variable de logitud del arreglo y restar una posicion al momento de utilizarla

```python
num_length = len(array)
print(arr[num_length - 1])
```

Para tener una lista anidada a otra lista meidante una lista que contiene dos listas.

```python
nombre = ["joaquin", "ignacio"]
edad = [19, 20]

nombe_edad = [nombre, edad]
```

> Para navegar en una lista de listas, usamos un sistema de coordenadas `print[row][colum]`

- Primer digito especifica la **Fila** (posicion eje horizontal)
- Segundo digito especifica la **Columna** (posicion eje vertical)

> Poner observacion en el orden de las coordenadas, visualizar las coordenadas de listas de listas como [fila][columna], y revisar la entrada detalladamente

**Proyecto Dia 4:** Piedra, Papel, Tijera

## Day 5

### Using the for loop with Python Lists

Loops o bucles, son cosas que repiten una y otra vez, ejecuta la misma linea de codigo multiples veces

Podemos ejecutar un bloque de codigo multiples veces

For Loop, recorrer cada elemento de una lista y realizar alguna accion con cada uno de ellos individualmente, podemosrealizar multiples

```python
for item in list_of_items:
    #Do something to each item
```

> Toma la lista, y asigna la variable a cada uno de ellos

`sum(a)` a es la lista , suma todos los n??meros de la lista a y toma el inicio como 0, por lo que devuelve s??lo la suma de los n??meros de la lista.

`max()` devuelve el mayor elemento de un iterable o el mayor de dos o m??s argumentos. En el caso de cadenas, devuelve el valor lexicogr??ficamente mayor.

> Usar nombres consistentes y explicativos, que se refieran a forma singular de cada uno de los elementos o su funcionalidad

Recorriendo listas, los elementos de la lista y haciendo cosas con ella

Podemos ocupar for loops completamente independientes de las listas, usando For Loops con Rango

`range()` si queremos generar un rango de numeros para un bucle

```python
for number in range(a, b):
    print(number)
```

> En vez de recorrer una lista recorremos un rango, entre a y b, de esa manera accedemos a los numeros dentro de ese rango [a, b), no incuyendo el numero maximo
> Para incrementar por cualquier otro numero, agragamos otra coma al final del rango y especificamos el tamanio del incremento

`random.shuffle(list)` Para cambiar el orden de los elementos en una lista, retroana la lista desordenada

Solucion mas sencilla para desodenar una creacion de una string, agregar todos a una lista y desordenarla y volverla una string

**Proyecto Dia 5:** Generador de contrasenia

## Day 6

### Defining and Calling Python Functions

Funciones

A grandes rasgos, una funcion es un bloque de codigo que realiza una cierta operacion, se pueden definir parametros de entrada que permiten al llamar a la funcion ser pasados a esta, ademas podemos tambien devolver un valor como salida, podemos llamar a la funcion cuantas veces queramos.

La principal caracteristica de las funciones es la **encapsulacion** de operaciones en un solo bloque que puede ser **reutilizable**.

La funcion puede ser llamada o invocada desde cualquier lugar del programa. Los valores que se pasan a la funcion son los **parametros** o **argumentos**.

> Idealmente un buen diseno de una funciones tiene como objetivo que realizen una sola tarea bien definida. Los algoritmos complejos deben dividirse en funciones mas sencillas y faciles de comprender, idealmente con un nombre que describa claramente lo que hace la funcion

Su caracteristica visual mas comun es la utilizacion de parentesis `()` al final del nombre de la variable, lo que esta dentro de los parentesis son los **parametros** de la funcion.

```python
# Definir una Funcion
def my_function():
    # Do this
    # Then do this
    # Finally do this

# Llamar una funcion
my_function()
```

> **Definimos la funcion**, con la Palabra clave `def` seguido del nombre que diferenciara a la funcion, luego entre parentesis las variables, para finalizar en dos puntos `:` que indicaran que todo lo que este despues de esta linea (indentado correctamente) pertenecera a la funcion.

Para llamar a una funcion escribimos el nombre de la funcion, seguido de los parentesis y la entrada necesaria.

[Funciones incorporadas](https://docs.python.org/3/library/functions.htmlhttps://docs.python.org/3/library/functions.html)

### Indentation in Python

Indentacion define la jerarquia de bloques, cada sangria se define como 4 espacios, se podria ver la estructura de indentacion como la estructura de carpetas en el explorador, cada carpeta tiene sub carpetas indentadas en un subnivel

`ctrl + [` o `ctrl + ]` para indentar un bloque de codigo

### While Loops

Bucle While que se ejecuta repetidas veces mientras la condicion sea cierta
Mientras la condicion es verdadera entonces vamos dentro del bucle y repetimos, y solamente cuando se convierte en falso el bucle se detiene

```python
# For
for item in list_of_items:
    # Do something to each item
for number in range(a,b)
    print(number)

# While
while something_true:
    #Do something repeatedly
```

> Para hacer un loop mientras no estemos en una parte podemos definirlo como `while at_goal() != True:` o mas comodamente `while not at_goal():`

Los bulces while son mas peligrosos que los bucles for, ya que en los bulces for establecemos la cantidad de iteraciones y se detendra cuando llegue al final, pero en los bucles whiles ejecutaremos hasta que esta condicion particular cambie a false.

Infinite loops, el codigo se ejecutara infinitamente