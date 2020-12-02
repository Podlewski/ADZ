from sklearn import tree

from classifiers.classifier import Classifier


class DecisionTree(Classifier):
    """Klasa drzewa decyzyjnego"""

    def __init__(self, data, labels, training_set_ratio):
        super().__init__(data, labels, training_set_ratio)
        self.name = 'Drzewo decyzyjne'
        self.short_name = 'Tree'
        self.model = tree.DecisionTreeClassifier()
