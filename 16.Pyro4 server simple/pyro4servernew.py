import Pyro4

@Pyro4.expose
class MyServer:
    def greet(self, name):
        return f"Hello, {name}!"
Pyro4.Daemon.serveSimple({MyServer: "myserver"},ns=True)

# python -m Pyro4.naming
# run server and client
