import turtle
import time
def draw_circle(x, y, red, green, blue, radius, pen):
    """Draw a cirle"""
    turtle.color(red,green,blue)
    turtle.setpos(x,y-radius)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    pen.goto(x,y)

def bullseye (x,y,pen):
    draw_circle(0,0,0,0,1,100,turtle)
    draw_circle(0,0,1,1,1,70,turtle)
    draw_circle(0,0,0,1,0,50,turtle)
    draw_circle(0,0,1,1,1,30,turtle)
    draw_circle(0,0,1,0,0,20,turtle)

bullseye(0,0,turtle)
time.sleep(5)
turtle.bye()
