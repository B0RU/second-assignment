from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from numpy import *

def initialize():
    glMatrixMode(GL_PROJECTION)
    #glOrtho(-10,-10,-10,-10,-10,-10)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glClearColor(0,0,0,0)
x = 0
angle = 0
z = 1
def draw():
    global x,angle, z
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glColor(1,0,0)

    # Road
    glLoadIdentity()
    glColor3f(.1, .1, .1)
    glTranslate(0, -1.80, 0)
    glScale(100, 0.5, 10)
    glutSolidCube(1)

    # RoadMarks
    glLoadIdentity()
    glColor3f(0.6, 0.6, 0.6)
    glTranslate(-2, -1.80, 0)
    glScale(6, 0.5, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0.6, 0.6, 0.6)
    glTranslate(-15, -1.80, 0)
    glScale(6, 0.5, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0.6, 0.6, 0.6)
    glTranslate(10, -1.80, 0)
    glScale(6, 0.5, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(0, 2.6, 0)
    glScale(50, 0.5, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(0, -15, 0)
    glScale(100, 0.5, 4)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(0, -15, 0)
    glScale(6, 0.5, 4)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-12, -15, 0)
    glScale(7.5, 0.5, 4)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-28, -15, 0)
    glScale(9, 0.5, 4)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(0, 2.6, 0)
    glScale(3, 0.5, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(5, 2.6, 0)
    glScale(2.5, 0.5, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-5, 2.6, 0)
    glScale(3, 0.5, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-11, 2.6, 0)
    glScale(3, 0.5, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(-17, 2.6, 0)
    glScale(3, 0.5, 1)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(9, 2.6, 0)
    glScale(3, 0.5, 1)
    glutSolidCube(1)



    #car

    glLoadIdentity()
    glColor(1,0,0)
    glTranslate(x,0,0)
    glScale(1,0.25,0.5)
    glutWireCube(5)

    glLoadIdentity()
    glTranslate(x+0,5*0.25,0)
    glScale(0.5,0.25,0.5)
    glutWireCube(5)

    glColor(0,0,1)
    glLoadIdentity()
    glTranslate(x+2.5,-2.5*0.25,2.5*0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125,0.5,12,8)

    glColor(0, 0, 1)
    glLoadIdentity()
    glTranslate(x+2.5, -2.5 * 0.25, -2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    glColor(0, 0, 1)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * 0.25, 2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    glColor(0, 0, 1)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5 * 0.25, -2.5 * 0.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    if x >= 7:
        z = -1
    if x < -10:
        z = 1

    x += 0.001 * z
    angle += 1 * z
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"car")
initialize()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()