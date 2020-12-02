from sklearn import naive_bayes

from classifiers.classifier import Classifier


class Bayes(Classifier):
    """Klasa nainwego klasyfikatora Bayesa"""

    def __init__(self, data, labels, training_set_ratio):
        super().__init__(data, labels, training_set_ratio)
        self.name = 'Naiwny klasyfikator Bayesa'
        self.short_name = 'Bayes'
        self.model = naive_bayes.GaussianNB()
