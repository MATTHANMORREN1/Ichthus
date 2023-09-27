import turtle

# Functie om een enkel commando uit te voeren
def uitvoeren(commando):
    if commando[0] == 'u':
        turtle.up()
    elif commando[0] == 'd':
        turtle.down()
    elif commando[0] == 'f':
        afstand = float(commando[1:])
        turtle.forward(afstand)
    elif commando[0] == 'b':
        afstand = float(commando[1:])
        turtle.backward(afstand)
    elif commando[0] == 'l':
        hoek = float(commando[1:])
        turtle.left(hoek)
    elif commando[0] == 'r':
        hoek = float(commando[1:])
        turtle.right(hoek)
    elif commando[0] == 'c':
        gegevens = commando[1:].split(',')
        straal = float(gegevens[0])
        graden = float(gegevens[1])
        turtle.circle(straal, graden)
    elif commando[0] == 'p':
        kleur = commando[1:]
        turtle.pencolor(kleur)
    elif commando[0] == 'i':
        kleur = commando[1:]
        turtle.fillcolor(kleur)
    elif commando[0] == 's':
        turtle.begin_fill()
    elif commando[0] == 'e':
        turtle.end_fill()
    elif commando[0] == 'g':
        gegevens = commando[1:].split(',')
        x = float(gegevens[0])
        y = float(gegevens[1])
        turtle.goto(x, y)

# Initialisatie van de schildpad
t = turtle.Turtle()
t.speed(10)  # Stel de tekeningsnelheid in

# Lijst met commando's om de tekening te maken
commando_lijst = [
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
    "c100,20",
    "l180",
    "c-100,20",
    "l-300.0",
    "c10,50",
    "l60.0",
    "c100,20",
    "l180",
    "c-100,20",
    "l-260.0",
    "c20,50",
    "l20.0",
    "c100,40",
    "l60.0",
    "c-100,5
