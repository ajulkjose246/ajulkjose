import Pyro4
ns=Pyro4.locateNS()
uri=ns.lookup("myserver")
server=Pyro4.Proxy(uri)
name=input("ENter the nmae:")
message=server.greet(name)
print("messagefrom server:",message)