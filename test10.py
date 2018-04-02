import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

PI = 3.1415926535897932384626433832795
rot = 0
			
def Cyl(x, y, z, length, radius, smoothness):
	global rot
	#glBegin(GL_POLYGON)
	#glVertex3f(0,0,0)
	#glVertex3f(1,1,1)
	#glVertex3f(1,2,3)
	c = 6 / 4
	i = rot
	
	#glMatrixMode(GL_MODELVIEW)
	#glLoadIdentity()
	
	#glPushMatrix()
	#glTranslatef(x, y, z)
	#glRotatef(1, 0, 0, 1)
	#glTranslatef(-x, -y, -z)
	while ( i < (2 * PI) + rot):
		temp = i
		i = i + (PI / 12)
		glColor4f(0.0, 0.0, 0.0, 1.0)
		if (c == 1):
			glColor4f(0.8, 0.8, 1.0, 1.0)
			
		glBegin(GL_TRIANGLES)
		glVertex3f(x, y, z)
		glVertex3f(x + cos(temp) * radius, y + sin(temp) * radius, z)
		glVertex3f(x + cos(i) * radius,y + sin(i) * radius, z)
		glEnd()
		
		glBegin(GL_TRIANGLES)
		glVertex3f(x, y, z + length)
		glVertex3f(x + cos(temp) * radius, y + sin(temp) * radius, z + length)
		glVertex3f(x + cos(i) * radius, y + sin(i) * radius, z + length)
		glEnd()
		
		glColor4f(1.0, 1.0, 1.0, 1.0)
		glBegin(GL_QUADS)
		glVertex3f(x + cos(temp) * radius, y + sin(temp) * radius, z)
		glVertex3f(x + cos(i) * radius, y + sin(i) * radius, z)
		glVertex3f(x + cos(i) * radius, y + sin(i) * radius, z + length)
		glVertex3f(x + cos(temp) * radius, y + sin(temp) * radius, z + length)
		glEnd()
		
		c = c - 1
		if ( c < 0):
			c = 12/4
		
	#glPopMatrix()
			
def Squa(x0, y0, z0, x1, y1, z1, x2, y2, z2, x3, y3, z3):
	#glColor4f(1.0, 1.0, 1.0, 1.0)
	glBegin(GL_QUADS)
	glVertex3f(x0, y0, z0)
	glVertex3f(x1, y1, z1)
	glVertex3f(x2, y2, z2)
	glVertex3f(x3, y3, z3)
	glEnd()
	
