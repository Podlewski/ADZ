import seaborn
from matplotlib import pyplot as plt


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


def get_accuracy_trend_plot(algorithm, predictions, lines=[]):
    accuracy_trend = count_accuracy_trend(predictions)
    seaborn.lineplot(x=range(len(accuracy_trend)), y=accuracy_trend)
    for x in lines:
        plt.axvline(x, color='red')

    plt.title('Dokładność modelu na podstawie wszystkich próbek dla algorytmu %s' % algorithm)
    plt.xlabel('Numer próbki')
    plt.ylabel('Dokładność')
    plt.show()


def get_accuracy_trend_for_window_plot(algorithm, predictions, window=100, lines=[]):
    accuracy_trend = count_accuracy_trend_for_window(predictions, window)
    seaborn.lineplot(x=range(window, len(predictions)), y=accuracy_trend)
    for x in lines:
        plt.axvline(x, color='red')

    plt.title('Dokładność modelu na podstawie przedziału %d próbek dla algorytmu %s' % (window, algorithm))
    plt.xlabel('Numer próbki')
    plt.ylabel('Dokładność')
    plt.show()