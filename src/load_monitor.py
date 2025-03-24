import itertools

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.server_cycle = itertools.cycle(self.servers)

    def get_next_server(self):
        """Returns the next server to handle the request."""
        return next(self.server_cycle)

if __name__ == "__main__":
    servers = ["Server-1", "Server-2", "Server-3"]
    lb = LoadBalancer(servers)

    for i in range(6):
        print(f"Task {i+1} assigned to {lb.get_next_server()}")
