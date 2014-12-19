import matplotlib.pyplot as plt


class Plotter:

    def __init__(self, k):
        self.k = k
        self.clusters = None

        self.initialize()

    def initialize(self):
        self.clusters = [None for i in range(self.k)]

    def add_data(self, data, index):
        x_data = []
        y_data = []

        for i in range(len(data)):
            x_data.append(data[i][0])
            y_data.append(data[i][1])

        self.clusters[index] = [x_data, y_data]

        if (index == (self.k - 1)):
            self.draw()

    def draw(self):
        c = self.clusters

        cen_x = [sum(c[0][0]) / len(c[0][0]), sum(c[1][0]) / len(c[1][0]), sum(c[2][0]) / len(c[2][0])]
        cen_y = [sum(c[0][1]) / len(c[0][1]), sum(c[1][1]) / len(c[1][1]), sum(c[2][1]) / len(c[2][1])]

        plt.plot(c[0][0], c[0][1], 'ro', c[1][0], c[1][1], 'bs', c[2][0], c[2][1], 'g^', cen_x, cen_y, 'r--')

        plt.ylabel('Population (x 10^8)')
        plt.xlabel('Area (x 10^6)')

        plt.show()
