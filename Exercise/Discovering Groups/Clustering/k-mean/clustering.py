import json
from math import ceil, sqrt
from random import random
from plotter import Plotter


ITERATION_LIMIT = 20

class Cluster:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = []

    def relocate(self, iteration):
        num_points = len(self.points)
        x_sum = y_sum = 0

        for i in range(num_points):
            x_sum += self.points[i][0]
            y_sum += self.points[i][1]

        self.x = x_sum / num_points
        self.y = y_sum / num_points

        self.points = []


class KMean:

    def __init__(self, k):
        self.plotter = Plotter(k)

        self.k = k
        self.clusters = None

        self.data = None
        self.elements = []

        self.limit_x = 0
        self.limit_y = 0

        self.load_data()
        self.decide_limit()
        self.initialize()

    def load_data(self):
        with open('dataset.json') as f:
            self.data = json.loads(f.read())

        for i in range(len(self.data)):
            self.elements.append([(self.data[i]['area']) / 1000000, (self.data[i]['population']) / 100000000, self.data[i]['name']])

    def decide_limit(self):
        for i in range(len(self.data)):
            if (self.elements[i][0] > self.limit_x):
                self.limit_x = self.elements[i][0]

            if (self.elements[i][1] > self.limit_y):
                self.limit_y = self.elements[i][1]

        self.limit_x = ceil(self.limit_x)
        self.limit_y = ceil(self.limit_y)

    def initialize(self):
        self.clusters = [Cluster(random() * self.limit_x, random() * self.limit_y) for i in range(self.k)]

    def distance(self, a, b):
        return sqrt(((a[0] - b[0]) * (a[0] - b[0])) + ((a[1] - b[1]) * (a[1] - b[1])))

    def process(self):
        for i in range(ITERATION_LIMIT):

            for j in range(len(self.elements)):
                min_dist = self.distance(self.elements[j], [self.clusters[0].x, self.clusters[0].y])
                c = 0

                for k in range(1, self.k):
                    if (self.distance(self.elements[j], [self.clusters[k].x, self.clusters[k].y]) <= min_dist):
                        min_dist = self.distance(self.elements[j], [self.clusters[k].x, self.clusters[k].y])
                        c = k

                self.clusters[c].points.append(self.elements[j])

            if (i == (ITERATION_LIMIT - 1)):
                for l in range(self.k):
                    self.plotter.add_data(self.clusters[l].points, l)
            else:
                for m in range(self.k):
                    self.clusters[m].relocate(i)
