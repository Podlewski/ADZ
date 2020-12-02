from argument_parser import ArgumentParser
from data_loader import load_data
from drift_detectors.drift_adwin import DriftADWIN
from drift_detectors.drift_ddm import DriftDDM
from drift_detectors.drift_eddm import DriftEDDM
from drift_detectors.drift_page_hinkley import DriftPageHinkley
from classifiers.bayes import Bayes
from classifiers.neural_network import NeuralNetwork
from classifiers.knn import KNN
from classifiers.svm import SVM
from util import *

argument_parser = ArgumentParser()
filename = argument_parser.get_filename()
adwin_delta = argument_parser.get_delta()
training_set_ratio = argument_parser.get_training_set_ratio()
neighbors_number = argument_parser.get_neighbors_number()
kernel = argument_parser.get_kernel()
regulation = argument_parser.get_regulation()
max_iters = argument_parser.get_iterations()
n_of_hidden = argument_parser.get_n_of_hidden_layers()

data, labels = load_data(filename)

classifiers = [Bayes(data, labels, training_set_ratio),
               KNN(data, labels, training_set_ratio, neighbors_number),
               NeuralNetwork(data, labels, training_set_ratio, n_of_hidden, max_iters),
               SVM(data, labels, training_set_ratio, kernel, regulation)]

separator = False

for classifier in classifiers:
    if separator is True:
        print(f'\n\n==============================')
    separator = True
    print(f'{classifier.get_name()}\n')
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

        save_plots(algorithm.get_name(), classifier.get_name(),
                   classifier.get_short_name(), classifier.get_params_string(),
                   prediction_table, change_indexes)
