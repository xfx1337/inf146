from turtle import *
screensize(1000, 1000)

tracer(0)
down()
left(90)
k = 25
for i in range(8):
    for j in range(4):
        forward(5 * k)
        right(30)
        forward(6 * k)
        right(150)
    right(60)

up()
for i in range(-25, 25):
    for j in range(-25, 25):
        goto(i*k, j*k)
        dot(3, 'red')


exitonclick()