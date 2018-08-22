from __future__ import print_function


class Obstacle:
    def __init__(self, x, y, l, w):
        self.x = x
        self.y = y
        self.length = l
        self.width = w

    def draw(self, bd):
        for i in range(self.length):
            for j in range(self.width):
                bd.buff[self.x+i][self.y+j] = ' '


class Clouds(Obstacle):
    def __init__(self, x, y, l, w):
        Obstacle.__init__(self, x, y, l, w)

    def draw(self, bd):
        bd.buff[self.x][self.y] = " "
        bd.buff[self.x][self.y+1] = "c"
        bd.buff[self.x][self.y+2] = "c"
        bd.buff[self.x][self.y+3] = " "
        bd.buff[self.x+1][self.y] = "c"
        bd.buff[self.x+1][self.y+1] = "c"
        bd.buff[self.x+1][self.y+2] = "c"
        bd.buff[self.x+1][self.y+3] = "c"
        bd.buff[self.x+2][self.y] = " "
        bd.buff[self.x+2][self.y+1] = "c"
        bd.buff[self.x+2][self.y+2] = "c"
        bd.buff[self.x+2][self.y+3] = " "


class Hills(Obstacle):
    def __init__(self, x, y, l, w, size):
        Obstacle.__init__(self, x, y, l, w)
        self.size = size

    def draw(self, bd):
        if (self.size == 1):
            bd.buff[self.x][self.y+3] = "/"
            bd.buff[self.x][self.y+4] = "\\"
            bd.buff[self.x+1][self.y+2] = "/"
            bd.buff[self.x+1][self.y+5] = "\\"
            bd.buff[self.x+2][self.y+1] = "/"
            bd.buff[self.x+2][self.y+6] = "\\"
            bd.buff[self.x+3][self.y] = "/"
            bd.buff[self.x+3][self.y+7] = "\\"
        else:
            bd.buff[self.x][self.y+5] = "/"
            bd.buff[self.x][self.y+6] = "\\"
            bd.buff[self.x+1][self.y+4] = "/"
            bd.buff[self.x+1][self.y+7] = "\\"
            bd.buff[self.x+2][self.y+3] = "/"
            bd.buff[self.x+2][self.y+8] = "\\"
            bd.buff[self.x+3][self.y+2] = "/"
            bd.buff[self.x+3][self.y+9] = "\\"
            bd.buff[self.x+4][self.y+1] = "/"
            bd.buff[self.x+4][self.y+10] = "\\"
            bd.buff[self.x+5][self.y] = "/"
            bd.buff[self.x+5][self.y+11] = "\\"


class Bricks(Obstacle):
    def __init__(self, x, y, l, w):
        Obstacle.__init__(self, x, y, l, w)

    def draw(self, bd):
        for i in range(self.length):
            for j in range(self.width):
                bd.buff[self.x + i][self.y + j] = "X"


class Pipe(Obstacle):
    def __init__(self, x, y, l, w):
        Obstacle.__init__(self, x, y, l, w)

    def draw(self, bd):
        for i in range(self.length):
            for j in range(self.width):
                bd.buff[self.x + i][self.y + j] = "-"
        for i in range(self.length):
            bd.buff[self.x+i][self.y] = "|"
            bd.buff[self.x+i][self.y+self.width] = "|"


class Coins(Obstacle):
    def __init__(self, x, y, l, w):
        Obstacle.__init__(self, x, y, l, w)

    def draw(self, bd):
        bd.buff[self.x][self.y] = "$"
        bd.buff[self.x][self.y+1] = "$"
