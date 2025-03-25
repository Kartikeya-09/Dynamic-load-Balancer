import threading
import load_monitor  # Corrected import
import load_balancer
import visualization

def monitor():
    """Monitors CPU load in a separate thread."""
    while True:
        print(f"CPU Load: {load_monitor.get_cpu_load()}%")  # Corrected function call
        
def visualize():
    """Visualizes CPU usage graph."""
    visualization.plot_cpu_load()

if __name__ == "__main__":
    # Start CPU monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor, daemon=True)
    monitor_thread.start()

    # Simulate Load Balancer
    servers = ["Server-1", "Server-2", "Server-3"]
    lb = load_balancer.LoadBalancer(servers)

    for i in range(5):
        print(f"Task {i+1} assigned to {lb.get_next_server()}")

    # Start visualization
    visualize()
