import turtle
turtle.shape('turtle')
turtle.speed(1)

n = 8
angle = 360 / n
p = 50

for x in range(n):
    turtle.forward(p)
    turtle.stamp()
    turtle.backward(p)
    turtle.left(angle)

turtle.exitonclick()