def main():
	
    global rot
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    glEnable(GL_BLEND)
    glEnable(GL_DEPTH_TEST)
    
    glDepthFunc(GL_LESS)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0,0, -20)

    glRotatef(25, 2, 1, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #glTranslatef(-0.5,0,0)
                    glRotatef(10, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    #glTranslatef(0.5,0,0)
                    glRotatef(-10, 0, 1, 0)

                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    glRotatef(10,1,0,0)

                if event.button == 4:
                    glRotatef(-10,1,0,0)
                    
                if event.button == 1:
                    glRotatef(10, 0,0,1)
                
                if event.button == 3:
                    glRotatef(-10, 0,0,1)

        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        
        
        #draw()
        
        glColor3f(0.9, 0.1, 0.1)
        Squa(-0.3, 0.5, 0.4, 
			 2.0, 0.5, 0.4, 
			 2.0, 2.0, 0.4, 
			 -0.3, 1.8, 0.4)
		
        glColor3f(0.9, 0.1, 0.1)
        Squa(-0.3, 0.5, 0.4, 
			-0.3, 1.8, 0.4, 
			-0.3, 1.8, 3.9, 
			-0.3, 0.5, 3.9)
		
        glColor3f(0.9, 0.1, 0.1)
        Squa(-0.3, 0.5, 3.9, 
			 2.0, 0.5, 3.9, 
			 2.0, 2.0, 3.9, 
			 -0.3, 1.8, 3.9)
		
        glColor3f(0.1, 0.1, 0.1)
        Squa(-0.3, 1.8, 0.4,
			2.0, 2.0, 0.4,
			2.0, 2.0, 3.9,
			-0.3, 1.8, 3.9)
			
		#windshield depan
        glColor3f(0.3, 0.4, 0.5)
        Squa(2.0, 2.0, 0.5,
			2.0, 2.0, 3.8,
			2.5, 3.3, 3.8,
			2.5, 3.3, 0.5)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(2.0, 2.0, 0.5,
			2.0, 2.0, 0.4,
			2.5, 3.3, 0.4,
			2.5, 3.3, 0.5)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(2.0, 2.0, 3.8,
			2.0, 2.0, 3.9,
			2.5, 3.3, 3.9,
			2.5, 3.3, 3.8)
			
        glColor3f(0.9, 0.1, 0.1)	
        Squa(2.5, 3.3, 0.4,
			2.5, 3.3, 3.9,
			4.5, 3.3, 3.9,
			4.5, 3.3, 0.4)
		
        glColor3f(0.9, 0.1, 0.1)	
        Squa(4.5, 3.3, 0.4,
			4.5, 3.3, 3.9,
			6.75, 3.3, 3.9,
			6.75, 3.3, 0.4)
			
		#windshield belakang
        glColor3f(0.3, 0.4, 0.5)
        Squa(6.75, 3.3, 0.5,
			6.75, 3.3, 3.8,
			7.0, 2.0, 3.8,
			7.0, 2.0, 0.5)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(6.75, 3.3, 0.4,
			6.75, 3.3, 0.5,
			7.0, 2.0, 0.5,
			7.0, 2.0, 0.4)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(6.75, 3.3, 3.8,
			6.75, 3.3, 3.9,
			7.0, 2.0, 3.9,
			7.0, 2.0, 3.8)
			
		#windshield kanan
        glColor3f(0.3, 0.4, 0.5)
        Squa(4.0, 3.3, 0.4,
			4.0, 2.0, 0.4,
			2.1, 2.0, 0.4,
			2.6, 3.3, 0.4)
        glColor3f(0.3, 0.4, 0.5)
        Squa(5.6, 3.3, 0.4,
			5.6, 2.0, 0.4,
			4.1, 2.0, 0.4,
			4.1, 3.3, 0.4)
        glColor3f(0.3, 0.4, 0.5)
        Squa(6.65, 3.3, 0.4,
			6.9, 2.0, 0.4,
			5.7, 2.0, 0.4,
			5.7, 3.3, 0.4)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(4.0, 3.3, 0.4,
			4.0, 2.0, 0.4,
			4.1, 2.0, 0.4,
			4.1, 3.3, 0.4)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(5.7, 3.3, 0.4,
			5.7, 2.0, 0.4,
			5.6, 2.0, 0.4,
			5.6, 3.3, 0.4)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(6.65, 3.3, 0.4,
			6.9, 2.0, 0.4,
			7.0, 2.0, 0.4,
			6.75, 3.3, 0.4)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(2.5, 3.3, 0.4,
			2.0, 2.0, 0.4,
			2.1, 2.0, 0.4,
			2.6, 3.3, 0.4)
			
		#windshield kanan
        glColor3f(0.3, 0.4, 0.5)
        Squa(4.0, 3.3, 3.9,
			4.0, 2.0, 3.9,
			2.1, 2.0, 3.9,
			2.6, 3.3, 3.9)
        glColor3f(0.3, 0.4, 0.5)
        Squa(5.6, 3.3, 3.9,
			5.6, 2.0, 3.9,
			4.1, 2.0, 3.9,
			4.1, 3.3, 3.9)
        glColor3f(0.3, 0.4, 0.5)
        Squa(6.65, 3.3, 3.9,
			6.9, 2.0, 3.9,
			5.7, 2.0, 3.9,
			5.7, 3.3, 3.9)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(4.0, 3.3, 3.9,
			4.0, 2.0, 3.9,
			4.1, 2.0, 3.9,
			4.1, 3.3, 3.9)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(5.7, 3.3, 3.9,
			5.7, 2.0, 3.9,
			5.6, 2.0, 3.9,
			5.6, 3.3, 3.9)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(6.65, 3.3, 3.9,
			6.9, 2.0, 3.9,
			7.0, 2.0, 3.9,
			6.75, 3.3, 3.9)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(2.5, 3.3, 3.9,
			2.0, 2.0, 3.9,
			2.1, 2.0, 3.9,
			2.6, 3.3, 3.9)
			
        glColor3f(0.9, 0.1, 0.1)
        Squa(7.0, 2.0, 0.4,
			7.0, 2.0, 3.9,
			7.0, 0.5, 3.9,
			7.0, 0.5, 0.4)
		
        glColor3f(0.9, 0.1, 0.1)	
        Squa(7.0, 0.5, 3.9,
			7.0, 2.0, 3.9,
			6.5, 2.0, 3.9,
			6.5, 0.5, 3.9)
		
        glColor3f(0.9, 0.1, 0.1)	
        Squa(6.5, 0.5, 3.9,
			6.5, 2.0, 3.9,
			6.5, 2.0, 3.9,
			6.5, 0.5, 3.9)
			
        Squa(7.0, 0.5, 0.4,
			7.0, 2.0, 0.4,
			6.5, 2.0, 0.4,
			6.5, 0.5, 0.4)
			
        Squa(6.5, 2.0, 3.9,
			6.5, 0.5, 3.9,
			2.0, 0.5, 3.9,
			2.0, 2.0, 3.9)
			
        Squa(6.5, 2.0, 0.4,
			6.5, 0.5, 0.4,
			2.0, 0.5, 0.4,
			2.0, 2.0, 0.4)
		
        #glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        
        glRotatef(1, 0, 0, 1)
        Cyl(1.0, 0.6, 0.0, 0.3, 0.8, 12)
        Cyl(1.0, 0.6, 4.0, 0.3, 0.8, 12)
        Cyl(1.0, 0.6, 0.3, 3.7, 0.1, 12)
        glPopMatrix()
        
        glPushMatrix()
        glRotatef(1, 0, 0, 1)
        Cyl(6.0, 0.6, 0.0, 0.3, 0.8, 12)
        Cyl(6.0, 0.6, 4.0, 0.3, 0.8, 12)
        Cyl(6.0, 0.6, 0.3, 3.7, 0.1, 12)	
        glPopMatrix()
		
        #draw_circle(0.0, 0.0, 0.5, 12)
        #draw_tube()
        rot = rot - 1
        
        pygame.display.flip()
        pygame.time.wait(0)
		
main()
