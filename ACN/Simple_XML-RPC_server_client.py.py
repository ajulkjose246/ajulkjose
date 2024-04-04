import xmlrpc.client
server_uri = "http://localhost:8000"
proxy = xmlrpc.client.ServerProxy(server_uri)
x = 5
y = 3
result = proxy.add(x, y)
print(f"The result of adding {x} and {y} is:", result)
