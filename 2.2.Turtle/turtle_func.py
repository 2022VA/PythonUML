import sys
import turtle

def draw(turtle:turtle, x, sakx, saky):
    for i in range (x):
        turtle.goto(sakx + x, saky + int(x/2)+5)

if len(sys.argv) > 1:  # pārbauda komandrindas argumentus, kur sagaida x vērtību
    points = int(sys.argv[1])
    if (points < 150):
        print ('Skaitlim jābūt lielākam vai vienādam ar 150')
    else:
        # uzliek ekrāna izmērus atkarībā no saņemtā x
        ekrans = turtle.Screen()
        ekrans.setup((points + 50), (int(points/2) + 50))
        zimul = turtle.Turtle()
        # aprēķina kreiso apakšējo stūri, un pāriet uz to nezīmējot
        sakx = -int(ekrans.window_width()/2) + 25
        saky = -int(ekrans.window_height()/2) + 25
        zimul.penup()
        zimul.goto(sakx, saky)
        zimul.pendown()
        draw(zimul, points, sakx, saky) # zīmēšanas funkcija
        turtle.exitonclick() # gaida pēc zīmēšanas, kamēr nospiež peli
else:
    print ('Pievienojiet komandai skaitļa x vērtību kā argumentu, piem "python turtle_func.py 300"')
