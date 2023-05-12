from ftplib import FTP
import os
import time
import sys
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

res = [0 , 0]
session=1
sessionLimit = 1

while(True):
    print("\nChoice :\n1 Operation\n2 Change session\n3 Quit\n4 Create Another Session\n5 Response\n")
    a = input()
    if(a=="1"):
        c = input("\nChoice operation:\n1 Add\n2 Subtract\n3 Multiply\n4 Increment\n5 Quit\n")
        
        if(c == "1"):
            file="Add.txt"
            respMessage = ftpObject.retrbinary("RETR "+"Add.txt", open("Add.txt", 'wb').write);
            print(open(file,"r").read())
            ser = input("Enter server to connect: ")
            input1 = input("Enter First Integer")
            input2 = input("Enter Second Integer")
            ff = name+"_session_"+str(session)+"_"+ser+"$$request"
            f = open(ff,'w')
            f.write(input1+";+;"+input2)
            f.close()
            respMessage = ftpObject.storbinary("STOR "+ff, open(ff, 'rb'));
        if(c == "2"):
            file="Subtract.txt"
            respMessage = ftpObject.retrbinary("RETR "+"Subtract.txt", open("Subtract.txt", 'wb').write);
            print(open(file,"r").read())
            ser = input("Enter server to connect: ")
            input1 = input("Enter First Integer")
            input2 = input("Enter Second Integer")
            ff = name+"_session_"+str(session)+"_"+ser+"$$request"
            f = open(ff,'w')
            f.write(input1+";-;"+input2)
            f.close()
            respMessage = ftpObject.storbinary("STOR "+ff, open(ff, 'rb'));
        if(c == "3"):
            file="Multiply.txt"
            respMessage = ftpObject.retrbinary("RETR "+"Multiply.txt", open("Multiply.txt", 'wb').write);
            print(open(file,"r").read())
            ser = input("Enter server to connect: ")
            input1 = input("Enter First Integer")
            input2 = input("Enter Second Integer")
            ff = name+"_session_"+str(session)+"_"+ser+"$$request"
            f = open(ff,'w')
            f.write(input1+";*;"+input2)
            f.close()
            respMessage = ftpObject.storbinary("STOR "+ff, open(ff, 'rb'));
        if(c == "4"):
            file="Inc.txt"
            respMessage = ftpObject.retrbinary("RETR "+"Inc.txt", open("Inc.txt", 'wb').write);
            print(open(file,"r").read())
            ser = input("Enter server to connect: ")
            input1 = res[int(session)]
            input2 = "1"
            ff = name+"_session_"+str(session)+"_"+ser+"$$request"
            f = open(ff,'w')
            f.write(input1+";++;"+input2)
            f.close()
            respMessage = ftpObject.storbinary("STOR "+ff, open(ff, 'rb'));
        if(c == "5"):
            break

    if(a=="99"):
        file="Servers.txt"
        respMessage = ftpObject.retrbinary("RETR "+"Servers.txt", open("Servers.txt", 'wb').write);
        print(open(file,"r").read())
    if(a=="2"):
        session=input("Enter session no.")
    if(a=="3"):
        break;
    if(a=="4"):
        res.append(0)
        sessionLimit+=1
    if(a=="5"):
        lis = ftpObject.nlst()
        for i in lis:
            checkname1 = "response_"+name
            if checkname1 in i:
                respMessage = ftpObject.retrbinary("RETR "+i, open(i, 'wb').write);
                print(i)
                res[int(i.split("_")[3])] = open(i,'r').read()
                # time.sleep(3)
                ftpObject.delete(i)  ## Comment for same client in different terminal
        print(res[int(session)])
