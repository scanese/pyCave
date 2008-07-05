#    This file is part of pyCave.
#
#    pyCave is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyCave is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pyCave.  If not, see <http://www.gnu.org/licenses/>.

from OpenGL.GL import *
from tga import *

class Sprite:
    '''
    Two dimensional entity displayed as an image.
    Used for explosion-effects and menu graphics
    @params fname: TGA texture filename
    '''
    def __init__(self,fname):
        #Image, position, drawing (tricky)
        self.image = TgaTexture(fname)
        self.image.newGLTexture() 
    
    def draw(self):
        glBindTexture(GL_TEXTURE_2D,self.image.name)
        #rotate
        polygon()
        
    def polygon():
        glBegin(GL_POLYGON)
        glMultiTexCoord2f(GL_TEXTURE1,1 ,1)
        glVertex3i(0,10,10)
        glMultiTexCoord2f(GL_TEXTURE1,1,0)
        glVertex3i(0,10,-10)
        glMultiTexCoord2f(GL_TEXTURE1,0,0)
        glVertex3i(0,-10,-10)
        glMultiTexCoord2f(GL_TEXTURE1, 0, 1)
        glVertex3i(0,-10,10)
        glEnd()

if __name__ == '__main__':
    pass
