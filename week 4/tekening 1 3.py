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
"i#F6D02F",
"s",
"u",
"c130,40",
"d",
"c100,105",
"l180",
"c-100,5",
"l-300.0",
"c300,30",
"c30,50",
"l90.0",
"c300,36",
"l-76.0",
"c150,70",
"l-20.0",
"c300,40",
"c30,50",
"l-270.0",
"c300,35",
"l185.0",
"c105,95",
"l180",
"c-105,5",
"l60.0",
"c500,18",
"l-28.0",
"f10",
"l80.0",
"f7",
"l-70.0",
"f10",
"l90.0",
"c10,80",
"l200.0",
"f10",
"l80.0",
"c10,80",
"l220.0",
"f12",
"l-240.0",
"f13",
"l240.0",
"c10,70",
"l-300.0",
"c10,70",
"l-70.0",
"c300,18",
"l47.0",
"c500,8",
"l180",
"c-500,15",
"l2.0",
"c100,65",
"l5.0",
"c100,5",
"l180",
"c-100,5",
"l80.0",
"c200,20",
"c20,70",
"l-250.0",
"c-100,20",
"l180",
"c100,20",
"l60.0",
"c10,70",
"l50.0",
"c-100,20",
"l180",
"c100,20",
"l-230.0",
"c100,60",
"l110.0",
"c-100,10",
"l180",
"c100,10",
"l5.0",
"c100,10",
"c-100,40",
"c100,35",
"l180",
"c-100,10",
"l110.0",
"c100,55",
"c10,50",
"l85.0",
]

for cmd in commandos:
    uitvoeren(cmd, t)

turtle.mainloop()