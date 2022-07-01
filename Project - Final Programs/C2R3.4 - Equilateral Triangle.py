import turtle
t= turtle.Turtle()
t.hideturtle()

def eqTri(x, y):
    t.up()
    t.goto(x, y)
    t.left(120)
    t.down()
    for angle in range(3):
        t.forward(200)
        t.left(120)
    input()

eqTri(0,0)
