"""
plotter.py
----------

This module implements Plotter class.
Which helps drawing resultant image from result data.
"""

import matplotlib.pyplot as plt


class Plotter:

    def __init__(self, k):
        self.k = k
        self.clusters = None

        self.initialize()

    def initialize(self):
        """ Initialize data content for each clusters.
        """

        self.clusters = [None for i in range(self.k)]

    def add_data(self, data, index):
        """ Add points data for each cluster.
        according to the index provided.
        """

        x_data = []
        y_data = []
        name_data = []

        for i in range(len(data)):
            x_data.append(data[i][0])
            y_data.append(data[i][1])
            name_data.append(data[i][2])

        print "Cluster - %d" %(index)
        for country in name_data:
            print country

        self.clusters[index] = [x_data, y_data]

        # draw the resultant image when all the cluster data is available.
        if (index == (self.k - 1)):
            self.draw()

    def draw(self):
        """ Draw the resultant cluster image.
        """

        c = self.clusters

        # list representing co-ordinates of cluster centroids.
        # X and Y co-ordinates respectively.
        cen_x = [sum(c[0][0]) / len(c[0][0]), sum(c[1][0]) / len(c[1][0]), sum(c[2][0]) / len(c[2][0])]
        cen_y = [sum(c[0][1]) / len(c[0][1]), sum(c[1][1]) / len(c[1][1]), sum(c[2][1]) / len(c[2][1])]

        # plot all the clusters and the centroids also
        plt.plot(c[0][0], c[0][1], 'ro', c[1][0], c[1][1], 'bs', c[2][0], c[2][1], 'g^', cen_x, cen_y, 'r--')

        plt.ylabel('Population (x10^8 People)')
        plt.xlabel('Area (x 10^6 KM^2)')

        plt.show()
