from os import path
import inspect
import server_procedures
import socket
import json
lis = ["foo","bar","random_rating"]
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    PORT = 12346
    s.bind(('127.0.0.1',PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print("recvd from client",data)
                if not data:
                    break
                else:
                    data = data.decode('utf-8')
                    funcDetails = json.loads(data)
                    if funcDetails['name'] in lis:
                        methodToCall = getattr(server_procedures,funcDetails['name'])
                        ans = methodToCall(*funcDetails['args'])
                        conn.sendall(str.encode(str(ans)))
                    else:
                        conn.sendall(str.encode(str("Invalid Function")))
if __name__ == "__main__":
    main()
