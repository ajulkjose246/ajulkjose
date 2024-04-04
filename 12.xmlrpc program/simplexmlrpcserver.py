import xmlrpc.client
server=xmlrpc.client.ServerProxy("http://localhost:8000")
result=server.add(3,5)
print ("The result of addition is",result)