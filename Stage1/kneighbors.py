import warnings
from numpy import unique
from sklearn import metrics, neighbors


class KNeighbors:
    """Klasyfikator k najbliższych sąsiadów"""
    model = None
    unique_labels = None
    training_data = None
    training_labels = None
    test_data = None
    test_labels = None
    prediction = None

    def __init__(self, data, labels, training_set_ratio, neighbors_number=5):
        """
        Przyjmuje dane, etykiety, procent podziału zbioru na część
        treningową oraz testową, a także liczbę najbliższych sąsiadów
        (domyślnie 5)
        """
        self.model = neighbors.KNeighborsClassifier(neighbors_number)
        self.unique_labels = unique(labels)
        partition_index = int(len(data.index) * training_set_ratio)
        self.training_data = data.iloc[:partition_index].values
        self.training_labels = labels.iloc[:partition_index].values.ravel()
        self.test_data = data.iloc[partition_index:].values
        self.test_labels = labels.iloc[partition_index:].values.ravel()

    def train(self):
        """Trenuje klasyfikator na zbiorze treningowym"""
        self.model.fit(self.training_data, self.training_labels)

    def test(self):
        """Dokonuje predykcji na zbiorze testowym"""
        self.prediction = self.model.predict(self.test_data)

    def get_accuracy(self):
        """Oblicza poprawność klasyfikacji"""
        return metrics.accuracy_score(self.test_labels, self.prediction)

    def get_prediction_table(self):
        """
        Zwraca tablicę zawierającą informację o poprawności przypisania
        klasy do danej próbki
        """
        prediction_table = []
        for i in range(len(self.prediction)):
            prediction_table.append(self.prediction[i] == self.test_labels[i])
        return prediction_table
