from dataset import Dataset
from scoring import score, rank

dataset = Dataset()

# number of bookmarks in the dataset; please choose an integer multiple of 100.
dataset.limit = 500

dataset.collector()

# prints list containing similar tags to python, ordered by their similarity score.
print rank(dataset.data, 'python')[:20]
