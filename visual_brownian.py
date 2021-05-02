from math import *
from vpython import *
import numpy as np
import time
import random


def brownian_motion_simulation(m=2, n=1001, d=10.0, t=1.0):

    # *****************************************************************************80
    #
    ## BROWNIAN_MOTION_SIMULATION simulates Brownian motion.
    #
    #  Discussion:
    #
    #    Thanks to Feifei Xu for pointing out a missing factor of 2 in the
    #    stepsize calculation, 08 March 2016.
    #
    #    Thanks to Joerg Peter Pfannmoeller for pointing out a missing factor
    #    of M in the stepsize calculation, 23 April 2018.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #    10 June 2018
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, integer M, the spatial dimension.
    #    This defaults to 2.
    #
    #    Input, integer N, the number of time steps to take, plus 1.
    #    This defaults to 1001.
    #
    #    Input, real D, the diffusion coefficient.
    #    This defaults to 10.0.
    #
    #    Input, real T, the total time.
    #    This defaults to 1.0
    #
    #    Output, real X(M,N), the initial position at time 0.0, and
    #    the N-1 successive locations of the particle.
    #

    #
    #  Set the time step.
    #
    dt = t / float(n - 1)
    #
    #  Compute the individual steps.
    #
    x = np.zeros([m, n])

    for j in range(1, n):
        #
        #  S is the stepsize
        #
        s = np.sqrt(2.0 * m * d * dt) * np.random.randn(1)
        #
        #  Direction is random.
        #
        if m == 1:
            dx = s * np.ones(1)
        else:
            dx = np.random.randn(m)
            norm_dx = np.sqrt(np.sum(dx ** 2))
            for i in range(0, m):
                dx[i] = s * dx[i] / norm_dx
        #
        #  Each position is the sum of the previous steps.
        #
        x[0:m, j] = x[0:m, j - 1] + dx[0:m]

    return x


x = 0
y = 0
z = 0
SphereRadius = 0.2
particle = sphere(
    pos=vector(x, y, z), color=color.yellow, radius=SphereRadius, opacity=0.6
)

Trace = curve(color=color.yellow)
scene.autoscale = False  # prevents automatic rescaling of
# display window

while True:
    rate(100)
    x = x + 0.1 * random.randint(0, 1) * np.random.randn(1)
    y = y + 0.1 * random.randint(0, 1) * np.random.randn(1)
    z = z + 0.1 * random.randint(0, 1) * np.random.randn(1)
    particle.pos = vector(x, y, z)
    Trace.append(particle.pos)
    time.sleep(random.randint(0, 1))
