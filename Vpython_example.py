#Program showing two simple harmonic motions at 90 degrees
#to each ot her ,and the resulting circular motion of their
#intersection.

from math import *
from vpython import *

RodWidth = 0.1
R = 1.0 # Circle radius
SphereRadius = 0.2
thetao = 0.0
omega = 1.0
dt = 0.01 #time step
time = 0.0

# Initial set up of system
VerticalRod = cylinder(
    pos= vector(R*sin(thetao), -R, 0),
    color=color.red,
    radius=RodWidth,
    axis = vector(0, 2, 0),
    opacity =0.6)
HorizontalRod = cylinder(
    pos=vector(-R, R*cos(thetao), 0),
    color=color.red,
    radius=RodWidth,
    axis = vector(2, 0, 0),
    opacity = 0.6)

Dot = sphere(
    pos=vector(R*sin(thetao), R*cos(thetao), 0),
    color=color.yellow,
    radius=SphereRadius,
    opacity =0.5)

Trace = curve(color=color.yellow)
scene.autoscale=False # prevents automatic rescaling of
# display window
# Keep doing this indefinitely
while True :
    rate(100) # limits speed to 100 frames / sec
    time = time + dt
    #calculate x and y with respect to time.
    x = R*sin(omega*time)
    y = R*cos(omega*time)
    #update positions of objects .B.0 VPython Coordinates 171
    VerticalRod.pos.x = x
    HorizontalRod.pos.y = y
    Dot.pos = vector(x, y, 0)
    # and the trace also
    Trace.append(Dot.pos)