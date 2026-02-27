import numpy as np
import matplotlib.pyplot as plt

def peak_detector(data: list[float], thr: float):
    value_record = 0
    time_record = 0
    indecies: list[float] = []
    for i, value in enumerate(data):
        if value > thr:
            if value > value_record:
                value_record = value
                time_record = i
        else:
            if value_record:
                indecies.append(time_record)
                time_record = 0
                value_record = 0

    return indecies

def moving_average_filter(data: np.ndarray, window: int):
    N = len(data)
    smoothed = np.zeros_like(data)
    halfwindow = window // 2
    for i in range(N):
        start = max(0, i - halfwindow)
        end = min(N, i + halfwindow + 1)
        smoothed[i] = data[start:end].mean()

    return smoothed

class HeartCycleExtactor:
    def __init__(self):
        ...

    def get_cycle(self, n):
        ...

    