import turtle

def uitvoeren(commando, turtle):
    commando_type = commando[0]
    argument = commando[1:].strip()
    
    match commando_type:
        case 'u':
            turtle.up()
        case 'd':
            turtle.down()
        case 'f':
            turtle.forward(float(argument))
        case 'b':
            turtle.backward(float(argument))
        case 'l':
            turtle.left(float(argument))
        case 'r':
            turtle.right(float(argument))
        case 'i':
            turtle.fillcolor(argument)
        case 's':
            turtle.begin_fill()
        case 'e':
            turtle.end_fill()
        case 'p':
            turtle.pencolor(argument)
        case 'c':
            args = argument.split(',')
            radius = float(args[0])
            extent = float(args[1])
            turtle.circle(radius, extent)
        case 'g':
            args = argument.split(',')
            x = float(args[0])
            y = float(args[1])
            turtle.goto(x, y)
        case _:
            print(f"Ongeldig commando: {commando}")

t = turtle.Turtle()

# Met dank aan CHATGPT voor het plaatsen van aanhalingstekens en komma's in deze commandos
commandos = [
    "u",
    "l90",
    "f200",
    "d",
    "r90",
    "ipink",
    "s",
    "c10,180",
    "c25,110",
    "l50",
    "c60,45",
    "c20,170",
    "r24",
    "f30",
    "l10",
    "c30,110",
    "f20",
    "l40",
    "c90,70",
    "c30,150",
    "r30",
    "f15",
    "c80,90",
    "l15",
    "f45",
    "r165",
    "f20",
    "l155",
    "c150,80",
    "l50",
    "c150,90",
    "e",
    "l150",
    "c-90,70",
    "l20",
    "c75,105",
    "l-261.0",
    "c80,98",
    "c-90,40",
    "l180",
    "c90,40",
    "c-80,98",
    "l-323.0",
    "f30",
    "l90",
    "f25",
    "l45",
    "igreen",
    "s",
    "c-80,90",
    "r90",
    "c-80,90",
    "e",
    "r135",
    "f60",
    "l180",
    "f85",
    "l90",
    "f80",
    "r90",
    "r45",
    "igreen",
    "s",
    "c80,90",
    "l90",
    "c80,90",
    "e",
    "l135",
    "f60",
    "l180",
    "f60",
    "r90",
    "c200,60"
]

for cmd in commandos:
    uitvoeren(cmd, t)

turtle.mainloop()
