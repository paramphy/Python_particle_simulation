# A mass m is suspended from a spring of spring constant k.  The mass is
# displaced from equilibrium by an initial distance yo, then released.
# Write a Python program to plot y(t) for some reasonable set of parameters.

from vpython import *
import numpy as np
from matplotlib import pyplot as plt

ball_radius = 0.2

ball = sphere(
    pos=vector(0, 0, 0),
    color=color.red,
    radius=ball_radius,
    opacity=0.6,
    make_trail=True,
    retain=200,
)


def func(t, y0=10, w=2):

    y = y0 * np.sin(w * t)
    return y


def velocityfunc(t, y0=10, w=2):

    y = w * y0 * np.cos(w * t)
    return y


t = np.linspace(0, 10, 1000)
y = func(t)
v = velocityfunc(t)
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(t, y, label="Displacement")  # Plot some data on the axes.
ax.set_xlabel("t")  # Add an x-label to the axes.
ax.set_ylabel("y")  # Add a y-label to the axes.
ax.set_title("Chapter 3 Problem 02")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(y, v, label="")  # Plot some data on the axes.
ax.set_xlabel("y")  # Add an x-label to the axes.
ax.set_ylabel("v")  # Add a y-label to the axes.
ax.set_title("Chapter 3 Problem 03")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
