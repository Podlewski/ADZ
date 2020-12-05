from abc import ABCMeta
from numpy import unique
from sklearn import metrics


class Classifier(metaclass=ABCMeta):
    """Klasa klasyfikatora"""

    def __init__(self, data, labels, training_set_ratio):
        """
        Przyjmuje dane, etykiety, procent podziału zbioru na część
        treningową oraz testową, a także liczbę najbliższych sąsiadów
        (domyślnie 5)
        """

        self.name = None
        self.short_name = None
        self.params_string = None
        self.model = None
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

    def get_matrix(self):
        return metrics.confusion_matrix(self.test_labels, self.prediction)

    def get_accuracy(self):
        """Oblicza dokładność klasyfikacji"""
        return metrics.accuracy_score(self.test_labels, self.prediction)

    def get_precision(self):
        """Oblicza precyzję klasyfikacji"""
        return metrics.precision_score(self.test_labels, self.prediction,
                                       pos_label='Yes')

    def get_sensitivity(self):
        """Oblicza czułości klasyfikacji"""
        return metrics.recall_score(self.test_labels, self.prediction,
                                    pos_label='Yes')

    def get_specificity(self):
        """Oblicza specyficzności klasyfikacji"""
        return metrics.recall_score(self.test_labels, self.prediction,
                                    pos_label='No')

    def get_accuracy_range(self, start_index=0, end_index=0):
        """
        Oblicza poprawność dla podanego zakresu. Kiedy indeksy nie zostaną
        podane bierze odpiwiednio początek i koniec zakresu
        """
        if end_index == 0:
            end_index = len(self.prediction)

        return metrics.accuracy_score(
            self.test_labels[start_index:end_index],
            self.prediction[start_index:end_index])

    def get_accuracy_table(self):
        """
        Zwraca tablicę zawierającą informację o poprawności przypisania
        klasy do danej próbki
        """
        prediction_table = []
        for i in range(len(self.prediction)):
            prediction_table.append(self.prediction[i] == self.test_labels[i])
        return prediction_table

    def get_precision_table(self):
        """
        Zwraca tablicę zawierającą informację o zaklsyfikowaniu
        pozytywnych przypadków - tablicę precyzji 
        """
        precision_table = []
        for i in range(len(self.prediction)):
            if self.prediction[i] == 'Yes':
                precision_table.append(self.prediction[i] == self.test_labels[i])
        return precision_table     

    def get_sensitivity_table(self):
        """Zwraca tablicę czułości"""
        sensitivity_table = []
        for i in range(len(self.prediction)):
            if self.test_labels[i] == 'Yes':
                sensitivity_table.append(self.prediction[i] == self.test_labels[i])
        return sensitivity_table  

    def get_specificity_table(self):
        """Zwraca tablicę specyficzności"""
        specificity_table = []
        for i in range(len(self.prediction)):
            if self.test_labels[i] == 'No':
                specificity_table.append(self.prediction[i] == self.test_labels[i])
        return specificity_table  

    def get_name(self):
        """Zwraca nazwę klasyfikatora"""
        return self.name

    def get_short_name(self):
        """Zwraca nazwę na potrzebę tworzenia plików"""
        return self.short_name

    def get_params_string(self):
        """Zwraca ciąg znaków zawierajcy informację o ustawionych parametrach"""
        return self.params_string