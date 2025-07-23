import turtle
turtle.shape('turtle')
turtle.speed(0)


def circle(k):
    n = 20
    angle = 180 - (180 * (n - 2)) / n

    for x in range(n):
        turtle.forward(k)
        turtle.left(angle)


k = 5
p = 0

for x in range(10):
    circle(k)
    p += 1
    k = -k
    if p == 2:
        p = 0
        k += 2


turtle.exitonclick()
