from pydraw import \
    clear, resize, origin, point, line, rect, circle, ellipse, arc, pie, polygon, polygram, star

resize(800, 600)
origin(400,300)
clear('yellow')


# point(0, 0, 'red', 10)
# line(0, 0, 400, -300, 'blue')
# rect(-100, 100, 100, -100, 'green', False, 10)
# circle(0, 0, 200, 'magenta', False, 10)


# ellipse(0, 0, 300, 200, 'navy', False, 10)


# pie(0, 0, 400, 300, 45, -45, 'black', 10)
# polygon(0, 0, 200, 5, 'white', True)
# polygram(0, 0, 200, 10, 4, 'green')

polygram(0, 0, 200, 7, 3, 'green')

star(0, 0, 200, 7, 'red', True)
