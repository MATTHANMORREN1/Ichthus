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

# Loop door de lijst met commando's en voer elk commando uit
for commando in commando_lijst:
    uitvoeren(commando)

# Sluit het tekenvenster niet onmiddellijk
turtle.mainloop()
