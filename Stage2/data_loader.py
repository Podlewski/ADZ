import pandas as pd
import numpy as np


def factorize(column):
    """Przetwrzenie danych słownych na liczbowe"""
    if column.dtype in [np.float64, np.float32, np.int32, np.int64]:
        return column
    else:
        return pd.factorize(column)[0]

def load_data(file_name):
    """Wczytywanie danych z podanego pliku

    Funkcja wczytuje dane z podanego pliku, pozbywając się rekordów z pustymi
    danymi, przetwarza dane słowne na liczbowe, a następnie oddziela etykiety
    od danych (ostatnią kolumnę)
    """
    df = pd.read_csv(file_name, header=0).dropna()

    data = df.iloc[:,:-1].dropna(axis=1, how='all').apply(factorize)
    labels = pd.DataFrame(pd.factorize(df.iloc[:,-1])[0])

    return data, labels