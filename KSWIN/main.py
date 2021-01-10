from argument_parser import ArgumentParser
from data_loader import load_data
from kswin import KSWIN 
from knn import KNN
from ploter import *

argument_parser = ArgumentParser()
filename = argument_parser.get_filename()

data, labels = load_data(filename)

classifier = KNN(data, labels)

classifier.train()
classifier.test()

prediction_table = classifier.get_prediction_table()

print(f'Classifier accuracy: {classifier.get_accuracy() * 100:4.2f} %\n')

kswin = KSWIN()
kswin.add_data_points(prediction_table)
change_indexes = kswin.get_drift_indexes()

print(f'Change indexes: {change_indexes}')

get_accuracy_trend_plot(prediction_table, change_indexes)
