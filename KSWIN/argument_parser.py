import argparse


class ArgumentParser:
    args = None

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='KSWIN - przykład użycia', formatter_class=argparse.RawTextHelpFormatter,
            description='Politechnika Łódzka\
                         \nAnaliza Danych Złożonych - algorytm KSWIN - przykład użycia\
                         \n\nAutorzy:\
                         \n  Paweł Galewicz\t234053\
                         \n  Karol Podlewski\t234106')

        self.parser.add_argument(metavar='NAZWA_PLIKU', dest='filename', type=str,
                                 help='Nazwa pliku z danymi strumieniowymi')

        self.args = self.parser.parse_args()

    def get_filename(self):
        return self.args.filename

