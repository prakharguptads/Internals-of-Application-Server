from ftplib import FTP
import os
import time
import sys
import signal
from threading import Thread
url = input("URL : ").split(":")
flag=True
ftpObject = FTP();
dict = {}
ftpResponseCode = ftpObject.connect(host=(url[0]), port=int(url[1]));
print("Response code for connect:%s"%ftpResponseCode)

username = input("Username : ")
password = input("Password : ")
name = sys.argv[1]
ftpResponseCode = ftpObject.login(username,password);
print("Response code for login:%s"%ftpResponseCode)

def Addition(i):
    checkname = name+"$$request"
    if checkname in i:
        respMessage = ftpObject.retrbinary("RETR "+i, open(i, 'wb').write);
        print(i)
        ff = open(i,'r').read().split(";")
        print(ff)
        re=0
        if ff[1]=="+":
            re=1
            result = int(ff[0])+int(ff[2])
        ftpResponse = ftpObject.delete(i);
        fi = i.split("$$")
        f1 = open("response_"+fi[0],"w")
        if re == 0:
            f1.write("Invalid Request")
        else:
            f1.write(str(result))
        f1.close()
        respMessage = ftpObject.storbinary("STOR "+("response_"+fi[0]), open(("response_"+fi[0]), 'rb'));
        os.remove(i)
def Subtraction(i):
    checkname = name+"$$request"
    if checkname in i:
        respMessage = ftpObject.retrbinary("RETR "+i, open(i, 'wb').write);
        print(i)
        ff = open(i,'r').read().split(";")
        print(ff)
        re=0
        if ff[1]=="-":
            re=1
            result = int(ff[0])-int(ff[2])
        ftpResponse = ftpObject.delete(i);
        fi = i.split("$$")
        f1 = open("response_"+fi[0],"w")
        if re == 0:
            f1.write("Invalid Request")
        else:
            f1.write(str(result))
        f1.close()
        respMessage = ftpObject.storbinary("STOR "+("response_"+fi[0]), open(("response_"+fi[0]), 'rb'));
        os.remove(i)
def Multiplication(i):
    checkname = name+"$$request"
    if checkname in i:
        respMessage = ftpObject.retrbinary("RETR "+i, open(i, 'wb').write);
        print(i)
        ff = open(i,'r').read().split(";")
        print(ff)
        re=0
        if ff[1]=="*":
            re = 1
            result = int(ff[0])*int(ff[2])
        ftpResponse = ftpObject.delete(i);
        fi = i.split("$$")
        f1 = open("response_"+fi[0],"w")
        if re == 0:
            f1.write("Invalid Request")
        else:
            f1.write(str(result))
        f1.close()
        respMessage = ftpObject.storbinary("STOR "+("response_"+fi[0]), open(("response_"+fi[0]), 'rb'));
        os.remove(i)

def Increment(i):
    checkname = name+"$$request"
    if checkname in i:
        respMessage = ftpObject.retrbinary("RETR "+i, open(i, 'wb').write);
        print(i)
        ff = open(i,'r').read().split(";")
        print(ff)
        re=0
        if ff[1]=="++":
            re = 1
            result = int(ff[0])+int(ff[2])
        ftpResponse = ftpObject.delete(i);
        fi = i.split("$$")
        f1 = open("response_"+fi[0],"w")
        if re == 0:
            f1.write("Invalid Request")
        else:
            f1.write(str(result))
        f1.close()
        respMessage = ftpObject.storbinary("STOR "+("response_"+fi[0]), open(("response_"+fi[0]), 'rb'));
        os.remove(i)

a="0";

def handler(signum, frame):
    file = "sv0_"+name
    f = open("sv0_"+name,"w")
    f.write(name+"$$Remove$$"+a)
    f.close()
    respMessage = ftpObject.storbinary("STOR "+file, open(file, 'rb'));
    # os.remove(file)
    # if res == 'y':
    exit(1)
 
signal.signal(signal.SIGINT, handler)

while(flag):
    print("\nChoice operation:\n1 Add\n2 Subtract\n3 Multiply\n4 Increment\n")
    a = input()
    file = "sv0_"+name
    f = open("sv0_"+name,"w")
    if(a=="1"):
        f.write(name+"$$Add")
        f.close()
        respMessage = ftpObject.storbinary("STOR "+file, open(file, 'rb'));
        os.remove(file)
        while(True):
            time.sleep(3)
            lis = ftpObject.nlst()
            for i in lis:
                t= Thread(target = Addition,args=[i])
                t.start()
    if(a=="2"):
        f.write(name+"$$Subtract")
        f.close()
        respMessage = ftpObject.storbinary("STOR "+file, open(file, 'rb'));
        while(True):
            time.sleep(3)
            lis = ftpObject.nlst()
            for i in lis:
                t= Thread(target = Subtraction,args=[i])
                t.start()
                
    if(a=="3"):
        f.write(name+"$$Multiply")
        f.close()
        respMessage = ftpObject.storbinary("STOR "+file, open(file, 'rb'));
        while(True):
            time.sleep(3)
            lis = ftpObject.nlst()
            for i in lis:
                t= Thread(target = Multiplication,args=[i])
                t.start()

    if(a=="4"):
        f.write(name+"$$Inc")
        f.close()
        respMessage = ftpObject.storbinary("STOR "+file, open(file, 'rb'));
        while(True):
            time.sleep(3)
            lis = ftpObject.nlst()
            for i in lis:
                t= Thread(target = Increment,args=[i])
                t.start()
                
    if(a=="5"):
        f.write(name+"$$")
