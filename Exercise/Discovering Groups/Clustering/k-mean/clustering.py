import json
from math import ceil
from random import random


class Cluster:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = []

    def relocate(self):
        num_points = len(self.points)
        x_sum = y_sum = 0

        for i in range(num_points):
            x_sum += self.points[i][0]
            y_sum += self.points[i][1]

        self.x = x_sum / num_points
        self.y = y_sum / num_points


class KMean:

    def __init__(self, k, limit_x, limit_y):
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
        with open('data.json') as f:
            self.data = json.loads(f.read())

        for i in range(self.data):
            self.elements.append([self.data[i]['area'], self.data[i]['population']])

    def decide_limit(self):
        for i in range(self.data):
            if (self.elements[i][0] > self.limit_x):
                self.limit_x = self.elements[i][0]

            if (self.elements[i][1] > self.limit_y):
                self.limit_y = self.elements[i][1]

        self.limit_x = ceil(self.limit_x)
        self.limit_y = ceil(self.limit_y)

    def initialize(self):
        self.clusters = [Cluster(random() * self.limit_x, random() * self.limit_y) for i in range(self.k)]
