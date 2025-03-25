import psutil
import time

def get_cpu_load(interval=1):
    """Returns the CPU usage percentage."""
    return psutil.cpu_percent(interval=interval)

class LoadBalancer:
    """Simple round-robin load balancer."""
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_next_server(self):
        """Returns the next server in the round-robin sequence."""
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

if __name__ == "__main__":
    while True:
        cpu_usage = get_cpu_load()
        print(f"CPU Load: {cpu_usage}%")
        time.sleep(1)
