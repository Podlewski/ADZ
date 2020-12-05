from skmultiflow.drift_detection.adwin import ADWIN
from drift_detectors.drift_detector import DriftDetector


class DriftADWIN(DriftDetector):
    
    def __init__(self, delta=0.002):
        """Inicjalizacja klasy algorytmu ADWIN"""
        self.name = 'ADWIN'
        self.delta = delta
        self.model = ADWIN(delta)
        self.change_indexes = []
        self.warning_zones_indexes = []

    def prepare_element(self, prediction):
        return int(prediction)

    def reset_model(self):
        self.model = ADWIN(self.delta)
        self.change_indexes = []
        self.warning_zones_indexes = []