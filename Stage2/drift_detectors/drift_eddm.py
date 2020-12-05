from drift_detectors.drift_detector import DriftDetector
from skmultiflow.drift_detection.eddm import EDDM


class DriftEDDM(DriftDetector):

    def __init__(self):
        """Inicjalizacja klasy algorytmu EDDM"""
        self.name = 'EDDM'
        self.model = EDDM()
        self.change_indexes = []
        self.warning_zones_indexes = []

    def reset_model(self):
        self.model = EDDM()
        self.change_indexes = []
        self.warning_zones_indexes = []