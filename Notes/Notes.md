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

Primitive Data types:

- String
- Integer
- Float
- Boolean

**String** delimitado por `''` o `""`, mediante subscripting, el numero entre `[]` determina el caracter que vamos a extraer, empezando desde 0

**Integer** numeros positivos o negativos sin decimales, pueden estar separados por `_`, solo para uso visual

**Float** numeros decimales, aquellos que tiene una punto flotante

**Boolean** True o False, verdadero o falso

*TypeError* es el cual nos indica que hay un error de tipo de dato en el codigo

Para prevenir errores de tipos de datos podemos hacer **Type Cheking** y verificar el tipo de dato con la funcion `type()` la cual nos indica que tipo de dato es, ademas podemos convertir los tipos de datos en otros haciendo "Type Casting", podemos convertir con los siguientes prefijos:

> str(var), int(var), float(var), boolean(var)

**Mathematical Operators**

- `+` suma 3 + 5
- `-` resta 7 - 4
- `*` multiplicacion 3 * 2
- `/` division 6 / 3
- `**` elevado 2 ** 3
- `%` resto 2 % 5

Recordar el orden de las operaciones matematicas, PEMDAS Parentesis, Exponentes, (Multiplicacion, Division), (Adicion y Sustraccion), Desde la izquierda a la derecha

**Number Manipulation and F Strings**

Para redondondear un numero usamos la funcion `round()`

> Ex: `round(2.666666, 2)` = 2.67

Podemos Usar la *Floor Division* `//` divide y retorna el resultado en un numero en entero, pero truncado

Para manipular un numeros y operarlos basados en su valor anterior, podemos hacerlo mediante `+=`, `/=`, etc

**f-Strings**, para poder imprimir sin problemas varios tipos de de datos, en vez de convertirlos todos en string

En frente de las dobles comillas o simples comillas escibimos el caracter `f`, usamos `{}` para colocar nuestras variables y hacer que todos los datos se conviertan en String

> Ex: `print(f"La variable es:" {var})`

**Proyecto Dia 2: Tip Calculator**
