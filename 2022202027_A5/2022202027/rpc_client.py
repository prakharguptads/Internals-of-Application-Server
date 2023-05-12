import socket
import json
HOST = '127.0.0.1'
PORT=12346
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
def foo(*args):
	dict = {'name':"foo",'args':args}
	funArgs = json.dumps(dict)
	s.sendall(str.encode(funArgs))
	response = s.recv(1024).decode('utf-8')
	return response
def bar(*args):
	dict = {'name':"bar",'args':args}
	funArgs = json.dumps(dict)
	s.sendall(str.encode(funArgs))
	response = s.recv(1024).decode('utf-8')
	return response
def random_rating(*args):
	dict = {'name':"random_rating",'args':args}
	funArgs = json.dumps(dict)
	s.sendall(str.encode(funArgs))
	response = s.recv(1024).decode('utf-8')
	return response
