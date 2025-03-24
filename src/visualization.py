import psutil
import time
import matplotlib.pyplot as plt

def monitor_cpu(duration=10, interval=1):
    """Records CPU usage over time."""
    cpu_usage = []
    timestamps = []

    for i in range(duration):
        usage = psutil.cpu_percent(interval=interval)
        cpu_usage.append(usage)
        timestamps.append(time.time())
        print(f"Time: {i+1}s | CPU: {usage}%")

    return timestamps, cpu_usage

def plot_cpu_load():
    """Plots the recorded CPU load."""
    timestamps, cpu_usage = monitor_cpu()

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, cpu_usage, marker='o', linestyle='-', color='b', label="CPU Usage")
    plt.xlabel("Time (s)")
    plt.ylabel("CPU Load (%)")
    plt.title("CPU Load Over Time")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_cpu_load()
