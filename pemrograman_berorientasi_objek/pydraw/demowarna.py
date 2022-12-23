from pydraw import *

class Color:
    def __init__(self, hue, lum=50, sat=100):
        self.hue = hue
        self.lum = lum
        self.sat = sat
    def __repr__(self):
        return hls(self.hue, self.lum, self.sat)
    def __add__(self, other):
        if (isinstance(other, Color)):
            r1, g1, b1 = hls2rgb(self.hue, self.lum, self.sat)
            r2, g2, b2 = hls2rgb(other.hue, other.lum, other.sat)
            r = min(255, r1 + r2)
            g = min(255, g1 + g2)
            b = min(255, b1 + b2)
            print(r, g, b)
            return Color(*rgb2hls(r, g, b))
        else:
            return other + self
    def __radd__(self, other):
        return Color(self.hue, self.lum + other, self.sat)
    def __sub__(self, other):
        if (isinstance(other, Color)):
            r1, g1, b1 = hls2rgb(self.hue, self.lum, self.sat)
            r2, g2, b2 = hls2rgb(other.hue, other.lum, other.sat)
            r = max(0, r1 - r2)
            g = max(0, g1 - g2)
            b = max(0, b1 - b2)
            print(r, g, b)
            return Color(*rgb2hls(r, g, b))
        else:
            return other + self
    def __rsub__(self, other):
        return Color(self.hue, self.lum - other, self.sat)
    def __rshift__(self, other):
        return other >> self
    def __rrshift__(self, other):
        hue = (self.hue + other) % 360
        return Color(hue, self.lum, self.sat)

# rect(-500, -500, 0, 0, rgb(255, 0, 0), True)

# m = Color(120)
# g = Color(240)
# clear(str(m + 25))

clear(rgb(255, 255, 255))

c = Color(0)
for x in range(0, 400):
    line(x, 0, x, -400, str(c))
    c = c >> 1

# bgcolor = hls(0, 25, 100)
# fgcolor = hls(0, 50, 100)
# origin(200, 200)
# clear(bgcolor)
# circle(0, 0, 100, fgcolor, True)