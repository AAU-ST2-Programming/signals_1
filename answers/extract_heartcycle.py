import numpy as np
import matplotlib.pyplot as plt


class heartCycleExtractor:
    def __init__(self, filename, fs: float):
        self.filename = filename
        self.fs = fs
        self.time, self.data = np.genfromtxt(filename, unpack=True, delimiter=",")

    def get_cycle(self, n, before_R_sec: float = 0.1):
        filtered_data = self.moving_average_filter(15)
        R_indecies = self.peak_detector(filtered_data, 0.4)
        samples_before_R = int(before_R_sec * self.fs)
        cycle_indecies = R_indecies - samples_before_R
        # remove indecies that are out of bounds
        cycle_indecies = cycle_indecies[cycle_indecies >= 0]
        if len(cycle_indecies) <= n + 1:
            return None, None
        # get n cycles with time
        cycle_time = self.time[cycle_indecies[n] : cycle_indecies[n + 1]]
        cycle_data = filtered_data[cycle_indecies[n] : cycle_indecies[n + 1]]
        return cycle_time, cycle_data

    def peak_detector(self, data, thr: float):
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

        return np.array(indecies)

    def moving_average_filter(self, window: int):
        data = self.data
        N = len(data)
        smoothed = np.zeros_like(data)
        halfwindow = window // 2
        for i in range(N):
            start = max(0, i - halfwindow)
            end = min(N, i + halfwindow + 1)
            smoothed[i] = data[start:end].mean()

        return smoothed


cycle_extractor = heartCycleExtractor(
    "/home/nurrix/Documents/ST2-AnvendtProgrammering/signals_1/files/ECG_noisy.csv",
    fs=300,
)
i = 0
while True:
    cycle_time, cycle_data = cycle_extractor.get_cycle(i)

    if cycle_time is None or cycle_data is None:
        break

    # plot cycle
    plt.plot(cycle_data, color="blue", alpha=0.2)
    i += 1


plt.title("Extracted Heart Cycle")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
