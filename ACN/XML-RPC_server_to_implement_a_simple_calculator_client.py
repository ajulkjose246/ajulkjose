import xmlrpc.client

# URI of the XML-RPC server
server_uri = "http://localhost:8000"

# Create an XML-RPC client proxy
proxy = xmlrpc.client.ServerProxy(server_uri)

# Use the Calculator methods remotely
x = 10
y = 5

try:
    print(f"{x} + {y} = {proxy.add(x, y)}")
    print(f"{x} - {y} = {proxy.subtract(x, y)}")
    print(f"{x} * {y} = {proxy.multiply(x, y)}")
    print(f"{x} / {y} = {proxy.divide(x, y)}")

except xmlrpc.client.Fault as err:
    print("Error:", err.faultString)
except ConnectionError:
    print("Error: Could not connect to the server. Make sure the server is running.")
