# -*- coding:UTF-8 -*-
__author__ = "zhangguodong"
__time__ = "2017.11.16"
 
import turtle
 
turtle.title("张国栋画五角星")
turtle.setup(500,300,0,0)
turtle.fillcolor("red")
turtle.begin_fill()
 
while True:
    turtle.forward(220)
    turtle.right(144)
    if abs(turtle.pos()) < 1:
            break
 
turtle.end_fill()
turtle.done()

