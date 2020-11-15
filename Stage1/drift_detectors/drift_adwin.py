from skmultiflow.drift_detection.adwin import ADWIN
from drift_detectors.drift_detector import DriftDetector


class DriftADWIN(DriftDetector):
    
    def __init__(self, delta=0.002):
        """Inicjalizacja klasy algorytmu ADWIN"""
        self.name = 'ADWIN'
        self.model = ADWIN(delta)
        self.change_indexes = []
        self.warning_zones_indexes = []
