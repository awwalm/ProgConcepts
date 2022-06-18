import turtle

heights = [856, 420, 360, 260, 205]

def main():
    t = turtle.Turtle()
    t.hideturtle()
    for i in range(5):
        drawRectangle(t, -200 + (76 * i), 0, 76, heights[i]/4, 'black', 'light blue')
    displayText(t)

def drawRectangle(t, x, y, w, h, colorP='black', colorP='black', colorF='white'):
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

def displayText(t):
    
