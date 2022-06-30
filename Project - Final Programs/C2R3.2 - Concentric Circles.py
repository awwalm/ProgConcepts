import turtle
t= turtle.Turtle()
t.hideturtle()

def drawCircle(t, x, y, diameter, colorP):
    t.up()
    t.goto(x, y)
    t.pencolor(colorP)
    t.dot(diameter)

drawCircle(t, 0, 0, 200, 'black')
drawCircle(t, 0, 125, 50, 'black')
