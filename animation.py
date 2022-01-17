import turtle
wn = turtle.Screen()
wn.setup(400,600)
wn.bgcolor("black")
s = turtle.Turtle()

for i in range(4):
    s.begin_fill()
    s.forward(100)
    s.left(90)
    s.pencolor("dark orange")
    s.forward(100)
    s.fillcolor("dark orange")
    s.end_fill()

for i in range(4):
    s.begin_fill()
    s.forward(80)
    s.left(90)
    s.pencolor("white")
    s.forward(80)
    s.fillcolor("white")
    s.end_fill()

for i in range(4):
    s.begin_fill()
    s.forward(60)
    s.left(90)
    s.pencolor("green")
    s.forward(60)
    s.fillcolor("green")
    s.end_fill()

'''for i in range(4):
   s.begin_fill()
    s.forward(40)
    s.left(90)
    s.pencolor('brown')
    s.forward(40)
    s.fillcolor("brown")
    s.end_fill()

for i in range(4):
    s.begin_fill()
    s.forward(20)
    s.left(90)
    s.pencolor("black")
    s.forward(20)
    s.fillcolor("black")
    s.end_fill()'''

turtle.done()