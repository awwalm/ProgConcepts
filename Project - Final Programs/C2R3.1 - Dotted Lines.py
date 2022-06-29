import turtle
t= turtle.Turtle()
t.hideturtle()

linelength= 200
def drawLine(t, x, y, linelength):
    t.up()
    t.goto(x, y)
    t.left(45)
    t.down()
    t.forward(linelength)

drawLine(t, 0, 0, linelength)    

def drawCircle(t, x, y, diameter, colorP):
    t.up()
    t.goto(x, y)
    t.pencolor(colorP)
    t.dot(diameter)

drawCircle(t, 0, 0, 10, 'black')
drawCircle(t, 141.42, 139.5, 10, 'black')
