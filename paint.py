"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import * # Se importa la libreria turtle

from freegames import vector


def line(start, end): # Funcion para crear una linea
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end): # Funcion crea un cuadrado
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def tcircle(start, end): # Funcion crea un circulo
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()

    begin_fill()
    circle(end.x - start.x)
    end_fill()


def rectangle(start, end): # Funcion crea un rectangulo
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x + start.x)
        left(90)
        forward(end.x - start.x)
        left(90)

    end_fill()


def triangle(start, end): # Funcion crea un triangulo
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y): # Registra la posicion del click
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value): # Guarda datos
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0) # Crea el canvas
onscreenclick(tap) # Pone la funcion tap cuando se hace click
listen() # Se prepara para recibir input de teclas
onkey(undo, 'u') # Regresa el cambio

# Colores
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')
# Figuras
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', tcircle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
