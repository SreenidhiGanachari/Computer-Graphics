from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)

def draw():                                            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLineWidth(2.5);
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(5.0,-5,-5)
    
    glColor3f(1.0, 0.0, 0.0);
    glBegin(GL_QUADS);

    glColor3f(1.0, 0.0, 0.0);
    
    glVertex3f(-1, 1, -1);
    glVertex3f(1, 1, -1);
    glVertex3f(1, -1, -1);
    glVertex3f(-1, -1, -1);

    glColor3f(0.0, 0.0, 1.0);
    
    glVertex3f(-1, 1, 1);
    glVertex3f(1, 1, 1);
    glVertex3f(1, -1, 1);
    glVertex3f(-1, -1, 1);

    glColor3f(0.0, 1.0, 0.0);
    
    glVertex3f(-1, 1, -1);
    glVertex3f(-1, -1, -1);
    glVertex3f(-1, -1, 1);
    glVertex3f(-1, 1, 1);

    glColor3f(1.0, 0.0, 0.0);
    glVertex3f(-1, 1, -1);
    glVertex3f(1, 1, -1);
    glVertex3f(1, 1, 1);
    glVertex3f(-1, 1, 1);

    glColor3f(1.0, 0.0, 0.0);
    glVertex3f(1, 1, -1);
    glVertex3f(1, -1, -1);
    glVertex3f(1, -1, 1);
    glVertex3f(1, 1, 1);

    glColor3f(1.0, 0.0, 0.0);
    glVertex3f(-1, -1, -1);
    glVertex3f(1, -1, -1);
    glVertex3f(1, -1, 1);
    glVertex3f(-1, -1, 1);

    
    glEnd()
    glutSwapBuffers()      

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Plot Points")
    glutDisplayFunc(draw)
    glViewport(0,0,500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75.0,1,0.1,45.0)
    
    glRotatef(30,1,0,0)
    glRotatef(30,0,1,0)
    init()
    glutMainLoop()
main()
