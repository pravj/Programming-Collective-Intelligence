"""
Tanimoto Score

Tanimoto scoring is used for comparing vectors having discrete or specifically binary values.
It is being used for item-item recommendation systems mostly. It's also considered similar to Jaccard Index.
"""

"""
Sample discrete data for item selection by users
1 -> liked and 0 -> not liked
"""
data = {'Bob': {'a': 0, 'b': 0, 'c': 1, 'd': 0}, 'Jack': {'a': 1, 'b': 1, 'c': 0, 'd': 1}, 'Sam': {'a': 1, 'b': 1, 'c': 1, 'd': 0}}

"""
Tanimoto score function
"""
def score(item_a, item_b):
    item_a_count, item_b_count, common_count = 0, 0, 0

    for person in data:
        item_a_count += data[person][item_a]
        item_b_count += data[person][item_b]

        if data[person][item_a] == data[person][item_b] == 1:
            common_count += 1

    return (common_count * 1.0)/(item_a_count + item_b_count - common_count)

"""
Return ranked list of similar items for the item
"""
def rank(item):
    items = ['a', 'b', 'c', 'd']

    similar = [(score(item, item_), item_) for item_ in items if item_ != item]
    similar.sort()
    similar.reverse()

    return similar
