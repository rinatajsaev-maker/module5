#Author:Rinat.R
#Date:10.26.25
"""This program draws a simple pattern with turtle"""
import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red","orange","yellow","green","blue","purple"]

for i in range(36):
    t.color(colors[i % 6])
    t.circle(50)
    t.left(10)

turtle.done()