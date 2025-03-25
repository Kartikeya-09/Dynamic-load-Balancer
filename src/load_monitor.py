import psutil
import time
import logging

# Configure logging with timestamps
logging.basicConfig(filename="cpu_monitor.log", level=logging.INFO, format="%(asctime)s - CPU Load: %(message)s%%", datefmt="%Y-%m-%d %H:%M:%S")

def get_cpu_load(interval=1):
    """Returns the CPU usage percentage."""
    cpu_load = psutil.cpu_percent(interval=interval)
    logging.info(f"CPU Load: {cpu_load}%")
    return cpu_load

def monitor_cpu(interval=2, duration=30):
    """
    Monitors CPU utilization at regular intervals and logs the data.
    """
    print("Starting CPU Load Monitoring... Press Ctrl+C to stop.")
    
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_usage = get_cpu_load(interval=interval)  # Use existing function
        print(f"CPU Load: {cpu_usage}%")
        time.sleep(interval - 1)  # Adjust for the time taken to get CPU usage

    print("CPU Monitoring Completed.")

if __name__ == "__main__":
    monitor_cpu(interval=2, duration=30)  # Monitor for 30 seconds at 2-sec intervals
