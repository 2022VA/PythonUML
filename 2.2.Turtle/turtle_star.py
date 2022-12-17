import sys
import turtle

def draw(turtle:turtle, n):
    for i in range (n):
        turtle.forward(100)
        turn = 180 - 180.0/n
        turtle.right(turn)
        turtle.forward(100)

if len(sys.argv) > 1:  # pārbauda komandrindas argumentus, kur sagaida nepāra skaitli cik stari jāzīmē
    points = int(sys.argv[1])
    if (points % 2) == 0 or (points < 0):
        print ('Skaitlim jābūt nepāra un pozitīvam')
    else:
        zimul = turtle.Turtle()
        draw(zimul, points)
        turtle.exitonclick() # gaida pēc zīmēšanas, kamēr nospiež peli
else:
    print ('Pievienojiet komandai nepāra skaitli kā argumentu, lai zīmētu n-staru zvaigzni, piem "python turtle_star.py 7"')
