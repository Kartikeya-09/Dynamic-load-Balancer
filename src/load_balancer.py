import psutil
import time

def get_cpu_load(interval=1):
    """Returns the CPU usage percentage."""
    return psutil.cpu_percent(interval=interval)

if __name__ == "__main__":
    while True:
        cpu_usage = get_cpu_load()
        print(f"CPU Load: {cpu_usage}%")
        time.sleep(1)
