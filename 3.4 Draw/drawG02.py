import turtle

class Canvas:
    def __init__(self, w, h):
        self.__visibleObjects = []   #list of shapes to draw
        self.__turtle = turtle.Turtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width = w, height = h)
        self.__turtle.hideturtle()

    def drawAll(self):
        self.__turtle.reset()
        self.__turtle.up()
        self.__screen.tracer(0)
        for shape in self.__visibleObjects: #draw all shapes in order
            shape._draw(self.__turtle)
        self.__screen.tracer(1)
        self.__turtle.hideturtle()

    def addShape(self, shape):
        self.__visibleObjects.append(shape)

    def draw(self, gObject):
        gObject.setCanvas(self)
        gObject.setVisible(True)
        self.__turtle.up()
        self.__screen.tracer(0)
        gObject._draw(self.__turtle)
        self.__screen.tracer(1)
        self.addShape(gObject)

    def freeze(self):
        self.__screen.exitonclick()

from abc import *
class GeometricObject(ABC):         #inherit from Abstract Base Class
    def __init__(self):
        self.__lineColor = 'black'
        self.__lineWidth = 1
        self.__visible = False
        self.__myCanvas = None

    def setColor(self, color):  #modified to redraw visible shapes
        self.__lineColor = color
        if self.__visible:
            self.__myCanvas.drawAll()

    def setWidth(self, width):  #modified to redraw visible shapes
        self.__lineWidth = width
        if self.__visible:
            self.__myCanvas.drawAll()

    def getColor(self):
        return self.__lineColor

    def getWidth(self):
        return self.__lineWidth

    @abstractmethod
    def _draw(self):
        pass

    def setVisible(self, vFlag):
        self.__visible = vFlag

    def getVisible(self):
        return self.__visible

    def setCanvas(self, theCanvas):
        self.__myCanvas = theCanvas

    def getCanvas(self):
        return self.__myCanvas        

class Point(GeometricObject):
    def __init__(self, x, y):
        super().__init__()
        self.point = (x, y) # GV 09.01.2023 Tuple

    def getCoord(self):
        return (self.point)

    def getX(self):
        return self.point[0] # GV 09.01.2023 Return 0th element = X

    def getY(self):
        return self.point[1] # GV 09.01.2023 Return 1st element = Y

    def _draw(self, turtle):
        turtle.goto(self.point[0], self.point[1])
        turtle.dot(self.getWidth(), self.getColor())

class PointOLD(GeometricObject):
    def __init__(self, x, y):
        super().__init__()
        self.__x = x
        self.__y = y

    def getCoord(self):
        return (self.__x, self.__y)

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def _draw(self, turtle):
        turtle.goto(self.__x, self.__y)
        turtle.dot(self.getWidth(), self.getColor())

class Line(GeometricObject):
    def __init__(self, p1, p2):
        super().__init__()
        self.__p1 = p1
        self.__p2 = p2

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2

    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        turtle.goto(self.__p1.getCoord())
        turtle.down()
        turtle.goto(self.__p2.getCoord())

class Polygon(GeometricObject):
    def __init__(self, radius, points):
        super().__init__()
        self.__points = points
        self.__radius = radius

    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        turtle.goto(0, -self.__radius)
        turtle.down()
        turtle.circle(self.__radius, steps = self.__points) # GV 09.01.2023 uztaisām daudzstūra klasi, kas izmanto turtle.circle funkciju, lai zīmētu daudzstūrus

class Triangle(Polygon):
    def __init__(self, radius):
        super().__init__(radius, 3)

class Rectangle(Polygon):
    def __init__(self, radius):
        super().__init__(radius, 4)

class Octagon(Polygon):
    def __init__(self, radius):
        super().__init__(radius, 8)

def test2():
    myCanvas = Canvas(500, 500)
    line1 = Line(Point(-100, -100), Point(100, 100))
    line2 = Line(Point(-100, 100), Point(100, -100))
    line1.setWidth(4)   
    triang = Triangle(100)
    rectang = Rectangle(100)
    octagon = Octagon(120)
    polyg = Polygon(50, 15)
    triang.setColor("Blue")
    triang.setWidth(4)
    rectang.setColor("Green")
    rectang.setWidth(4)
    octagon.setColor("Orange")
    octagon.setWidth(4)
    myCanvas.draw(line1)
    myCanvas.draw(line2)
    myCanvas.draw(triang) 
    myCanvas.draw(rectang)
    myCanvas.draw(octagon)
    myCanvas.draw(polyg)
    line1.setColor('red')
    line2.setWidth(4)
    myCanvas.freeze()  # GV 09.01.2023. Neizvērt beigās logu

test2()