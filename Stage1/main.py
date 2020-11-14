from data_loader import load_data
from drift_detector import DriftDetector
from kneighbors import KNeighbors
import pandas as pd
import sys
from skmultiflow.drift_detection.eddm import EDDM
from skmultiflow.drift_detection.ddm import DDM


data, labels = load_data(sys.argv[1])

classifier = KNeighbors(data, labels, 0.2)

classifier.train()
classifier.test()

prediction_table = classifier.get_prediction_table()

print(f'Accuracy: {classifier.get_accuracy() * 100:4.2f} %')

ddm = DriftDetector('DDM')
eddm = DriftDetector('EDDM')

ddm.catch_concept_drift(prediction_table)
eddm.catch_concept_drift(prediction_table)

ddm_change_indexes = ddm.get_change_indexes()
ddm_warning_zones_indexes = ddm.get_warning_zones_indexes()
eddm_change_indexes = eddm.get_change_indexes()
eddm_warning_zones_indexes = eddm.get_warning_zones_indexes()
