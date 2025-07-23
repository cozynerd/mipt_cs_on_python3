import turtle
turtle.speed(0)
turtle.shape('turtle')
k = 10
for x in range(50):
    turtle.forward(k)
    turtle.left(90)
    k += 5

turtle.exitonclick()
