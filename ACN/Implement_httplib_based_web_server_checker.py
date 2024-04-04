import http.client

conn=http.client.HTTPConnection("www.google.com",80,timeout=30)
conn.request("GET","/")
response=conn.getresponse().status
if response==200:
    print("connection success")
else:
    print("connection failed")