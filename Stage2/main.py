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
algorithm = argument_parser.get_algorithm()
printing = argument_parser.is_printing()

data, labels = load_data(filename)

classifiers = {'bayes': Bayes(data, labels, training_set_ratio),
               'knn': KNN(data, labels, training_set_ratio, neighbors_number),
               'nn': NeuralNetwork(data, labels, training_set_ratio, n_of_hidden, max_iters),
               'svm': SVM(data, labels, training_set_ratio, kernel, regulation)}

classifier =  classifiers[algorithm]

classifier.train()
classifier.test()

accuracy_table = classifier.get_accuracy_table()
precision_table = classifier.get_precision_table()
sensitivity_table = classifier.get_sensitivity_table()
specificity_table = classifier.get_specificity_table()

metrics = (accuracy_table, precision_table, sensitivity_table, specificity_table)

if printing is True:
    print(f'{classifier.get_name()}\n')
    print(f'{"Dokładność:":<15}{classifier.get_accuracy() * 100:4.2f} %')
    print(f'{"Precyzja:":<15}{classifier.get_precision() * 100:4.2f} %')
    print(f'{"Czułość:":<15}{classifier.get_sensitivity() * 100:4.2f} %')
    print(f'{"Specyficzność:":<15}{classifier.get_specificity() * 100:4.2f} %\n')


algorithms = [DriftDDM(),
              DriftEDDM(),
              DriftADWIN(adwin_delta),
              DriftPageHinkley()]

for algorithm in algorithms:
    save_plots(algorithm, classifier.get_name(),
               classifier.get_short_name(), classifier.get_params_string(),
               metrics)
