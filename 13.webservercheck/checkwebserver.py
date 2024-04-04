import http.client
def check_web_server_httplib(host,port=80):
    try:
      conn=http.client.HTTPConnection(host, port,timeout=10)
      conn.request("GET","/")
      response=conn.getresponse()
      print(f"Response from {host}:{port}-status code:{response.status}")
      conn.close()
    except ConnectionRefusedError:
       print(f"connection to{host}:{port}refused")
    except Exception as e:
       print(f"An error occurred:{str(e)}")
if __name__=="__main__":
   host=input("Enter the host address:" )
   port=(input("Enter the port number"))
   if port:
      port=int(port)
   else:
      port=80
   check_web_server_httplib(host,port)

    