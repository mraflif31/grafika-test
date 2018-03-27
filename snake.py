from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import randint

window = 0                                             # glut window number
width, height = 500, 500                               # window size
field_width, field_height = 50, 50                     # internal resolution
snake = [(20, 20)]
snake_dir = (1,0)
food = []

interval = 200

def refresh2d_custom(width, height, internal_width, internal_height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, internal_width, 0.0, internal_height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
   
def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle
   
def draw():                                            # draw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d_custom(width, height, field_width, field_height)
   
    draw_food()
    draw_snake()
   
    glutSwapBuffers()                                  # important for double buffering

def draw_snake():
	glColor3f(1.0, 1.0, 1.0)
	for x, y in snake:
		draw_rect(x, y, 1, 1)

def draw_food():
	glColor3f(0.5, 0.5, 1.0)
	for x, y in food:
		draw_rect(x, y, 1, 1)

def update(value):
	snake.insert(0, vec_add(snake[0], snake_dir))
	snake.pop()

	#spawn food
	r = randint(0, 20)
	if r == 0:
		x, y = randint(0, field_width), randint(0, field_height)
		food.append((x, y))

	(hx, hy) = snake[0]
	for x, y in food:
		if hx == x and hy == y:
			snake.append((x, y))
			food.remove((x, y))

	glutTimerFunc(interval, update, 0) # trigger next update

def vec_add((x1, y1), (x2, y2)):
	return (x1 + x2, y1 + y2)

def keyboard(*args):
	global snake_dir

	if args[0] == 'w':
		snake_dir = (0, 1)
	if args[0] == 'a':
		snake_dir = (-1, 0)
	if args[0] == 's':
		snake_dir = (0, -1)
	if args[0] == 'd':
		snake_dir = (1, 0)
	
   

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("halotole")                  # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutTimerFunc(interval, update, 0)
glutKeyboardFunc(keyboard)
glutMainLoop()   