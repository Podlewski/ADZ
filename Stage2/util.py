from matplotlib import pyplot as plt
from collections import namedtuple
import os
import seaborn

Plot = namedtuple('Plot', ['x', 'y', 'color'])

def count_trend(predictions):
    correct = 0
    accuracy_trend = []
    for x in range(len(predictions)):
        if predictions[x]:
            correct += 1

        accuracy_trend.append(correct / float(x+1))

    return accuracy_trend

def count_accuracy_trend_for_window(predictions, windowLen=10):
    accuracy_trend = []
    for x in range(windowLen, len(predictions)):
        window = predictions[x - windowLen: x]
        accuracy_trend.append(window.count(True) / float(len(window)))

    return accuracy_trend


def get_plot_title(classifier, params, algorithm, suffix):
    parsed_params = f' {params}' if params else ""
    return f'{classifier}{parsed_params}, {algorithm} - {suffix}'


def get_plot_filename(algorithm, file_prefix, params):
    params_short = params.replace(', ', '-').replace('(', '').replace(')', '')
    return f'img\\{file_prefix}_{"".join(algorithm.split())}_{params_short}'


def save_drift_plot(title, filename, plots, lines):
    for plot in plots:
        seaborn.lineplot(x=plot.x, y=plot.y, color=plot.color)

    for x in lines:
        plt.axvline(x, color='red')

    plt.title(title)
    plt.savefig(filename, dpi=300)
    plt.close()


def save_metric_plot(algorithm, classifier, metric_name, file_prefix, params, predictions):
    print(f'save met: {len(predictions)}')
    algorithm.catch_concept_drift(predictions)
    change_indexes = algorithm.get_change_indexes()

    accuracy_trend = count_trend(predictions)

    acc_plot = Plot(x=range(len(accuracy_trend)), y=accuracy_trend, color='blue')

    title = get_plot_title(classifier, params, algorithm.get_name(), metric_name)
    filename = get_plot_filename(algorithm.get_name(), f'{metric_name}_{file_prefix}', params)

    save_drift_plot(title, filename, [acc_plot], change_indexes)

# def save_precision_plot(algorithm, classifier, file_prefix, params, predictions, lines):
#     precision_trend = count_trend(predictions)
#
#     prec_plot = Plot(x=range(len(precision_trend)), y=precision_trend, color='blue')
#
#     title = get_plot_title(classifier, params, algorithm, 'precyzja klasyfikacji z wykrytym dryftem')
#     filename = get_plot_filename(algorithm, f'Prec_{file_prefix}', params)
#
#     save_drift_plot(title, filename, [prec_plot], lines)
#
# def save_sensitivity_plot(algorithm, classifier, file_prefix, params, predictions, lines):
#     sensitivity_trend = count_trend(predictions)
#
#     sens_plot = Plot(x=range(len(sensitivity_trend)), y=sensitivity_trend, color='blue')
#
#     title = get_plot_title(classifier, params, algorithm, 'czułość klasyfikacji z wykrytym dryftem')
#     filename = get_plot_filename(algorithm, f'Sens_{file_prefix}', params)
#
#     save_drift_plot(title, filename, [sens_plot], lines)
#
# def save_specificity_plot(algorithm, classifier, file_prefix, params, predictions, lines):
#     specificity_trend = count_trend(predictions)
#
#     spec_plot = Plot(x=range(len(specificity_trend)), y=specificity_trend, color='blue')
#
#     title = get_plot_title(classifier, params, algorithm, 'specyficzność klasyfikacji z wykrytym dryftem')
#     filename = get_plot_filename(algorithm, f'Spec_{file_prefix}', params)
#
#     save_drift_plot(title, filename, [spec_plot], lines)

def save_plots(algorithm, classifier, file_prefix, params, metrics):
    # accuracy_table, precision_table, sensitivity_table, specificity_table = metrics
    accuracy_table, precision_table = metrics

    print(len(accuracy_table))
    print(len(precision_table))
    if not os.path.exists('img'):
        os.makedirs('img')

    plt.figure(figsize=(9,6))

    save_metric_plot(algorithm, classifier, "precyzja", file_prefix, params, precision_table)
    save_metric_plot(algorithm, classifier, "dokładność", file_prefix, params, accuracy_table)


def get_accuracy_trend_plot(algorithm, predictions, lines=[]):
    accuracy_trend = count_trend(predictions)
    seaborn.lineplot(x=range(len(accuracy_trend)), y=accuracy_trend)
    for x in lines:
        plt.axvline(x, color='red')

    plt.title('Dokładność modelu na podstawie wszystkich próbek dla algorytmu %s' % algorithm)
    plt.xlabel('Numer próbki')
    plt.ylabel('Dokładność')
    plt.figure(figsize=(12,8))
    plt.tight_layout()
    plt.savefig('test', dpi=200)
    # plt.show()


def get_accuracy_trend_for_window_plot(algorithm, predictions, lines=[], window=1000):
    
    seaborn.lineplot(x=range(window, len(predictions)), y=accuracy_trend)
    for x in lines:
        plt.axvline(x, color='red')

    plt.title('Dokładność modelu na podstawie przedziału %d próbek dla algorytmu %s' % (window, algorithm))
    plt.xlabel('Numer próbki')
    plt.ylabel('Dokładność')
    plt.show()