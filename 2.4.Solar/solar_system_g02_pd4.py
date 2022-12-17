import turtle
import math

class SolarSystem:
    def __init__(self, width, height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width/2.0, -height/2.0,
                                             width/2.0, height/2.0)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def addSun(self, aSun):
        self.__theSun = aSun

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)

    def sortPlanets(self): # 4.2.1 task a)
        planet_order_sorted = sorted(self.__planets)
        planet_order_sorted_print = [str(p) for p in planet_order_sorted]
        print ("Planets:", planet_order_sorted_print)
        print ("Sun:", str(self.__theSun))
        self.__ssTurtle.up()
        self.__ssTurtle.setposition(-0.9, 0.9)
        self.__ssTurtle.down()
        self.__ssTurtle.write("Sun:"+str(self.__theSun) + " - planets:"+str(planet_order_sorted_print), font=('monaco',30,'bold'))
        self.__ssTurtle.up()
            
    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.__planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(),
                     p.getYPos() + dt * p.getYVel())

            rX = self.__theSun.getXPos() - p.getXPos()
            rY = self.__theSun.getYPos() - p.getYPos()
          
            r = math.sqrt(rX**2 + rY**2)

            accX = G * self.__theSun.getMass() * rX/r**3
            accY = G * self.__theSun.getMass() * rY/r**3

            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY) 

    def freeze(self):
        self.__ssScreen.exitonclick() 

class Sun:
   def __init__(self, iName, iRad, iM, iTemp):
       self.__name = iName
       self.__radius = iRad
       self.__mass = iM
       self.__temp = iTemp
       self.__x = 0
       self.__y = 0

       self.__sTurtle = turtle.Turtle()
       self.__sTurtle.shape("circle")
       self.__sTurtle.color("yellow")

   def getMass(self):
       return self.__mass

   def __str__(self):
        return self.__name

   def getXPos(self):
       return self.__x

   def getYPos(self):
       return self.__y

class Planet:
    def __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        self.__velX = iVx
        self.__velY = iVy 

        self.__x = self.__distance
        self.__y = 0
        self.__color = iC

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")
        self.__pTurtle.turtlesize(self.__radius/50.0) # 4.2.1 task b)

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.down()

# 4.2.1 task c)
        self.__moons = []

    def addMoon(self, aMoon):
        self.__moons.append(aMoon)

    def getMoons(self):
        return self.__moons

# END - 4.2.1 task c)

    def getName(self):
        return self.__name

    def getRadius(self):
        return self.__radius

    def getMass(self):
        return self.__mass

    def getDistance(self):
        return self.__distance

    def getVolume(self):
        import math
        v = 4/3 * math.pi * self.__radius**3
        return v

    def getSurfaceArea(self):
        import math
        sa = 4 * math.pi * self.__radius**2
        return sa

    def getDensity(self):
        d = self.__mass / self.getVolume()
        return d

    def setName(self, newName):
        self.__name = newName 

    def setRadius(self, newRadius):
        self.__radius = newRadius 

    def setMass(self, newMass):
        self.__mass = newMass 

    def setDistance(self, newDistance):
        self.__distance = newDistance 

    def __str__(self):
        out = self.__name   # papildināts priekš 4.2.1 c)
        for m in self.__moons:
            out = out + "+" + str(m)
        return out
      
    def __lt__(self, otherPlanet):
        return self.__distance < otherPlanet.__distance

    def __gt__(self, otherPlanet):
        return self.__distance > otherPlanet.__distance  

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)
        for m in self.__moons: # papildināts priekš 4.2.1 c)
            m.moveTo(self.__x, self.__y)

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy 

class Moon: # papildināts priekš 4.2.1 c)
    def __init__(self, iName, iX, iY):
        self.__name = iName
        self.__x = iX
        self.__y = iY
    
        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color("gray")
        self.__pTurtle.shape("circle")
        self.__pTurtle.turtlesize(0.4)

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)

    def __str__(self):
        return self.__name
        
    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)


def createSSandAnimate():
   ss = SolarSystem(2, 2)

   sun = Sun("Sun", 5000, 10, 5800)
   ss.addSun(sun)

   m = Planet("Jupiter", 100, 49000, 0.7, 0, 1, "black")
   ss.addPlanet(m)

   m = Planet("Mercury", 19.5, 1000, .25, 0, 2, "blue")
   ss.addPlanet(m)

   m = Planet("Earth", 47.5, 5000, 0.3, 0, 2.0, "green")
   moon = Moon("Meness", 0.3, 0.0) # papildināts priekš 4.2.1 c)
   m.addMoon(moon)
   ss.addPlanet(m)

   m = Planet("Mars", 50, 9000, 0.5, 0, 1.63, "red")
   ss.addPlanet(m)

   ss.sortPlanets() # Izdrukā - 4.2.1 uzdevumu a) 

   numTimePeriods = 2000
   for aMove in range(numTimePeriods):
        ss.movePlanets()

   ss.freeze()


createSSandAnimate()