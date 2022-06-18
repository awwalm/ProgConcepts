import turtle
def main():
    import turtle
    t = turtle.Turtle()
    t.hideturtle()
    drawFilledRectangle(t, 0, 0, 150, 25, 'light blue', 'light blue')
    drawFilledRectangle(t, 0, 25, 150, 50, 'blue', 'blue')
    drawFilledRectangle(t, 0, 75, 150, 25, 'light blue', 'light blue')

    drawDot(t, 75, 50, 40, 'white')

def drawFilledRectangle(t, x, y, w, h, colorP='black', colorF='white'):
    import turtle
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.goto(x + w, y)
    t.goto(x + w, y + h)
    t.goto(x, y + h)
    t.begin_fill()
    t.goto(x + w, y)
    t.goto(x + w, y + h)
    t.goto(x, y + h)
    t.goto(x, y)
    t.end_fill()

def drawDot(t, x, y, diameter, colorP):
    import turtle
    t.up()
    t.goto(x, y)
    t.pencolor(colorP)
    t.dot(diameter)

main()
