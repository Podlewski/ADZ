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

        self.parser.add_argument('-t', metavar='N', dest='training_set_ratio',
                                 type=float, default=0.2,
                                 help='Częśc zbioru treningowego dla klasyfikatorów')

        self.parser.add_argument('-n', metavar='N', dest='neighbors_number',
                                 type=int, default=5,
                                 help='Liczba sąsiadów dla klasyfikatorów')

        self.parser.add_argument('-d', metavar='DELTA', dest='delta', type=float,
                                 default=0.002, help='Delta dla algorytmu ADWIN')

        self.args = self.parser.parse_args()

    def get_filename(self):
        return self.args.filename

    def get_delta(self):
        return self.args.delta

    def get_training_set_ratio(self):
        return self.args.training_set_ratio

    def get_neighbors_number(self):
        return self.args.neighbors_number
