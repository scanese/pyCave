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

import sys
import os
#TODO: Only if in windows:
sys.path.insert(0, os.path.join(sys.prefix, "pyopengl-3.0.0b2-py2.5.egg"))
sys.path.insert(0, os.path.join(sys.prefix, "setuptools-0.6c8-py2.5.egg"))

from renderer import *


class Main:
    def __init__(self):
        if profiling:
            cProfile.runctx('self.re = Renderer()', globals(), locals(), 'startup')
        else:
            self.re = Renderer()
        self.re.mainLoop()
        
app = Main()