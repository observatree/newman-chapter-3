
from pylab import plot, show, xlim, ylim
from numpy import loadtxt
import sys

data = loadtxt(sys.argv[1], float)
print(data)
x = data[:, 0]
y = data[:, 1]
plot(x, y)
show()
