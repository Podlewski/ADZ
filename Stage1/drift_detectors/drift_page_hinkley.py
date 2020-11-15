from drift_detectors.drift_detector import DriftDetector
from skmultiflow.drift_detection.page_hinkley import PageHinkley


class DriftPageHinkley(DriftDetector):

    def __init__(self):
        """Inicjalizacja klasy algorytmu Page-Hinkley"""
        self.name = 'Page Hinkley'
        self.model = PageHinkley()
        self.change_indexes = []
        self.warning_zones_indexes = []

    def prepare_element(self, prediction):
        return int(prediction)