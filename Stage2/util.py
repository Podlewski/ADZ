from matplotlib import pyplot as plt
from collections import namedtuple
import os
import seaborn

Plot = namedtuple('Plot', ['x', 'y', 'label', 'color'])

def count_accuracy_trend(predictions):
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
        seaborn.lineplot(x=plot.x, y=plot.y, label=plot.label, color=plot.color)

    for x in lines:
        plt.axvline(x, color='red')

    plt.title(title)
    plt.savefig(filename, dpi=300)


def save_accuracy_plot(algorithm, classifier, file_prefix, params, predictions,
                       lines, window):
    accuracy_trend = count_accuracy_trend(predictions)
    window_accuracy_trend = count_accuracy_trend_for_window(predictions, window)

    acc_plot = Plot(x=range(len(accuracy_trend)), y=accuracy_trend, label='dokładność', color='blue')
    window_acc_plot = Plot(x=range(window, len(predictions)), y=window_accuracy_trend, color='green',
                     label=f'dokładność ostatnich {window} próbek')

    title = get_plot_title(classifier, params, algorithm, 'dokładność klasyfikacji z wykrytym dryftem')
    filename = get_plot_filename(algorithm, f'Acc_{file_prefix}', params)

    save_drift_plot(title, filename, [acc_plot, window_acc_plot], lines)


def save_plots(algorithm, classifier, file_prefix, params, predictions,
               lines=[], window=1000):
    if not os.path.exists('img'):
        os.makedirs('img')
    plt.figure(figsize=(9,6))
    save_accuracy_plot(algorithm, classifier, file_prefix, params, predictions,
                       lines, window)


def get_accuracy_trend_plot(algorithm, predictions, lines=[]):
    accuracy_trend = count_accuracy_trend(predictions)
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