import numpy as np
import matplotlib.pyplot as plt

def moving_average_filter(data: np.ndarray, window: int):
    N = len(data)
    smoothed = np.zeros_like(data)
    halfwindow = window // 2
    for i in range(N):
        start = max(0, i - halfwindow)
        end = min(N, i + halfwindow + 1)
        smoothed[i] = data[start:end].mean()

    return smoothed


def peak_detector(data: list[float] | np.ndarray, thr: float):
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



class HeartCycleExtractor:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.time, self.ekg = np.genfromtxt(filename, unpack=True, delimiter=",")
        self.fs: float = round(1/ np.diff(self.time).mean())
        print("Filename:", filename)
        print("fs:",self.fs, "Hz")

    def get_cycle(self,n):
        offset0_1s = round(0.1 * self.fs)
        # filter data
        filtered_data = moving_average_filter(self.ekg,20)
        # get R peak indecies
        indecies = np.array(peak_detector(filtered_data,0.3))
        # get start og stop indecies
        cycle_starts = indecies - offset0_1s
        cycle_starts = cycle_starts[cycle_starts>=0]
        if not n<len(cycle_starts)-2:
            return None,None
        # lave time og ekg
        start = cycle_starts[n]
        stop = cycle_starts[n+1]
        time = self.time[start:stop]
        ekg = filtered_data[start:stop]

        # return
        return time, ekg



filename = "files/ECG_noisy.csv"
extractor = HeartCycleExtractor(filename=filename)

for i in range(1000):
    time,ekg = extractor.get_cycle(i)
    if time is not None and ekg is not None:
        plt.plot(time-time[0],ekg, color="blue", alpha=0.2)
    else:
        break
plt.title("Segmented EKGs")
plt.ylabel("Amplitude")
plt.xlabel("Time [s]")
plt.show()