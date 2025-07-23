import turtle
turtle.shape('turtle')
turtle.speed(0)


def circle():
    n = 40
    angle = 180 - (180 * (n - 2)) / n

    for x in range(n):
        turtle.forward(10)
        turtle.left(angle)
    turtle.right(150)


for x in range(10):
    circle()


turtle.exitonclick()
