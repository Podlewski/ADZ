import argparse


class ArgumentParser:
    args = None

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='ADZ - Etap 2', formatter_class=argparse.RawTextHelpFormatter,
            description='Politechnika Łódzka\
                         \nAnaliza Danych Złożonych - Etap 2\
                         \n\nAutorzy:\
                         \n  Paweł Galewicz\t234053\
                         \n  Karol Podlewski\t234106')

        self.parser.add_argument(metavar='NAZWA_PLIKU', dest='filename', type=str,
                                 help='Nazwa pliku z danymi strumieniowymi')

        self.parser.add_argument('-t', metavar='T', dest='training_set_ratio',
                                 type=float, default=0.2,
                                 help='Częśc zbioru treningowego dla klasyfikatorów')

        self.parser.add_argument('-n', metavar='N', dest='neighbors_number',
                                 type=int, default=5,
                                 help='Liczba sąsiadów dla klasyfikatorów')

        self.parser.add_argument('-d', metavar='DELTA', dest='delta', type=float,
                                 default=0.002, help='Delta dla algorytmu ADWIN')

        self.parser.add_argument('-k', metavar='K', dest='kernel', type=str,
                                 default="rbf", help='Funkcja jądra dla algorytmu SVM (wspierane funcje: linear, rbf, poly, sigmoid)')

        self.parser.add_argument('-r', metavar='R', dest='regulation', type=float,
                                 default=1, help='Parametr regularyzacji dla algorytmu SVM')

        self.parser.add_argument('-l', metavar='L', dest='n_of_hidden_layers', type=int,
                                 default=1, help='Liczba warstw ukrytych w sieci neuronowej')

        self.parser.add_argument('-i', metavar='I', dest='iterations', type=int,
                                 default=1000, help='Maksymalna liczba iteracji sieci neuronowej')

        self.args = self.parser.parse_args()

    def get_filename(self):
        return self.args.filename

    def get_delta(self):
        return self.args.delta

    def get_training_set_ratio(self):
        return self.args.training_set_ratio

    def get_neighbors_number(self):
        return self.args.neighbors_number

    def get_kernel(self):
        supported_kernels = ['linear', 'rbf', 'poly', 'sigmoid']
        while self.args.kernel not in supported_kernels:
            self.args.kernel = str(input('\nWybierz wspieraną funkcję jądra (linear, rbf, poly, sigmoid) \nWybór: '))

        return self.args.kernel

    def get_regulation(self):
        return self.args.regulation

    def get_n_of_hidden_layers(self):
        return self.args.n_of_hidden_layers

    def get_iterations(self):
        return self.args.iterations
