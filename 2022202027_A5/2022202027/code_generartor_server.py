import sys
import json
f = open("rpc_server.py", "w")
from inspect import signature
pfile = sys.argv[1]
f.write("from os import path\n")
f.write("import inspect\n")
f.write("import server_procedures\n")
f.write("import socket\n")
f.write("import json\n")

file = open(pfile)
ff = json.load(file)
s = "lis = ["
for d in ff["remote_procedures"]:
        s += "\""+d["procedure_name"]+"\","
s = s[:-1]
s+="]\n"
f.write(s)
f.write("def main():\n")

f.write("    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n")
f.write("    PORT = 12346\n")
f.write("    s.bind(('127.0.0.1',PORT))\n")
f.write("    s.listen()\n")
f.write("    while True:\n")
f.write("        conn, addr = s.accept()\n")

f.write("        with conn:\n")
f.write("            print('Connected by', addr)\n")
f.write("            while True:\n")
f.write("                data = conn.recv(1024)\n")
f.write("                print(\"recvd from client\",data)\n")
f.write("                if not data:\n")
f.write("                    break\n")
f.write("                else:\n")
f.write("                    data = data.decode('utf-8')\n")
f.write("                    funcDetails = json.loads(data)\n")
f.write("                    if funcDetails['name'] in lis:\n")
f.write("                        methodToCall = getattr(server_procedures,funcDetails['name'])\n")
f.write("                        ans = methodToCall(*funcDetails['args'])\n")
f.write("                        conn.sendall(str.encode(str(ans)))\n")
f.write("                    else:\n")
f.write("                        conn.sendall(str.encode(str(\"Invalid Function\")))\n")
    

f.write("if __name__ == \"__main__\":\n")
f.write("    main()\n")