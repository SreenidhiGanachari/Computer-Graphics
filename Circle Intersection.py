from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
def randompoints():
     glClear(GL_COLOR_BUFFER_BIT)
     glColor3f(0.0, 0.0, 0.0)
     
     glBegin(GL_LINES)
     glVertex2f(0,0)
     glVertex2f(-10,0)
     glEnd()
     glBegin(GL_LINES)
     glVertex2f(-10,0)
     glVertex2f(-5,-15)
     glEnd()
     glBegin(GL_LINES)
     glVertex2f(-5,-15)
     glVertex2f(0,0)
     glEnd()
    
     posx,posy=10,0
     sides=100
     radius=20
     glBegin(GL_LINE_LOOP)
     glColor3f(0.0, 1.0, 0.0)
     for i in range(100):
         xaxis = radius*cos((i*2*pi/sides))+ posx
         yaxis = radius*sin((i*2*pi/sides))+ posy
         glVertex2f(xaxis,yaxis)
     glEnd()

     posx,posy=-20,0
     sides=100
     radius=20
     glBegin(GL_LINE_LOOP)
     for i in range(100):
         xaxis = radius*cos((i*2*pi/sides))+ posx
         yaxis = radius*sin((i*2*pi/sides))+ posy
         glVertex2f(xaxis,yaxis)
     glEnd()
     posx,posy=-5,-20
     sides=100
     radius=20
     glBegin(GL_LINE_LOOP)
     for i in range(100):
         xaxis = radius*cos((i*2*pi/sides))+ posx
         yaxis = radius*sin((i*2*pi/sides))+ posy
         glVertex2f(xaxis,yaxis)
     glEnd()
     glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Random Points")
    glutDisplayFunc(randompoints)
    init()
    glutMainLoop()
main()
