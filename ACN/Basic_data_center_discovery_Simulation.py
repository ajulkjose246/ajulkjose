class Server:
    def __init__(self, name, cpu_capacity, memory_capacity, cpu_usage=0, memory_usage=0):
        self.name = name
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage

    def allocate_resources(self, cpu, memory):
        if self.cpu_capacity - self.cpu_usage >= cpu and self.memory_capacity - self.memory_usage >= memory:
            self.cpu_usage += cpu
            self.memory_usage += memory
            return True
        else:
            return False

    def release_resources(self, cpu, memory):
        self.cpu_usage -= cpu
        self.memory_usage -= memory


class Datacenter:
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        self.servers.append(server)

    def allocate_resources(self, cpu, memory):
        for server in self.servers:
            if server.allocate_resources(cpu, memory):
                return server.name
        return None


dc = Datacenter()
dc.add_server(Server("Server1", 4, 16))
dc.add_server(Server("Server2", 8, 32))
dc.add_server(Server("Server3", 2, 8))

workloads = [(2, 8), (4, 6), (1, 4)]

for cpu, memory in workloads:
    server_name = dc.allocate_resources(cpu, memory)
    if server_name:
        print(f"Workload ({cpu} CPU, {memory} Memory) allocated to {server_name}.")
    else:
        print(f"No server available to handle workload ({cpu} CPU, {memory} Memory).")