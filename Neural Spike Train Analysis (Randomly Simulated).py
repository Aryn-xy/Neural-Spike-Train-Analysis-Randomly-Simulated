import numpy as np
import matplotlib.pyplot as plt
duration = 1  #   seconds
firing_rate = 10  #Hz (spikes/ second)

# poisson distribution
n_spikes = np.random.poisson(firing_rate * duration)
spike_times = np.sort(np.random.rand(n_spikes) * duration)
print("Simulated Spike Times (seconds):", spike_times)

#raster plotting 
plt.figure(figsize=(10, 3))
plt.eventplot(spike_times, color='black')
plt.xlabel("Time (s)")
plt.title("Spike Train Simulation (Randomly Generated)")
plt.show()

# calculate ISI 
isi = np.diff(spike_times)

#plotting ISI histogram
plt.figure(figsize=(10, 5))
plt.hist(isi, bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Inter-Spike Interval (s)")
plt.title("Inter-Spike Interval (ISI) Distribution")
plt.show()

#calculate firing rate
calculated_firing_rate = len(spike_times) / duration
print(f"Calculated Firing Rate: {calculated_firing_rate:.2f} Hz")
