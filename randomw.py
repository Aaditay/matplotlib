from random import choice


class RandomWalk:
    def __init__(self, points):
        self.num = points
        self.x_ = [0]
        self.y_ = [0]


    def generate(self):
        x_ = []
        y_ = []
        for i in range(self.num):
            x_value = choice(list(range(-40, 40)))
            y_value = choice(list(range(-40, 40)))
            dist_x = self.x_[-1] + x_value
            dist_y = self.y_[-1] + y_value

            self.x_.append(dist_x)
            self.y_.append(dist_y)

