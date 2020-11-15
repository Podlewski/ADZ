from argument_parser import ArgumentParser
from data_loader import load_data
from drift_detectors.drift_adwin import DriftADWIN
from drift_detectors.drift_ddm import DriftDDM
from drift_detectors.drift_eddm import DriftEDDM
from drift_detectors.drift_page_hinkley import DriftPageHinkley
from knn import KNN
import pandas as pd
import sys
from skmultiflow.drift_detection.eddm import EDDM
from skmultiflow.drift_detection.ddm import DDM



argument_parser = ArgumentParser()
filename = argument_parser.get_filename()
adwin_delta = argument_parser.get_delta()
knn_parameters = argument_parser.get_knn_parameters()

data, labels = load_data(filename)

classifier = KNN(data, labels, knn_parameters[0], knn_parameters[1])

classifier.train()
classifier.test()

prediction_table = classifier.get_prediction_table()

print(f'{"Accuracy:":<15}{classifier.get_accuracy() * 100:4.2f} %\n')

algorithms = [DriftDDM(),
              DriftEDDM(),
              DriftADWIN(adwin_delta),
              DriftPageHinkley()]

for algorithm in algorithms:
    algorithm.catch_concept_drift(prediction_table)

    change_indexes = algorithm.get_change_indexes()
    warning_zones_indexes = algorithm.get_warning_zones_indexes()

    print(f'{algorithm.get_name()+":": <15}{change_indexes}')
