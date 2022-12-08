# 100 Days Of Code

Start day: December 4, 2022

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

`random()´ retorna un numero aleatoreo en el intervalo [0,1)