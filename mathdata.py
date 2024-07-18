import numpy
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)
y = numpy.median(speed)
print(y)
z=stats.mode(speed)
print(z)
