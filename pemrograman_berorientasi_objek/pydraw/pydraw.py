from PIL import Image, ImageDraw
from math import sqrt, cos, sin, tan, pi
from colorsys import hls_to_rgb, rgb_to_hls

class __PyDraw:
    def version(self):
        return '0.7.0'

    def __create_image(self, width, height, bgcolor):
        self.__img = Image.new('RGBA', (width, height), bgcolor)
        self.__draw = ImageDraw.Draw(self.__img)

    def __init__(self, width = 400, height = 400, bgcolor = (255, 255, 255, 0)):
        self.__x = 0
        self.__y = 0
        self.__width = width
        self.__height = height
        self.__bgcolor = bgcolor
        self.__create_image(width, height, bgcolor)

    def origin(self, x, y):
        self.__x = x
        self.__y = y

    def resize(self, width, height = None):
        self.__width = width
        self.__height = width if height is None else height
        self.__create_image(width, self.__height, self.__bgcolor)

    def clear(self, bgcolor = None):
        if bgcolor is None:
            bgcolor = self.__bgcolor
        else:
            self.__bgcolor = bgcolor
        self.__create_image(self.__width, self.__height, bgcolor)

    def point(self, x, y, color, size = 1):
        x = self.__x + x
        y = self.__y - y
        if size < 1:
            return
        elif size == 1:
            self.__draw.point([(x, y)], color)
        else:
            r = size / 2
            tl = (x - r, y - r)
            br = (x + r, y + r)
            self.__draw.ellipse([tl, br], color, color)

    def line(self, x1, y1, x2, y2, color, width = 1):
        x1 = self.__x + x1
        y1 = self.__y - y1
        x2 = self.__x + x2
        y2 = self.__y - y2
        self.__draw.line([x1, y1, x2, y2], color, width)

    def rect(self, x1, y1, x2, y2, color, is_filled = False, width = 1):
        x1 = self.__x + x1
        y1 = self.__y - y1
        x2 = self.__x + x2
        y2 = self.__y - y2
        fill = color if is_filled else None
        self.__draw.rectangle([x1, y1, x2, y2], fill, color, width)

    def circle(self, x, y, radius, color, is_filled = False, width = 1):
        x = self.__x + x
        y = self.__y - y
        tl = (x - radius, y - radius)
        br = (x + radius, y + radius)
        fill = color if is_filled else None
        self.__draw.ellipse([tl, br], fill=fill, outline=color, width=width)

    def ellipse(self, x, y, rx, ry, color, is_filled = False, width = 1):
        x = self.__x + x
        y = self.__y - y
        tl = (x - rx, y - ry)
        br = (x + rx, y + ry)
        fill = color if is_filled else None
        self.__draw.ellipse([tl, br], fill, color, width)

    def arc(self, x, y, rx, ry, start, end, color, width = 1):
        x = self.__x + x
        y = self.__y - y
        tl = (x - rx, y - ry)
        br = (x + rx, y + ry)
        self.__draw.arc([tl, br], -end, -start, color, width)

    def pie(self, x, y, rx, ry, start, end, color, is_filled = False, width = 1):
        x = self.__x + x
        y = self.__y - y
        tl = (x - rx, y - ry)
        br = (x + rx, y + ry)
        fill = color if is_filled else None
        self.__draw.pieslice([tl, br], -end, -start, fill, color, width)

    def polygon(self, x, y, r, side, color, is_filled = False, width = 1):
        x = self.__x + x
        y = self.__y - y
        fill = color if is_filled else None
        if is_filled or width == 1:
            rotate = 0 if side % 2 else 180 / side
            self.__draw.regular_polygon((x, y, r), side, rotate, fill, color)
        if width > 1:
            angle = 2 * pi / side
            xy = []
            for i in range(side):
                xy.append((
                    x + r * cos(i * angle - pi / 2),
                    y + r * sin(i * angle - pi / 2),
                ))
            xy.append((
                x + r * cos(-pi / 2),
                y + r * sin(-pi / 2),
            ))
            xy.append((
                x + r * (cos(-pi / 2) + cos(angle - pi / 2)) / 2,
                y + r * (sin(-pi / 2) + sin(angle - pi / 2)) / 2,
            ))
            self.__draw.line(xy, color, width, 'curve')

    def polygram(self, x, y, r, point, density, color, width = 1):
        x = self.__x + x
        y = self.__y - y
        angle = 2 * pi / point
        xy = []
        for i in range(point):
            xy.append((
                x + r * cos(i * angle - pi / 2),
                y + r * sin(i * angle - pi / 2),
            ))
        lines = 0
        groups = []
        start = 0
        while lines < point:
            a = start
            group = []
            while True:
                b = (a + density) % point
                group.append(xy[a])
                group.append(xy[b])
                lines += 1
                a = b
                if a == start: break
            group.append(xy[a])
            b = (a + density) % point
            group.append((
                (xy[a][0] + xy[b][0]) / 2,
                (xy[a][1] + xy[b][1]) / 2,
            ))
            groups.append(group)
            start += 1
        for group in groups:
            self.__draw.line(group, color, width, 'curve')

    def star(self, x, y, r, point, color, is_filled = False, width = 1, acuteness = None):
        if acuteness is None:
            acuteness = 2 / 3
        x = self.__x + x
        y = self.__y - y
        angle = 2 * pi / point
        t = r * cos(angle / 2)
        outer = angle + (pi - angle) * (1 - acuteness)
        base = 2 * r * sin(angle / 2)
        t = t - 0.5 * base / tan(outer / 2)
        xy = []
        for i in range(point):
            xy.append((
                x + r * cos(i * angle - pi / 2),
                y + r * sin(i * angle - pi / 2),
            ))
            xy.append((
                x + t * cos((i + 0.5) * angle - pi / 2),
                y + t * sin((i + 0.5) * angle - pi / 2),
            ))
        if is_filled:
            self.__draw.polygon(xy, color, None)
        xy.append((
            x + r * cos(-pi / 2),
            y + r * sin(-pi / 2),
        ))
        xy.append((
            x + (r * cos(-pi / 2) + t * cos(0.5 * angle - pi / 2)) / 2,
            y + (r * sin(-pi / 2) + t * sin(0.5 * angle - pi / 2)) / 2,
        ))
        self.__draw.line(xy, color, width, 'curve')

    def bezier(self, points, color, width = 1, smoothness = 100):
        length = 0
        for i in range(len(points) - 1):
            a, b = points[i], points[i + 1]
            dx, dy = b[0] - a[0], b[1] - a[1]
            length += sqrt(dx ** 2 + dy ** 2)
        length = round(length * smoothness / 100)
        xy = []
        for z in range(length):
            t = z / length
            q = [points]
            for i in range(len(points)):
                if not i: continue
                q.append([])
                a, b = q[i - 1], q[i]
                for j in range(len(a) - 1):
                    c, d = a[j], a[j + 1]
                    b.append((
                        (1 - t) * c[0] + t * d[0],
                        (1 - t) * c[1] + t * d[1],
                    ))
            x, y = q[i][0][0], q[i][0][1]
            xy.append((self.__x + x, self.__y - y))
        x, y = points[-1][0], points[-1][1]
        xy.append((self.__x + x, self.__y - y))
        self.__draw.line(xy, color, width, 'curve')

    def show(self):
        # self.__img.save('result.png')
        self.__img.show()

