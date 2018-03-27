from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

window = 0                                             # glut window number
width, height = 800, 600                               # window size
PI = 3.1415926535897932384626433832795
rot = 0

interval = 30

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)
   
    glColor3f(1.0, 1.0, 1.0)
    draw_rect(100, 100, 200, 100)

    draw_circle_tri(600, 100, 60, 24)
    draw_circle_tri(285, 100, 60, 24)
   
    glutSwapBuffers()                                  # important for double buffering
   
def draw_rect(x, y, width, height):
	glBegin(GL_POLYGON)
	glVertex2f(x, y)
	glVertex2f(x, y + 100)
	glVertex2f(x + 150, y + 100)
	glVertex2f(x + 250, y + 200)
	glVertex2f(x + 450, y + 200)
	glVertex2f(x + 550, y + 130)
	glVertex2f(x + 650, y + 100)
	glVertex2f(x + 650, y + 25)
	glVertex2f(x + 625, y)
	glEnd()

def draw_circle(x, y, radius, smoothness):
	
	global rot
	c = 1
	#glRotatef(40.0, 0.0, 0.0, 1.0)
	#glColor3f(1.0, 0.0, 0.0)
	#glScalef(2.0, 2.0, 2.0)
	glBegin(GL_POLYGON)
 	i = rot
 	while (i < (2 * PI + rot)):
		glColor3f(0.0, 0.0, 1.0)
		if ( c == 1 ) :
			glColor3f(0.0, 1.0, 0.0)
		
		if ( c == 0 ) :
			glColor3f(1.0, 0.0, 0.0)
 		glVertex2f(x + cos(i) * radius, y + sin(i) * radius)
 		i = i + (PI / smoothness)
 		c = c - 1
 		if ( c < 0 ) :
			c = 1
	glEnd()
	
def draw_circle_tri(x, y, radius, smoothness):
	
	global rot
	c = smoothness / 4
	i = rot
	while (i < (2 * PI + rot)):
		temp = i
		i = i + (PI / smoothness)
		glColor3f(1.0, 0.0, 0.0)
		if (c == 1):
			glColor3f(0.0, 0.0, 1.0)
		
		glBegin(GL_TRIANGLES)
		glVertex2f(x,y)
		glVertex2f(x + cos(temp) * radius, y + sin(temp) * radius)
		glVertex2f(x + cos(i) * radius, y + sin(i) * radius)
		glEnd()
		
		c = c - 1
		if (c < 0):
			c = smoothness / 4

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    #glViewport(0,0,width,height)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def update(value):
	global rot
	
	glPushMatrix()
	#glScalef(2.0, 2.0, 2.0)
	#glRotatef(10.0, 0.0, 0.0, 1.0)
	rot = rot - 0.5
	#draw_circle(600, 100, 60, 6)
	glPopMatrix()
	glutTimerFunc(interval, update, 0)

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("halotole")	               # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutTimerFunc(interval, update, 0)
glutMainLoop()       
