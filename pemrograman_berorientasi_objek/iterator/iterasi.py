import pydraw

# pydraw.show_at_exit = False

# iterator
class ColorWheel:
    def __init__(self, start_hue=0, step=1):
        self.hue = start_hue
        self.step = step
    def __iter__(self):
        """digunakan untuk menghasilkan objek iteratornya"""
        return self
    def __next__(self):
        hue = self.hue
        self.hue += self.step
        if self.hue >= 360: self.hue -= 360
        if self.hue < 0: self.hue = 360 + self.hue
        return pydraw.hls(hue, 50, 100)

# generator
def color_wheel(start_hue=0, step=1):
    hue = start_hue
    while True:
        yield pydraw.hls(hue, 50, 100)
        hue += step
        if hue >= 360: hue -= 360
        if hue < 0: hue = 360 - hue

# run app untuk iterator
"""
r = 200
for color in ColorWheel(0, 10):
    pydraw.circle(200, -200, r, color, True)
    r -= 1
    if r <= 0: break
"""
"""
it = ColorWheel(0, 2)
for r in reversed(range(200)):
    color = next(it)
    pydraw.circle(200, -200, r + 1, color, True)
"""
# run app untuk generator
color_wheel()

"""
it = ColorWheel()
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
"""
