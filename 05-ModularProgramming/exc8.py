import turtle

pen = turtle.Turtle()


def drawSquare(x, y, n):
    pen.setposition(x, y)
    for i in range(4):
        pen.forward(n)
        pen.right(90)
    turtle.done()


for i in range(2):
    drawSquare(0, 0, 50)
    pen.setposition(50, 50)