import turtle
t= turtle.Turtle()
t.hideturtle()
def drawRect(x, y, w, h):
    t.up()
    t.fillcolor('black')
    t.begin_fill()
    t.goto(x, y)
    t.down()
    t.goto(x+w, y)
    t.goto(x+w, y+h)
    t.goto(x, y+h)
    t.goto(0, 0)
    t.end_fill()    

drawRect(0, 0, 150, 250)
    
