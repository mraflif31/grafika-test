from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()

import logging
logging.basicConfig()

from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGLContext.arrays import *
from OpenGL.GL import shaders
import math

class TestContext(BaseContext):
	"""Creates a simple vertex shader..."""
	def OnInit( self ):
		VERTEX_SHADER = shaders.compileShader("""
		#version 120 
		void main() { 
			gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex; 
		}""", GL_VERTEX_SHADER)
		
		FRAGMENT_SHADER = shaders.compileShader("""
		#version 120 
		
		uniform vec2 u_resolution;
		
		void main() { 
			gl_FragColor = vec4( 1, 1, 1, 1 ); 
		}""", GL_FRAGMENT_SHADER)
		
		self.shader = shaders.compileProgram(VERTEX_SHADER,FRAGMENT_SHADER)
		
		self.vbo = vbo.VBO( array( [ 
			[ 0, 2, 0 ], 
			[ -2, -2, 0 ], 
			[ 2, -2, 0 ]
		],'f') )
		
		self.vbo2 = vbo.VBO( array( [
			
			[ 3, 5, 0],
			[ 1, 1, 0 ],
			[ 5, 1, 0 ]
		],'f') )
		
	
	def Render(self, mode):
		"""Render the geometry for the scene"""
		shaders.glUseProgram(self.shader)
		
		try:
			self.vbo.bind()
			try:
				glEnableClientState(GL_VERTEX_ARRAY);
				glVertexPointer( 3, GL_FLOAT, 12, self.vbo )
				glDrawArrays(GL_TRIANGLES,0,3)
			finally:
				self.vbo.unbind()
				glDisableClientState(GL_VERTEX_ARRAY);
				
			self.vbo2.bind()	
			try:
				glEnableClientState(GL_VERTEX_ARRAY);
				glVertexPointer( 3, GL_FLOAT, 12, self.vbo2 )
				glDrawArrays(GL_TRIANGLES,0,3)
				
			finally:
				self.vbo2.unbind()
				glDisableClientState(GL_VERTEX_ARRAY);
			
		finally:
			shaders.glUseProgram( 0 )
			
if __name__=="__main__":
	TestContext.ContextMainLoop()
