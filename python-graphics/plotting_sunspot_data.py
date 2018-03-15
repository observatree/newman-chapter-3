
from numpy import loadtxt

import sys

from pylab import plot, ylim, show
# noinspection PyUnresolvedReferences
from numpy import linspace, sin

data = loadtxt(sys.argv[1], float)

x = linspace(0, 10, 100)

y = sin(x)

plot(x, y)

ylim(-1.1, 1.1)

show()
