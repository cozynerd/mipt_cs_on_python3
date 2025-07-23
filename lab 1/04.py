import turtle
turtle.shape('turtle')
turtle.speed(0)

n = 50
angle = 180 - (180 * (n - 2)) / n

for x in range(n):
    turtle.forward(10)
    turtle.left(angle)

turtle.exitonclick()
