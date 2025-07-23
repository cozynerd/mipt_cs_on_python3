import turtle
import math


def cool(n, k):
    R = k / (2 * math.sin(math.pi / n))

    turtle.penup()
    turtle.goto(R, 0)
    turtle.pendown()

    turtle.setheading(90 + 180/n)

    angle = 360 / n
    for _ in range(n):
        turtle.forward(k)
        turtle.left(angle)


turtle.speed(5)
turtle.shape('turtle')

k = 30
n = 3

for i in range(10):
    cool(n, k)
    n += 1
    k += 10

turtle.exitonclick()
