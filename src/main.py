import threading
import load_monitor
import load_balancer
import visualization
import logging

# Configure logging with timestamps
logging.basicConfig(filename="main.log", level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

def monitor():
    """Monitors CPU load in a separate thread."""
    while True:
        cpu_load = load_monitor.get_cpu_load()
        logging.info(f"CPU Load: {cpu_load}%")
        print(f"CPU Load: {cpu_load}%")
        
def visualize():
    """Visualizes CPU usage graph."""
    logging.info("Starting visualization.")
    visualization.plot_cpu_load()
    logging.info("Visualization completed.")

if __name__ == "__main__":
    logging.info("Program started.")

    # Start CPU monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor, daemon=True)
    monitor_thread.start()
    logging.info("Started CPU monitoring thread.")

    # Simulate Load Balancer
    servers = ["Server-1", "Server-2", "Server-3"]
    lb = load_balancer.LoadBalancer(servers)
    logging.info("Initialized LoadBalancer.")

    for i in range(5):
        assigned_server = lb.get_next_server()
        logging.info(f"Task {i+1} assigned to {assigned_server}.")
        print(f"Task {i+1} assigned to {assigned_server}")

    # Start visualization
    visualize()
    logging.info("Program completed.")
