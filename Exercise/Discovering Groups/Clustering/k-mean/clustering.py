"""
clustering.py

This module implements Cluster and KMean classes.
Which helps processing the K-mean clustering algorithm.
"""


import json
from math import ceil, sqrt
from random import random
from plotter import Plotter

# constant representing max iterations
ITERATION_LIMIT = 20


class Cluster:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = []

    def relocate(self, iteration):
        """ Relocate the centroid of a cluster after an iteration.
        According to mean(center) of all points under the cluster.
        """

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
        """ Load the dataset file.
        """

        with open('dataset.json') as f:
            self.data = json.loads(f.read())

        # lowers the value of x, y axis data points.
        for i in range(len(self.data)):
            self.elements.append([(self.data[i]['area']) / 1000000, (self.data[i]['population']) / 100000000, self.data[i]['name']])

    def decide_limit(self):
        """ Find the limiting(maximum) values on each axis.
        """

        for i in range(len(self.data)):
            if (self.elements[i][0] > self.limit_x):
                self.limit_x = self.elements[i][0]

            if (self.elements[i][1] > self.limit_y):
                self.limit_y = self.elements[i][1]

        self.limit_x = ceil(self.limit_x)
        self.limit_y = ceil(self.limit_y)

    def initialize(self):
        """ Put all the cluster randomly but under the limits.
        According to the calculated limiting values for each axis.
        """

        self.clusters = [Cluster(random() * self.limit_x, random() * self.limit_y) for i in range(self.k)]

    def distance(self, a, b):
        """ Calculates the euclidean distance between two points.
        """

        return sqrt(((a[0] - b[0]) * (a[0] - b[0])) + ((a[1] - b[1]) * (a[1] - b[1])))

    def process(self):
        """ Work according to the K-mean algorithm.
        """

        for i in range(ITERATION_LIMIT):

            # put each point to its nearest cluster
            for j in range(len(self.elements)):
                min_dist = self.distance(self.elements[j], [self.clusters[0].x, self.clusters[0].y])
                c = 0

                for k in range(1, self.k):
                    if (self.distance(self.elements[j], [self.clusters[k].x, self.clusters[k].y]) <= min_dist):
                        min_dist = self.distance(self.elements[j], [self.clusters[k].x, self.clusters[k].y])
                        c = k

                self.clusters[c].points.append(self.elements[j])

            # relocates the clusters according to its points.
            # OR terminate the process when all the iterations are done.
            if (i == (ITERATION_LIMIT - 1)):
                for l in range(self.k):
                    self.plotter.add_data(self.clusters[l].points, l)
            else:
                for m in range(self.k):
                    self.clusters[m].relocate(i)
