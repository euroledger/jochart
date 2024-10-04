import random
import time

from draw import turtle_init, turtle_close, line, turtle_on_click, turtle_mainloop, ellipse, \
    turn_on_tracer, turtle_update, turtle_clear, set_coordinates, axis, plotter

list_of_points = []


MY_WIDTH=20
MY_HEIGHT=15
def setup():
    turtle_init()
    set_coordinates(MY_WIDTH, MY_HEIGHT)

    axis(MY_WIDTH, 1)
    axis(MY_HEIGHT, 1, 90)

    plotter(range(-MY_WIDTH // 2, MY_WIDTH // 2))


setup()


# draw()


turtle_close()
