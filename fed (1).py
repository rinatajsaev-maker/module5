#Author:Rinat.R
#Date:10.26.25
"""This program draws a polygon based on user input"""

import turtle

sides = int(input("Number of sides? "))
side_len = int(input("Length? "))
line_col = input("Line color? ")
fill_col = input("Fill color? ")

t = turtle.Turtle()
t.color(line_col, fill_col)

angle = 360 / sides

t.begin_fill()
for i in range(sides):
    t.forward(side_len)
    t.left(angle)
t.end_fill()

turtle.done()