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


def get_accuracy_trend_plot(predictions, lines=[]):
    accuracy_trend = count_accuracy_trend(predictions)
    seaborn.lineplot(x=range(len(accuracy_trend)), y=accuracy_trend)
    for x in lines:
        plt.axvline(x, color='red')

    plt.title('Dokładność modelu na podstawie wszystkich próbek dla algorytmu KSWIN')
    plt.xlabel('Numer próbki')
    plt.ylabel('Dokładność')
    plt.show()
