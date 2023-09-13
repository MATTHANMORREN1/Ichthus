import tkinter as tk
import turtle

def forward():
    distance = int(forward_entry.get())
    t.forward(distance)

def backward():
    distance = int(backward_entry.get())
    t.backward(distance)

def left():
    angle = int(left_entry.get())
    t.left(angle)

def right():
    angle = int(right_entry.get())
    t.right(angle)

def pen_up():
    t.penup()

def pen_down():
    t.pendown()

def goto():
    x = int(x_entry.get())
    y = int(y_entry.get())
    t.goto(x, y)

def reset():
    t.reset()

def change_pen_color():
    color = pen_color_entry.get()
    t.pencolor(color)

def change_fill_color():
    color = fill_color_entry.get()
    t.fillcolor(color)

def draw_circle():
    radius = int(circle_radius_entry.get())
    t.circle(radius)

def draw_polygon(sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(100)
        t.right(angle)

root = tk.Tk()
root.title("Turtle in Tkinter")
root.geometry("1000x700")

canvas = tk.Canvas(root)
canvas.place(x=0, y=0, width=1000, height=1000)

screen = turtle.ScrolledCanvas(canvas)
screen.place(x=0, y=0, width=1000, height=700)

t = turtle.RawTurtle(screen._canvas)


forward_label = tk.Label(root, text="Forward:")
forward_label.place(x=10, y=520)
forward_entry = tk.Entry(root)
forward_entry.place(x=80, y=520)
forward_button = tk.Button(root, text="Forward", command=forward)
forward_button.place(x=200, y=515)

backward_label = tk.Label(root, text="Backward:")
backward_label.place(x=10, y=550)
backward_entry = tk.Entry(root)
backward_entry.place(x=80, y=550)
backward_button = tk.Button(root, text="Backward", command=backward)
backward_button.place(x=200, y=545)

left_label = tk.Label(root, text="Left:")
left_label.place(x=300, y=520)
left_entry = tk.Entry(root)
left_entry.place(x=350, y=520)
left_button = tk.Button(root, text="Left", command=left)
left_button.place(x=470, y=515)

right_label = tk.Label(root, text="Right:")
right_label.place(x=300, y=550)
right_entry = tk.Entry(root)
right_entry.place(x=350, y=550)
right_button = tk.Button(root, text="Right", command=right)
right_button.place(x=470, y=545)


pen_up_button = tk.Button(root, text="Pen Up", command=pen_up)
pen_up_button.place(x=600, y=520)
pen_down_button = tk.Button(root, text="Pen Down", command=pen_down)
pen_down_button.place(x=700, y=520)


x_label = tk.Label(root, text="X:")
x_label.place(x=600, y=550)
x_entry = tk.Entry(root)
x_entry.place(x=620, y=550)
y_label = tk.Label(root, text="Y:")
y_label.place(x=660, y=550)
y_entry = tk.Entry(root)
y_entry.place(x=680, y=550)
goto_button = tk.Button(root, text="Go To", command=goto)
goto_button.place(x=720, y=545)


reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.place(x=10, y=590)


pen_color_label = tk.Label(root, text="Pen Color:")
pen_color_label.place(x=150, y=590)
pen_color_entry = tk.Entry(root)
pen_color_entry.place(x=230, y=590)
pen_color_button = tk.Button(root, text="Change Pen Color", command=change_pen_color)
pen_color_button.place(x=350, y=585)


fill_color_label = tk.Label(root, text="Fill Color:")
fill_color_label.place(x=500, y=590)
fill_color_entry = tk.Entry(root)
fill_color_entry.place(x=580, y=590)
fill_color_button = tk.Button(root, text="Change Fill Color", command=change_fill_color)
fill_color_button.place(x=700, y=585)


circle_radius_label = tk.Label(root, text="Circle Radius:")
circle_radius_label.place(x=10, y=625)
circle_radius_entry = tk.Entry(root)
circle_radius_entry.place(x=100, y=625)
draw_circle_button = tk.Button(root, text="Draw Circle", command=draw_circle)
draw_circle_button.place(x=230, y=620)


polygon_label = tk.Label(root, text="Polygon Sides:")
polygon_label.place(x=350, y=625)
polygon_entry = tk.Entry(root)
polygon_entry.place(x=450, y=625)

draw_triangle_button = tk.Button(root, text="Draw Triangle", command=lambda: draw_polygon(3))
draw_triangle_button.place(x=580, y=620)

draw_square_button = tk.Button(root, text="Draw Square", command=lambda: draw_polygon(4))
draw_square_button.place(x=680, y=620)

root.mainloop()
