from turtle import Turtle, Screen

the_turtle = Turtle()
the_screen = Screen()

the_turtle.shape("turtle")
the_turtle.color("green")

def forward_right():
    the_turtle.forward(150)
    the_turtle.right(90)
    the_turtle.forward(150)

def turn_right():
    the_turtle.right(90)

def create_square():
    forward_right()
    turn_right()
    forward_right()
    the_turtle.right(90)
the_turtle.pensize(1)

def pen_forward():
    the_turtle.down()
    the_turtle.forward(10)

def pen_up_forward():
    the_turtle.up()
    the_turtle.forward(10)

def create_triangle():
    the_turtle.forward(150)
    the_turtle.right(120)
    the_turtle.forward(150)
    the_turtle.right(120)
    the_turtle.forward(150)
    the_turtle.right(120)

def create_pentagon():
    the_turtle.forward(150)
    the_turtle.right(72)
    the_turtle.forward(150)
    the_turtle.right(72)
    the_turtle.forward(150)
    the_turtle.right(72)
    the_turtle.forward(150)
    the_turtle.right(72)
    the_turtle.forward(150)
    the_turtle.right(72)

def create_hexagon():
    the_turtle.forward(150)
    the_turtle.right(60)
    the_turtle.forward(150)
    the_turtle.right(60)
    the_turtle.forward(150)
    the_turtle.right(60)
    the_turtle.forward(150)
    the_turtle.right(60)
    the_turtle.forward(150)
    the_turtle.right(60)
    the_turtle.forward(150)
    the_turtle.right(60)

def create_septagon():
    the_turtle.forward(150)
    the_turtle.right(51)
    the_turtle.forward(150)
    the_turtle.right(51)
    the_turtle.forward(150)
    the_turtle.right(51)
    the_turtle.forward(150)
    the_turtle.right(51)
    the_turtle.forward(150)
    the_turtle.right(51)
    the_turtle.forward(150)
    the_turtle.right(51)
    the_turtle.forward(150)
    the_turtle.right(51)

def create_octagon():
    the_turtle.forward(150)
    the_turtle.right(45)
    the_turtle.forward(150)
    the_turtle.right(45)
    the_turtle.forward(150)
    the_turtle.right(45)
    the_turtle.forward(150)
    the_turtle.right(45)
    the_turtle.forward(150)
    the_turtle.right(45)
    the_turtle.forward(150)
    the_turtle.right(45)
    the_turtle.forward(150)
    the_turtle.right(45)
    the_turtle.forward(150)
    the_turtle.right(45)

create_square()
create_triangle()
create_pentagon()
create_hexagon()
create_septagon()
create_octagon()

the_screen.exitonclick()
