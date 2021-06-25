from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

xd1,yd1,xd2,yd2 = 500,300,-400,-50;
xmin=-150;
ymin=-150;
xmax=150;
ymax=150;

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(-500,500,-500,500)

def code(x,y):
    c=0;
    if(y>ymax):
        c=8;
    if(y<ymin):
        c=4;
    if(x>xmax):
        c=c|2;
    if(x<xmin):
        c=c|1;
    return c;

def cohen_Line(x1,y1,x2,y2):
    c1=code(x1,y1);
    c2=code(x2,y2);
    m=(y2-y1)/(x2-x1);
    while((c1|c2)>0):
        if((c1 & c2)>0):
           exit(0);
        xi=x1;
        yi=y1;
        c=c1;
        if(c==0):
            c=c2;
            xi=x2;
            yi=y2;
        
        x,y = 0,0
    
        if((c & 8)>0):
           y=ymax;
           x=xi+ 1.0/m*(ymax-yi);
        elif((c & 4)>0):
            y=ymin;
            x=xi+1.0/m*(ymin-yi);
        elif((c & 2)>0):
            x=xmax;
            y=yi+m*(xmax-xi)
        elif((c & 1)>0):
            x=xmin;
            y=yi+m*(xmin-xi);

        if(c==c1):
            xd1=x;
            yd1=y;
            c1=code(xd1,yd1);
        if(c==c2):
            xd2=x;
            yd2=y;
            c2=code(xd2,yd2);
    print(xd1)
    print(yd1)
    print(xd2)
    print(yd2)
    
    mykey(xd1,yd1,xd2,yd2);

def mykey(x1,y1,x2,y2):
    glColor3f(1.0,1.0,1.0);
    glBegin(GL_LINES);
    glVertex2f(x1,y1);
    glVertex2f(x2,y2);
    glEnd();
    glFlush();     

def display():

    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0,0.0,0.0);
    glBegin(GL_LINE_LOOP);
    glVertex2i(xmin,ymin);
    glVertex2i(xmin,ymax);
    glVertex2i(xmax,ymax);
    glVertex2i(xmax,ymin);
    glEnd();
    cohen_Line(xd1,yd1,xd2,yd2);
    glFlush();

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow('Cohen-Sutherland Algorithm ')
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()
