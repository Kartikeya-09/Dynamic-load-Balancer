import psutil
import time
import matplotlib.pyplot as plt
import logging

# Configure logging with timestamps
logging.basicConfig(filename="visualization.log", level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

def monitor_cpu(duration=10, interval=1):
    """Records CPU usage over time."""
    cpu_usage = []
    timestamps = []

    for i in range(duration):
        usage = psutil.cpu_percent(interval=interval)
        cpu_usage.append(usage)
        timestamps.append(time.time())
        logging.info(f"Time: {i+1}s | CPU: {usage}%")
        print(f"Time: {i+1}s | CPU: {usage}%")

    return timestamps, cpu_usage

def plot_cpu_load():
    """Plots the recorded CPU load."""
    logging.info("Starting CPU load plotting.")
    timestamps, cpu_usage = monitor_cpu()

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, cpu_usage, marker='o', linestyle='-', color='b', label="CPU Usage")
    plt.xlabel("Time (s)")
    plt.ylabel("CPU Load (%)")
    plt.title("CPU Load Over Time")
    plt.legend()
    plt.grid()
    plt.show()
    logging.info("Finished CPU load plotting.")

if __name__ == "__main__":
    plot_cpu_load()