__pydraw = __PyDraw()
__pydraw.resize(400, 400)

def origin(x, y):
    __pydraw.origin(x, y)

def resize(width, height = None):
    __pydraw.resize(width, height)

def clear(bgcolor = None):
    __pydraw.clear(bgcolor)

def point(x, y, color, size = 1):
    __pydraw.point(x, y, color, size)

def line(x1, y1, x2, y2, color, width = 1):
    __pydraw.line(x1, y1, x2, y2, color, width)

def rect(x1, y1, x2, y2, color, is_filled = False, width = 1):
    __pydraw.rect(x1, y1, x2, y2, color, is_filled, width)

def circle(x, y, radius, color, is_filled = False, width = 1):
    __pydraw.circle(x, y, radius, color, is_filled, width)

def ellipse(x, y, rx, ry, color, is_filled = False, width = 1):
    __pydraw.ellipse(x, y, rx, ry, color, is_filled, width)

def arc(x, y, rx, ry, start, end, color, width = 1):
    __pydraw.arc(x, y, rx, ry, start, end, color, width)

def pie(x, y, rx, ry, start, end, color, is_filled = False, width = 1):
    __pydraw.pie(x, y, rx, ry, start, end, color, is_filled, width)

def polygon(x, y, r, side, color, is_filled = False, width = 1):
    __pydraw.polygon(x, y, r, side, color, is_filled, width)

def polygram(x, y, r, point, density, color, width = 1):
    __pydraw.polygram(x, y, r, point, density, color, width)

def star(x, y, r, point, color, is_filled = False, width = 1, acuteness = None):
    __pydraw.star(x, y, r, point, color, is_filled, width, acuteness)

def bezier(points, color, width = 1, smoothness = 100):
    __pydraw.bezier(points, color, width, smoothness)

def hls2rgb(h, l, s):
    r, g, b = hls_to_rgb(h / 360, l / 100, s / 100)
    return (255 * r, 255 * g, 255 * b)

def hsl2rgb(h, s, l):
    return hls2rgb(h, l, s)

def rgb2hls(r, g, b):
    h, l, s = rgb_to_hls(r / 255, g / 255, b / 255)
    return (360 * h, 100 * l, 100 * s)

def rgb2hsl(r, g, b):
    h, l, s = rgb2hls(r, g, b)
    return (h, s, l)

def rgb(r, g, b, a = 100):
    return '#{:02x}{:02x}{:02x}{:02x}'.format(
        int(r), int(g), int(b), int(255 * a / 100))

def hls(h, l, s, a = 100):
    r, g, b = hls2rgb(h, l, s)
    return rgb(r, g, b, a)

def hsl(h, s, l, a = 100):
    return hls(h, l, s, a)

def __show():
    __pydraw.show()

import atexit
atexit.register(__show)