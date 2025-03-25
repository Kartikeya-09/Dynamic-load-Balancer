import psutil
import time
import logging

# Configure logging for debugging
logging.basicConfig(filename="cpu_monitor.log", level=logging.INFO, format="%(asctime)s - CPU Load: %(message)s%%")

def monitor_cpu(interval=2, duration=30):
    """
    Monitors CPU utilization at regular intervals and logs the data.
    
    :param interval: Time in seconds between checks.
    :param duration: Total duration to monitor (seconds).
    """
    print("Starting CPU Load Monitoring... Press Ctrl+C to stop.")
    
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Load: {cpu_usage}%")
        logging.info(cpu_usage)
        time.sleep(interval - 1)  # Adjust for the time taken to get CPU usage

    print("CPU Monitoring Completed.")

if __name__ == "__main__":
    monitor_cpu(interval=2, duration=30)  # Monitor for 30 seconds at 2-sec intervals
