from skmultiflow.drift_detection.ddm import DDM
from drift_detectors.drift_detector import DriftDetector


class DriftDDM(DriftDetector):

    def __init__(self):
        """Inicjalizacja klasy algorytmu DDM"""
        self.name = 'DDM'
        self.model = DDM()
        self.change_indexes = []
        self.warning_zones_indexes = []
