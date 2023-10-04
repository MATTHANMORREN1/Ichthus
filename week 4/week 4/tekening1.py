import turtle as t


def draw_circle(radius, angle):
    t.circle(radius, angle)


def draw_line(length):
    t.forward(length)


def draw_dot(radius, color):
    t.penup()
    t.dot(radius, color)
    t.pendown()

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


t.speed(1)
t.bgcolor("white")


pink = "pink"
green = "green"


t.penup()
t.color(pink)
t.pendown()

t.up()
t.left(90)
t.fd(200)
t.down()
t.right(90)

draw_circle(10, 180)
draw_circle(25, 110)
t.left(50)
draw_circle(60, 45)
draw_circle(20, 170)
t.right(24)
draw_line(30)
t.left(10)
draw_circle(30, 110)
draw_line(20)
t.left(40)
draw_circle(90, 70)
draw_circle(30, 150)
t.right(30)
draw_line(15)
draw_circle(80, 90)
t.left(15)
draw_line(45)
t.right(165)
draw_line(20)
t.left(155)
draw_circle(150, 80)
t.left(50)
draw_circle(150, 90)
t.penup()
move_to(0, 0)
t.pendown()




t.penup()
t.color(green)
t.pendown()


draw_circle(-80, 90)
t.right(90)
draw_circle(-80, 90)
t.penup()
move_to(0, 0)
t.pendown()


t.right(135)
draw_line(60)
t.left(180)
draw_line(85)
t.right(90)
draw_line(80)
t.right(90)
t.right(45)


t.penup()
t.color(green)
t.pendown()


draw_circle(80, 90)
t.left(90)
draw_circle(80, 90)
t.penup()
move_to(0, 0)
t.pendown()


t.left(135)
draw_line(60)
t.left(180)
draw_line(60)
t.right(90)
draw_line(200)


t.exitonclick()
