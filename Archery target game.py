import math
from graphics import *

def circle(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(circle(p2.getX() - p1.getX())
    + circle(p2.getY() - p1.getY()))
    return dist

win = GraphWin("Archery",400,400)
center = Point(200,200)
color = ["white","black","blue","red","yellow"]
radius = 100;
for i in range(0,5):
    cir = Circle(center, radius)
    cir.draw(win)
    cir.setFill(color[i])
    radius -=20
  
message = Text(Point(80, 20), "Total Score : 0")
message.draw(win)
message2 = Text(Point(80, 40), "")
message2.draw(win)
totalScore = 0;
for i in range(0,5):
    pt = win.getMouse()
    cir = Circle(pt, 5)
    cir.draw(win)
    cir.setFill("black")
    dist = distance(center, pt)
if(dist<=20):
    score = 9
elif(dist<=40):
    score = 7
elif(dist<=60):
    score = 5
elif(dist<=80):
    score = 3
elif(dist<=100):
    score = 1
else:
    score = 0
message2.setText("Hit Score : "+str(score))
totalScore+=score
message.setText("Total Score : "+str(totalScore))
  
win.getMouse()
win.close()
