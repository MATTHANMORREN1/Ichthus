import turtle



file = open("tekening.txt", "r")

regels = file.readlines()

file.close()

t = turtle.Turtle()

t.speed(10000)

for regel in regels:

    argument = regel[1:].strip("\n")

    match regel[0]:

        case "i":

            t.fillcolor(argument)

        case "s":

            t.begin_fill()

        case "p":

            t.pencolor(argument)

        case "e":

            t.end_fill()

        case "c":

            (rad, deg) = argument.split(",")

            t.circle(float(rad), float(deg))

        case "d":

            t.down()

        case "u":

            t.up()

        case "o":

            t.dot()

        case "b":

            t.back(float(argument))

        case "f":

            t.forward(float(argument))

        case "r":

            t.right(float(argument))

        case "g":

            (x, y) = argument.split(",")

            t.goto(float(x), float(y))

        case "l":

            t.left(float(argument))



turtle.mainloop()