# from turtle import * - импорт черепахи
#fd(x) вперёд
#bk(x) назад
#lt(x) влево
#rt(x) вправо

#forward(x) вперёд
#backward(x) назад
#left(x) влево
#right(x) вправо
#значения в пикселях и в градусах

#up и down  поднять и опустить хвост
# goto(x,y) - перейти в точку
# dot(pixels, color) - поставить точку

# tracer(0) отключение анимации
# update - обновить картинку
# screensize(5000,5000) поменять размер окна

#отрисовка целочисленных точек(сетка)

r = 10 # масштаб. что бы было что то видно. все движения, кроме поворотов, нужно умножать на r

from turtle import *

screensize(5000,5000)
tracer(0)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*r, y*r)
        dot(3, 'red') # 3 - диаметр в пикселях, 'red' - цвет
goto(0,0)
down()
for i in range(2):
    fd(5*r)
    rt(90)
    fd(11*r)
    rt(90)
up()
fd(-4*r)
rt(90)
fd(6*r)
lt(90)
down()
for i in range(2):
    fd(42*r)
    rt(90)
    fd(63*r)
    rt(90)

update()
mainloop()