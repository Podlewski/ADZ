from sklearn import svm

from classifiers.classifier import Classifier


class SVM(Classifier):
    """Klasa maszyny wektorów nośnych"""

    def __init__(self, data, labels, training_set_ratio, kernel, regulation):
        super().__init__(data, labels, training_set_ratio)
        self.name = 'Maszyna wektorów nośnych'
        self.short_name = 'Svm'
        self.params_string = f'({kernel}, {str(regulation).replace(".", ",")})'
        self.model = svm.SVC(C=regulation, kernel=kernel)
