# modulo tortuga
import turtle
import random

random2 = random.randrange(0, 360, 50)
random1 = random.randrange(0, 360, 50)

print(random2)
print(random1)


def langton():
    try:
        # Pantalla de juego
        window = turtle.Screen()
        window.bgcolor("white")
        window.screensize(1000, 1000)

        # color y coordenadas
        maps = {}

        # creando la hormiga
        ant = turtle.Turtle()

        # forma de la hormiga
        ant.shape("circle")

        # tamaño de la hormiga
        ant.shapesize(0.5)

        # Velocidad de la hormiga
        ant.speed(1)

        # le damos las coordenadas a la hormiga
        pos = coordinate(ant)

        # Controlar Turtle con el teclado
        def h1():
            window.bye()

        def h2():
            ant.speed(0)

        def h3():
            ant.speed(1)

        window.onkey(h1, "q")
        window.onkey(h2, "0")
        window.onkey(h3, "1")

        window.listen()
        while True:

            # la distancia en la que la hormiga se va a mover
            step = 10
            if pos not in maps or maps[pos] == "white":

                # agregar color
                ant.fillcolor("black")

                # copia de las casillas en el lienzo
                ant.stamp()
                invert(maps, ant, "black")
                ant.right(random2)

                # le damos un color a la hormiga
                ant.fillcolor("red")

                # hace lo contrario
                ant.forward(step)
                pos = coordinate(ant)

            elif maps[pos] == "black":
                ant.fillcolor("white")
                invert(maps, ant, "white")

                ant.stamp()
                ant.left(random1)
                ant.forward(step)
                pos = coordinate(ant)

                # color de la hormiga?
                ant.fillcolor("red")



    except:
        print(f"{random2}, {random1}")


def invert(graph, ant, color):
    graph[coordinate(ant)] = color


def coordinate(ant):
    return round(ant.xcor()), round(ant.ycor())


langton()