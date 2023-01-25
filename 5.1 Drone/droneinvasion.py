from turtle import *
import math
import random
from abc import *

class Score(Turtle):
    score = 0
    scorestring = "Punkti: %s" %score
    playing = True

    def __init__(self):
        super().__init__()
        Score.updateScore(0)

    @staticmethod
    def updateScore(punkti):
        if Score.playing:
            Score.score = Score.score + punkti
            Score.scorestring = "Punkti: %s" %Score.score
            clear()
            hideturtle()
            penup()
            setposition(-190,390)
            write(Score.scorestring,  font=("Arial",14,"normal"))

            if Score.score >= 100:
                Score.playing = False
                clear()
                hideturtle()
                penup()
                setposition(0,200)
                write("Uzvara!!!",  font=("Arial",24,"normal"))
            if Score.score <= -100:
                Score.playing = False
                clear()
                hideturtle()
                penup()
                setposition(0,200)
                write("Zaudēji :(",  font=("Arial",24,"normal"))
       

class LaserCannon(Turtle):
    def __init__(self, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__screen = self.getscreen()
        self.__screen.onclick(self.aim)
        self.__screen.onkey(self.shoot, 's')
        self.__screen.onkey(self.quit, 'q')

    def aim(self, x, y):
        heading = self.towards(x, y)
        self.setheading(heading)

    def shoot(self):
        Bomb(self.heading(), 5, self.__xMin, self.__xMax, 
                                self.__yMin, self.__yMax)

    def quit(self):
        self.__screen.bye()

class BoundedTurtle(Turtle):
    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__()
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__speed = speed

    def outOfBounds(self):
        xPos, yPos = self.position()
        out = False
        if xPos < self.__xMin or xPos > self.__xMax:
            out = True
        if yPos < self.__yMin or yPos > self.__yMax:
            out = True
        return out

    def getSpeed(self):
        return self.__speed

    def getXMin(self):
        return self.__xMin
  
    def getXMax(self):
        return self.__xMax
  
    def getYMin(self):
        return self.__yMin
  
    def getYMax(self):
        return self.__yMax

    @abstractmethod  
    def remove(self):
        pass

    @abstractmethod
    def move(self):
       pass
       
class Drone(BoundedTurtle):

    droneList = []     #static variable

    @staticmethod
    def getDrones():
        return [x for x in Drone.droneList if x.__alive]

    def __init__(self, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.getscreen().tracer(0)
        self.up()
        if 'Drone.gif' not in self.getscreen().getshapes():
            self.getscreen().addshape('Drone.gif')
        self.shape('Drone.gif')
        self.goto(random.randint(xMin - 1, xMax - 1), yMax - 20)
        self.setheading(random.randint(250, 290))
        self.getscreen().tracer(1)
        Drone.droneList = Drone.getDrones()
        Drone.droneList.append(self)
        self.__alive = True
        self.getscreen().ontimer(self.move, 200)

    def move(self):
        self.forward(self.getSpeed())
        if self.outOfBounds():
            Score.updateScore(-10) # GV 25.01.2023 -10, ja iziet ārpus ekrāna
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 200)

    def remove(self):
        self.__alive = False
        self.hideturtle()

class Bomb(BoundedTurtle):
    def __init__(self, initHeading, speed, xMin, xMax, yMin, yMax):
        super().__init__(speed, xMin, xMax, yMin, yMax)
        self.resizemode('user')
        self.color('red', 'red')
        self.shape('circle')
        self.turtlesize(.25)
        self.setheading(initHeading)
        self.up()        
        self.getscreen().ontimer(self.move, 100)

    def move(self):
        exploded = False
        self.forward(self.getSpeed())
        for a in Drone.getDrones():
            if self.distance(a) < 5:
                a.remove()
                Score.updateScore(10) # GV 25.01.2023 +10, ja trāpīja
                exploded = True
        if self.outOfBounds() or exploded:
            self.remove()
        else:
            self.getscreen().ontimer(self.move, 100)

    def distance(self, other):
        p1 = self.position()
        p2 = other.position()        
        return math.dist(p1, p2)

    def remove(self):
        self.hideturtle()

class DroneInvasion:
    def __init__(self, xMin, xMax, yMin, yMax):
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax

    def play(self):
        self.__mainWin = LaserCannon(self.__xMin, self.__xMax,
                                self.__yMin, self.__yMax).getscreen()
        self.__mainWin.bgcolor('light green')
        self.__mainWin.setworldcoordinates(self.__xMin, self.__yMin, 
                                          self.__xMax, self.__yMax)
        self.__mainWin.ontimer(self.addDrone, 1000)
        self.__mainWin.listen()
        Score()
        mainloop()

    def addDrone(self):
        if len(Drone.getDrones()) < 7:
            Drone(5, self.__xMin, self.__xMax, 
                     self.__yMin, self.__yMax)
        self.__mainWin.ontimer(self.addDrone, 1000)

di =  DroneInvasion(-200,200,0,400)
di.play()
