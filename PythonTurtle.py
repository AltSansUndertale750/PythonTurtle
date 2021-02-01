import turtle 
import random
wn=turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.ht()
t.tracer(0,0)
rainbow_colors = ["red", "orange", "green", "blue", "purple", "cyan", "lime", "pink", "white", "silver"]

for sides in range(1332):
  t.left(10)
  t.forward(10)
  if sides % 36 == 0:
    t.pencolor(random.choice(rainbow_colors))
  if sides % 36 == 0:
    t.right(10)
  if sides % 4 == 0:
    t.update()
t.penup()
t.goto(325, 150)
t.pendown()
for sides in range(200):
  t.left(200)
  t.forward(200)
  if sides % 4 == 0:
    t.pencolor(random.choice(rainbow_colors))
  if sides % 4 == 0:
    t.right(10)
  if sides % 1 == 0:
     t.update()
