#Use Matlab (or any other language) to plot the real part of the signal

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10, 10, 1000)
x = np.exp(-(1+1j*np.pi/2)*t)
plt.plot(t, x.real)
plt.savefig('assignment1.jpg')
plt.show()

#Explanation:
# We can decompose the x(t) function into two parts using the exponent property.
# x(t) = cos(-(1+j*pi/2)*t) + j*sin(-(1+j*pi/2)*t)
# The real part of x(t) is cos(-(1+j*pi/2)*t)
# We can plot the real part of x(t) using the plot function.
# We can plot the real and imaginary parts of x(t) using the plot function.
# The plot becomes x(real) = cos(-(1+j*pi/2)*t)