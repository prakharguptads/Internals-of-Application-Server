import json
import sys
f = open("rpc_client.py", "w")
pfile = sys.argv[1]
file1 = open(pfile)
s = "import socket\nimport json\nHOST = '127.0.0.1'\nPORT=12346\ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\ns.connect((HOST,PORT))\n"
data = json.load(file1)
data = data["remote_procedures"]
for d in data:
    s += "def "+d["procedure_name"]+"(*args):\n"+"\tdict = {'name':\""+d['procedure_name']+"\",'args':args}\n\tfunArgs = json.dumps(dict)\n\ts.sendall(str.encode(funArgs))\n\tresponse = s.recv(1024).decode('utf-8')\n\treturn response\n"
f.write(s)
f.close()