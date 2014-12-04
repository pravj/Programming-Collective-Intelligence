"""
dataset.py
----------

This module implements methods to collect the required dataset.
"""

import requests


class Dataset:

    def __init__(self):

        # number of bookmarks in the dataset; please choose an integer multiple of 100.
        self.limit = None

        # base API url that gives 100 bookmarks results for a particular page
        self.api_url = 'https://bookie.io/api/v1/bmarks?count=100&page='

        # dictionary representing the bookmarks dataset; tags mapped to posts.
        self.data = {}

    def collect(self, page):
        """ This method returns json response data for a particular page.

        param: page(int): page number
        """

        try:
            response = requests.get("%s%d" % (self.api_url, page))
        except:
            print 'Error in data collection'

        return response.json()

    def transform(self, data):
        """ This method forms a 'tag' based dictionary from 'post' based
        dictionary data.

        param: data(dict): json object representing the bookmarks data
        """

        bmarks = data['bmarks']

        for bmark in bmarks:
            tags = bmark['tags']

            if len(tags) != 0:
                for tag in tags:
                    if tag['name'] in self.data:
                        self.data[tag['name']].append(bmark['url'])
                    else:
                        self.data[tag['name']] = [bmark['url']]

    def collector(self):
        """ This method collects and transforms json data for all the pages until
        the total tag elements are less then limit.
        """

        for i in range(self.limit / 100):
            data = self.collect(i + 1)
            self.transform(data)
