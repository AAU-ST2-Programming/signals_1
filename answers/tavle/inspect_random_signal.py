import numpy as np
import matplotlib.pyplot as plt

def moving_average(x, winsz = 20):
    filtered_x = np.zeros_like(x)
    for i in range(len(x)):
        start = i - winsz//2
        stop = i + winsz//2
        if start<0:
            start = 0
        if stop > len(x):
            stop = len(x)
        print(start, stop)

        slice = x[start:stop]
        filtered_x[i] = slice.mean()
    return filtered_x


signal1 = np.genfromtxt("C:/Users/Martin/Documents/ST2_AP_all_lectures/signals_1/files/random_signal1.csv")
signal2 = np.genfromtxt("C:/Users/Martin/Documents/ST2_AP_all_lectures/signals_1/files/random_signal2.csv")
x = np.linspace(0,1,len(signal1))

filted_signal1 = moving_average(signal1,winsz=50)
mean_signal1 = signal1.mean()
mean_signal2 = signal2.mean()
std_signal1 = signal1.std()
std_signal2 = signal2.std()

print("signal 1 mean:", mean_signal1, "  signal 2 mean:", mean_signal2)
print("signal 1 std:", std_signal1, "  signal 2 std:", std_signal2)
plt.plot(x,signal1,color="black",alpha=0.1, label="Rå signal")
plt.plot(x,filted_signal1,color="black", label= "filtered Signal")
# plt.plot(signal2)
plt.plot([0,1], [mean_signal1, mean_signal1], label="mean")
plt.plot([0,1], [mean_signal1+std_signal1, mean_signal1+std_signal1], label="mean+std")
plt.plot([0,1], [mean_signal1-std_signal1, mean_signal1-std_signal1], label="mean-std")
plt.legend()
plt.ylabel("Amplitude")
plt.xlabel("Tid [s]")
plt.show()
print("fin")