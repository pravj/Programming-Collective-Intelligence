def score(data, tag_a, tag_b):
    set_a = set(data[tag_a])
    set_b = set(data[tag_b])

    num = set_a.intersection(set_b)
    den = set_a.union(set_b)

    return (len(num) * 1.0) / len(den)

def rank(data, tag):
    scores = [(score(data, tag, tag_), tag_) for tag_ in data if tag_ != tag]
    scores.sort()
    scores.reverse()

    return scores
