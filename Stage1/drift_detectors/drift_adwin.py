from skmultiflow.drift_detection.adwin import ADWIN
from drift_detectors.drift_detector import DriftDetector


class DriftADWIN(DriftDetector):
    
    def __init__(self, delta=0.002):
        """Inicjalizacja klasy algorytmu ADWIN"""
        self.name = 'ADWIN'
        self.model = ADWIN(delta)
        self.change_indexes = []
        self.warning_zones_indexes = []

    def catch_concept_drift(self, predictions):
        """
        Funkcja wyłapująca Concept drift oraz strefy zagrożenia. Pobiera ona
        tablicę predykcji w postaci zmiennych logicznych.
        """
        for i in range(len(predictions)):
            self.model.add_element(int(predictions[i]))
            if self.model.detected_change():
                self.change_indexes.append(i)          
            if self.model.detected_warning_zone():
                self.warning_zones_indexes.append(i)  