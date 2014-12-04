"""
scoring.py
----------

This module implements methods that help in the similarity scoring.
"""


def score(data, tag_a, tag_b):
    """ This method returns the similarity score between two tags
    based on 'Jaccard Index' method.

    param: data(dict): 'tag' based bookmarks data
    param: tag_a(string): a tag to compare
    param: tag_b(string): another tag to compare with
    """

    set_a = set(data[tag_a])
    set_b = set(data[tag_b])

    num = set_a.intersection(set_b)
    den = set_a.union(set_b)

    return (len(num) * 1.0) / len(den)


def rank(data, tag):
    """ This method returns tags ordered by similarity scores with respect to
    the 'tag'.

    param: data(dict): 'tag' based bookmarks data
    param: tag(string): the tag, whose similar tags we're searching for
    """

    scores = [(score(data, tag, tag_), tag_) for tag_ in data if tag_ != tag]
    scores.sort()
    scores.reverse()

    return scores
