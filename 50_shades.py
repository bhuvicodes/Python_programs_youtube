import turtle
turtle.color("black", "grey45")
turtle.colormode(1.0)
squares = 50
side = 100
shade = 1.0
for count in range(squares):
    turtle.fillcolor(shade,shade,shade)
    turtle.begin_fill()
    turtle.left(360 // squares)
    for x in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()
    shade -= turtle.colormode() / float(squares)
turtle.done()