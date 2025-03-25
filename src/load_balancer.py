import psutil
import time
import logging
from itertools import cycle

# Configure logging with timestamps
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

class LoadBalancer:
    def __init__(self, servers):
        """Initialize with a list of servers."""
        self.servers = servers
        self.server_cycle = cycle(servers)  # Use cycle for round-robin
        self.server_load = {server: 0 for server in servers}
        logging.info(f"LoadBalancer initialized with servers: {servers}")

    def add_task(self, task_id, task_load):
        """Assign task to the least loaded server."""
        least_loaded_server = min(self.server_load, key=self.server_load.get)
        self.server_load[least_loaded_server] += task_load
        logging.info(f"Task {task_id} assigned to {least_loaded_server} (Load: {task_load}%)")

    def get_next_server(self):
        """Implements round-robin server selection."""
        server = next(self.server_cycle)
        logging.info(f"Next server selected: {server}")
        return server

    def monitor_load(self):
        """Simulate server load balancing over time."""
        for _ in range(10):
            logging.info(f"Current Server Loads: {self.server_load}")
            time.sleep(2)

# Example usage
if __name__ == "__main__": 
    servers = ["Server-1", "Server-2", "Server-3"]
    balancer = LoadBalancer(servers)
    tasks = [(1, 20), (2, 35), (3, 10), (4, 50)]  # (Task ID, Load %)

    for task_id, load in tasks:
        balancer.add_task(task_id, load)

    balancer.monitor_load()
