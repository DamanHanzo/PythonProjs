import math
import turtle
import time

class Line(object):
    """Line class"""
    def __init__(self, beg = (0.0, 0.0), end = (0, 0.0),
                 pencolor = "black"):
        """
        create a line starting from the coordinates given by beg to
        the coordinates given by end
        """
        self.pencolor = pencolor
        self.beg = beg
        self.end = end
        self.tag = "Line"

    def __str__(self):
        return "%s(%s,%s)" % (self.tag,self.beg,self.end)

    def draw(self,pen):
        """draw the line using the provided pen"""
        pen.pencolor(self.pencolor)
        if pen.pos() != self.beg:
            pen.up()
            pen.goto(self.beg)
        pen.down()
        pen.goto(self.end)

class Circle(object):
    """Circle class"""
    
    def __init__(self, center = (0.0,0.0), 
    r=50.0,
                 fillcolor="", pencolor="black"):
        """
        circle with center (x,y) and radius r
        """
        self.center = center
        self.radius = r
        self.fillcolor, self.pencolor = fillcolor, pencolor

    def __str__(self):
        return "Circle(%sr%.1f)" % (self.center,self.radius)


    def draw(self, pen):
        pen.seth(0)
        pen.color(self.pencolor, self.fillcolor)
        if pen.pos() != self.center:
            pen.up()
            pen.goto(self.center)
            pen.down()
        if self.fillcolor: pen.begin_fill()
        pen.circle(self.radius)
        pen.end_fill()
  


class Rectangular(object):
    def __init__(self,lin1,lin2,lin3,lin4):
        self.line1 = Line(lin1,lin2)
        self.line2 = Line(lin2,lin3)
        self.line3 = Line(lin3,lin4)
        self.line4 = Line(lin4,lin1)

    def draw(self,pen):
        self.line1.draw(pen)
        self.line2.draw(pen)
        self.line3.draw(pen)
        self.line4.draw(pen)
    

class Triangle(object):
    def __init__(self, cor1,cor2,cor3):
        self.line1 = Line(cor1,cor2)
        self.line2 = Line(cor2,cor3)
        self.line3 = Line(cor3,cor1)

    def draw(self,pen):
        self.line1.draw(pen)
        self.line2.draw(pen)
        self.line3.draw(pen)
        

def main():
    pen = turtle.Turtle()
    
##    lines = [Line((0,0),(40,20)), Line((0,20), (40,0), "red")]
##
##    for line in lines:
##        print ("\t", line)
##        line.draw(pen)
##    print

##    circle = Circle((15.0, 20.0), 60, 'blue', 'black')
##    circle.draw(pen)
##    print(circle)
##    pen.hideturtle()   # uncomment to hide the turtle

    triangle=Triangle((10,20),(100,300),(300,400))
    triangle.draw(pen)
    #print(triangle)

##    rectangle = Rectangular((70,80),(50,40),(50,40),(70,80))
##    rectangle.draw(pen)
main()

class House(object):
    pass

def housedemo():
    pen = turtle.Turtle()
    h = House()
    h.draw(pen)
    pen.hideturtle()
