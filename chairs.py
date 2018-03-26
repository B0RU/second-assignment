from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def init():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)


def chairs():

    #first chair



    #seat & back
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1,1,1)
    glTranslate(-0.25,0,-3.25)
    glScale(3,2.5,0.5)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glLineWidth(2)
    glTranslate(1, 0, 0)
    glScale(3, 0.25, 3)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

    #legs

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(-0.32, -1.5, 1.2)
    glScale(1, 5, 1)
    glutSolidCube(0.5)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(2.2, -1.5, 1.2)
    glScale(1, 5, 1)
    glutSolidCube(0.5)
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(1.75, -1.5, -2.2)
    glScale(1, 3.8, 1)
    glutSolidCube(0.5)
    glPopAttrib()
    glPopMatrix()




    #second chair


    #seat & back
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(4.5, 0, -3.25)
    glScale(3, 2.5, 0.5)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glLineWidth(2)
    glTranslate(5.2, 0, 0)
    glScale(2.5, 0.25, 3)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()


    #legs
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(4, -1.5, 1.3)
    glScale(1, 5, 1)
    glutSolidCube(0.5)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(6.2, -1.5, 1.1)
    glScale(1, 5, 1)
    glutSolidCube(0.5)
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 1, 1)
    glTranslate(6, -1.5, -2.2)
    glScale(1, 3.8, 1)
    glutSolidCube(0.5)
    glPopAttrib()
    glPopMatrix()
    glFlush()



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"chairs")
glutDisplayFunc(chairs)
init()
glutMainLoop()
