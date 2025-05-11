import numpy as np
import matplotlib.pyplot as plt

# Set the parameters for the simulation
duration = 1 # Duration of the simulation in seconds
firing_rate = 10  # Neuron firing rate in Hz (spikes / second)

# Generate the number of spikes based on a Poisson distribution
n_spikes = np.random.poisson(firing_rate * duration)

# Simulate the spike times (randomly distributed within the duration)
spike_times = np.sort(np.random.rand(n_spikes) * duration)

print("Simulated Spike Times (seconds):", spike_times)

# Create the raster plot to visualize spike timings
plt.figure(figsize=(10, 3))
plt.eventplot(spike_times, color='black')
plt.xlabel("Time (s)")
plt.title("Spike Train Simulation (Randomly Generated)")
plt.show()

# Calculate Inter-Spike Intervals (ISI) - time difference between consecutive spikes
isi = np.diff(spike_times)

# Plotting ISI histogram
plt.figure(figsize=(10, 5))
plt.hist(isi, bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Inter-Spike Interval (s)")
plt.title("Inter-Spike Interval (ISI) Distribution")
plt.show()

# Calculate firing rate based on the spike count
calculated_firing_rate = len(spike_times) / duration
print(f"Calculated Firing Rate: {calculated_firing_rate:.2f} Hz")
