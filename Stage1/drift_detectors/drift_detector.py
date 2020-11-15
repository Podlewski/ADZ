from skmultiflow.drift_detection.ddm import DDM

from abc import ABCMeta, abstractmethod

class DriftDetector(metaclass=ABCMeta):
    """Klasa detektora dryftu"""

    def __init__(self):
        """Inicjalizacja klasy detektora dryftu"""
        self.model = None
        self.name = None
        self.change_indexes = []
        self.warning_zones_indexes = []

    def catch_concept_drift(self, predictions):
        """
        Funkcja wyłapująca Concept drift oraz strefy zagrożenia. Pobiera ona
        tablicę predykcji w postaci zmiennych logicznych.
        """
        for i in range(len(predictions)):
            self.model.add_element(int(not predictions[i]))
            if self.model.detected_change():
                self.change_indexes.append(i)          
            if self.model.detected_warning_zone():
                self.warning_zones_indexes.append(i)          

    def get_name(self):
        return self.name

    def get_change_indexes(self):
        """Zwraca indeksy dla których algorytm wykrył Concept drift"""
        return self.change_indexes.copy()

    def get_warning_zones_indexes(self):
        """Zwraca indeksy dla których algorytm wykrył strefę zagrożenia"""
        return self.warning_zones_indexes.copy()
