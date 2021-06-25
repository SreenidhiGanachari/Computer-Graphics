import pyglet
from pyglet.gl import *
from pyglet import window
from pyglet.window import key
from random import randint

import sys
sys.path.append("../shared")


nNumPoints = 2


ctrlPoints = (GLfloat * 3 * 4)(   (-4.0, 0.0, 0.0),	
                                            (-4.0, 4.0, 0.0),	
                                            (4.0, -4.0, 0.0), 
                                            (4.0, 0.0, 0.0))
nNumPoints1 = 3


ctrlPoints1 = (GLfloat * 3 * 4)(   (-4.0, 0.0, 0.0),	
                                            (0.0, -4.0, 0.0),	
                                            (0.0, 4.0, 0.0), 
                                            (4.0, 0.0, 0.0))





def DrawPoints():
    
    glPointSize(5.0)
    glBegin(GL_POINTS)
    for i in range(0, nNumPoints):
       glVertex2fv(ctrlPoints[i])
    glEnd()

def DrawPoints1():
    
    glPointSize(5.0)
    glBegin(GL_POINTS)
    for i in range(0, nNumPoints1):
       glVertex2fv(ctrlPoints1[i])
    glEnd()    

    


class MainWindow(window.Window):
    def __init__(self, *args, **kwargs):
        window.Window.__init__(self, *args, **kwargs)

       
        glClearColor(1.0, 1.0, 1.0, 1.0 )

        glColor3f(1.0, 0.0, 0.0)	


   
    def on_draw(self):
      
        glClear(GL_COLOR_BUFFER_BIT)

        
        glMap1f(GL_MAP1_VERTEX_3,  
        0.0,                                   
        100.0,                                 
        3,                                       
        nNumPoints,                        
        ctrlPoints[0])                  

     
        glEnable(GL_MAP1_VERTEX_3)

        
        glBegin(GL_LINE_STRIP)
        
        for i in range (0, 101):

            glEvalCoord1f(i) 
        glEnd()

        
        DrawPoints()
        

    def on_draw(self):
      
        glClear(GL_COLOR_BUFFER_BIT)

        
        glMap1f(GL_MAP1_VERTEX_3,  
        0.0,                                   
        100.0,                                 
        3,                                       
        nNumPoints1,                        
        ctrlPoints1[0])                  

     
        glEnable(GL_MAP1_VERTEX_3)

        
        glBegin(GL_LINE_STRIP)
        
        for i in range (0, 101):

            glEvalCoord1f(i) 
        glEnd()

        
        DrawPoints1()        

    
    def on_resize(self, w, h):

        
        if h == 0:
            h = 1

       
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        


if __name__ == '__main__':
    w = MainWindow(800, 600, caption='2D Bezier Curve', resizable=True)
    pyglet.app.run()
