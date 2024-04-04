import Pyro4
class Myserver(object):
    @Pyro4.expose
    def greet(self,name):
        return "Hello, {}!".format(name)
daemon=Pyro4.Daemon()
uri=daemon.register(Myserver)
print("server URI:",uri)
ns=Pyro4.locateNS()
ns.register("myserver", uri)
print("server ready.")
daemon.requestLoop()