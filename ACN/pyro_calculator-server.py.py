import Pyro4

class Calculator(object):
    @Pyro4.expose
    def add(self, a, b):
        return a + b

    @Pyro4.expose
    def subtract(self, a, b):
        return a - b

    @Pyro4.expose
    def multiply(self, a, b):
        return a * b

    @Pyro4.expose
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

daemon = Pyro4.Daemon()

uri = daemon.register(Calculator)
print("Server URI : ", uri)
ns = Pyro4.locateNS()
ns.register("calculator", uri)
print("Server is Ready")
daemon.requestLoop()

# python -m Pyro4.naming
# run server and client
