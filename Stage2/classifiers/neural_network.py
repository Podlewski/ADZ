from sklearn import neural_network as nn

from classifiers.classifier import Classifier


class NeuralNetwork(Classifier):

    def __init__(self, data, labels, training_set_ratio, n_of_hidden_layer, max_iter):
        super().__init__(data, labels, training_set_ratio)
        self.name = 'Algorytm sieci neuronowych'
        self.short_name = 'MLP'
        self.params_string = f'({n_of_hidden_layer}, {max_iter})'
        self.model = nn.MLPClassifier(alpha=0.0001,
                                      hidden_layer_sizes=(n_of_hidden_layer, 10),
                                      max_iter=max_iter)
