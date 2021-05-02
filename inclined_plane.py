from vpython import *


hight = 5

g = vector(0, 0, -10)

theta = pi / 3

longest = box(
    pos=vector(0, 0, 0), size=vector(0.3, hight, hight * sin(theta)), color=color.red
)

longest.rotate(angle=pi / 3, axis=vector(0, 0, 1))

ball = sphere(
    pos=vector(0, hight, hight * sin(theta)),
    color=color.red,
    radius=0.3,
    opacity=0.6,
    make_trail=True,
    retain=200,
)
