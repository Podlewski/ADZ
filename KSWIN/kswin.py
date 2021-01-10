import numpy as np
from scipy import stats


class KSWIN():

    def __init__(self, alpha=0.005, window_size=100, subwindow_size=20):
        if alpha < 0 or alpha > 1:
            raise ValueError("Alpha must be between 0 and 1 (should be lower than 0.01")
        if window_size < 0:
            raise ValueError("Window size must be greater than 0")
        if window_size < subwindow_size * 2 + 1:
            raise ValueError("Window size must be greater than double subwindow size")
        if subwindow_size < 0:
            raise ValueError("Subwindow size must be greater than 0")
        self.alpha = alpha
        self.window_size = window_size
        self.subwindow_size = subwindow_size
        self.length = 0
        self.window = np.array([])
        self.drift_indexes = []


    def add_data_points(self, data_points):
        for data_point in data_points:
            self.add_data_point(int(data_point))


    def add_data_point(self, data_point):
        self.window = np.concatenate([self.window,[data_point]])

        while len(self.window) > self.window_size:
            self.window = np.delete(self.window,0)

        if len(self.window) == self.window_size:
            self.window = np.delete(self.window,0)
            r_subwindow = self.window[-self.subwindow_size:]
            w_subwindow = np.random.choice(self.window[:-self.subwindow_size], self.subwindow_size)

            (statistic, p_value) = stats.ks_2samp(w_subwindow, r_subwindow)

            if p_value <= self.alpha and statistic > 0.1:
                self.drift_indexes.append(self.length - self.subwindow_size)
                self.window = r_subwindow

        self.length += 1


    def reset(self):
        self.window = np.array([])
        self.drift_indexes = np.array([])


    def get_drift_indexes(self):
        return self.drift_indexes.copy()
