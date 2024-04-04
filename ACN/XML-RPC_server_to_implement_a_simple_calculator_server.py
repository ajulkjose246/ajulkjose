from xmlrpc.server import SimpleXMLRPCServer

# Define a class for the calculator
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

# Create an XML-RPC server
server = SimpleXMLRPCServer(("localhost", 8000))

# Register the Calculator class with the server
server.register_instance(Calculator())

# Start the server's main loop
print("XML-RPC calculator server is running on port 8000...")
server.serve_forever()
