import turtle
turtle.shape('turtle')
turtle.speed(0)


def draw_square(n):
    for x in range(4):
        turtle.forward(n)
        turtle.left(90)


n = 10
x = -5
y = -5
for x in range(10):
    draw_square(n)
    n += 10
    turtle.penup()
    for x in range(2):
        turtle.right(90)
        turtle.forward(5)
    turtle.right(180)
    x -= 5
    y -= 5
    turtle.pendown()

turtle.exitonclick()
