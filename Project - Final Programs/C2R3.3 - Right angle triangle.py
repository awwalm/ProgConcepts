import turtle
t= turtle.Turtle()
t.hideturtle()

hyp= 200
opp= 141
adj= 139.5
def drawTriangle(t, x, y, hyp, opp, adj):
    t.up()
    t.goto(x, y)
    t.right(45)
    t.down()
    t.forward(hyp)
    t.down()
    t.right(135)
    t.forward(opp)
    t.goto(x, y)
    t.goto(x, y-adj)

drawTriangle(t, 0, 0, hyp, opp, adj)
