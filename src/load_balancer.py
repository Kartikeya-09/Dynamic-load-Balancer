import psutil
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class LoadBalancer:
    def __init__(self, servers):
        """Initialize with a list of servers."""
        self.servers = servers
        self.server_load = {server: 0 for server in servers}  # Track load per server

    def add_task(self, task_id, task_load):
        """Assign task to the least loaded server."""
        least_loaded_server = min(self.server_load, key=self.server_load.get)
        self.server_load[least_loaded_server] += task_load
        logging.info(f"Task {task_id} assigned to {least_loaded_server} (Load: {task_load}%)")

    def get_next_server(self):
        """Implements round-robin server selection."""
        server = self.servers.pop(0)
        self.servers.append(server)
        return server

    def monitor_load(self):
        """Simulate server load balancing over time."""
        for _ in range(10):  # Simulating multiple cycles
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
