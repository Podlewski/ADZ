from skmultiflow.drift_detection.ddm import DDM
from skmultiflow.drift_detection.eddm import EDDM


class DriftDetector():
    """Klasa detektora dryftu"""
    model = None
    change_indexes = []
    warning_zones_indexes = []

    def __init__(self, model):
        """Inicjalizacja klasy detektora dryftu przyjmująca nazwę algorytmu"""
        if model == 'ddm' or model == 'DDM':
            self.model = DDM()
        elif model == 'eddm' or model == 'EDDM':
            self.model = EDDM()
        else:
            raise Exception('Count not find given drift detection method')

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

    def get_change_indexes(self):
        """Zwraca indeksy dla których algorytm wykrył Concept drift"""
        return self.change_indexes

    def get_warning_zones_indexes(self):
        """Zwraca indeksy dla których algorytm wykrył strefę zagrożenia"""
        return self.warning_zones_indexes
