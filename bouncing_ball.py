from vpython import *

ball = sphere(pos=vector(0, 0, 0), color=color.red, radius=0.2, opacity=0.6)
side = 10
thk = 0.2
s2 = 2 * side - thk
s3 = 2 * side + thk


wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color=color.gray(0.7))

ball.mass = 1.0
ball.p = vector(1, 0, 0)
g = vector(0, 0, -10)
dt = 0.00003
time = 0.0
scene.autoscale = False

side = side - thk * 0.5 - ball.radius

while True:
    rate(100)
    time = time + dt
    ball.p.z = ball.mass * ((ball.p.z / ball.mass) + g.z * time)
    ball.pos.z = ball.pos.z + (ball.p.z / ball.mass) * time
    ball.pos.x = ball.pos.x + ball.p.x * time
    if ball.pos.z < -side:
        ball.p.z = -ball.p.z
