
def main():
    import turtle
    t = turtle.Turtle()
    t.hideturtle()
    drawRectangle(t, 0, 0, 100, 150, 'red', 'yellow')

def drawRectangle(t, x, y, w, h, colorP='black', colorF='white'):
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
    t.goto(x, y)
    t.end_fill()

main()
