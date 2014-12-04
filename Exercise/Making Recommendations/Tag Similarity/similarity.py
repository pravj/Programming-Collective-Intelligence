from dataset import Dataset
from scoring import score, rank

dataset = Dataset()
dataset.collector()

print rank(dataset.data, 'programming')
