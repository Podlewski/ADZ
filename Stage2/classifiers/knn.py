from sklearn import neighbors

from classifiers.classifier import Classifier


class KNN(Classifier):
    """Klasyfikator k najbliższych sąsiadów"""

    def __init__(self, data, labels, training_set_ratio, neighbors_number=5):
        super().__init__(data, labels, training_set_ratio)
        self.name = 'k najbliższych sąsiadów'
        self.short_name = 'Knn'
        self.model = neighbors.KNeighborsClassifier(neighbors_number)
