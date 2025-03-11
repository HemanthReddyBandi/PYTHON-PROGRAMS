import turtle

w = turtle.Screen()
w.bgcolor('black')

t = turtle.Turtle()
t.pencolor('white')


def curve():
    for i in range(100):
        t.right(1)
        t.forward(1)

def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.left(140)
    t.forward(224)
    curve()
    t.left(120)
    curve()
    t.forward(224)
    t.end_fill()

heart()
t.hideturtle()
w.mainloop()
