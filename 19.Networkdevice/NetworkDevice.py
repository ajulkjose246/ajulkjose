class NetworkDevice:
    def __init__(self,name,ip_address):
        self.name=name
        self.ip_address=ip_address
        self.connections=[]
    def connect_to(self,other_device):
        self.connections.append(other_device)
        other_device.connections.append(self)
    def __str__(self):
        return f"{self.name}({self.ip_address})"

router=NetworkDevice("Router","192.168.1.1")
switch=NetworkDevice("Switch","192.168.1.2")
pc1=NetworkDevice("PC1","192.168.1.3")
pc2=NetworkDevice("PC2","192.168.1.4")

router.connect_to(switch)        
switch.connect_to(pc1)
switch.connect_to(pc2)

print("Network COnfiguration:")
print(f"{router} is connected to:")
for device in router.connections:
    print(f" - {device}")
print(f"{switch} is connected to")
for device in switch.connections:
    print(f" - {device}")
