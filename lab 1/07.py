import turtle
import math
turtle.shape('turtle')
turtle.speed(0)

a = 5
phi = 16 * math.pi
step = 0.1
angle = 0
turtle.speed(0)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

while angle <= phi:
    r = a * angle
    x = r * math.cos(angle)  # полярные координаты абсциссы
    y = r * math.sin(angle)  # полярные координаты ординаты
    turtle.goto(x, y)
    angle += step

turtle.exitonclick()
