from ftplib import FTP
import os
import time
import sys
from threading import Thread
url = input("URL : ").split(":")
flag=True
ftpObject = FTP();
dict = {'key':{'value1','value2'}}
dict['Add']=set()
dict['Subtract']=set()
dict['Multiply']=set()
dict['Inc']=set()
ftpResponseCode = ftpObject.connect(host=(url[0]), port=int(url[1]));
print("Response code for connect:%s"%ftpResponseCode)

username = input("Username : ")
password = input("Password : ")
name = sys.argv[1]
ftpResponseCode = ftpObject.login(username,password);
print("Response code for login:%s"%ftpResponseCode)

f = open("Add.txt","w")
f2 = open("Subtract.txt","w")
f3 = open("Multiply.txt","w")
f4 = open("Inc.txt","w")
respMessage = ftpObject.storbinary("STOR "+"Add.txt", open("Add.txt", 'rb'));
respMessage = ftpObject.storbinary("STOR "+"Subtract.txt", open("Subtract.txt", 'rb'));
respMessage = ftpObject.storbinary("STOR "+"Multiply.txt", open("Multiply.txt", 'rb'));
respMessage = ftpObject.storbinary("STOR "+"Inc.txt", open("Inc.txt", 'rb'));
f.close()
f4.close()
f3.close()
f2.close()

def check():
    time.sleep(4)
    while(flag):
        lis = ftpObject.nlst()
        for i in lis:
            checkname = name+"_server"
            checkname1 = name+"request_"
            if checkname in i:
                respMessage = ftpObject.retrbinary("RETR "+i, open(i, 'wb').write);
                f = open(i,"r")
                us = open(i,"r").read().split("$$")#change
                if(us[1] == "Add"):
                    (dict[us[1]]).add(us[0])
                    print(dict)
                    f1 = open("Add.txt","w")
                    f1.write(str(dict[us[1]])+"\n")
                    f1.close()
                    ftpObject.delete(i);
                    respMessage = ftpObject.storbinary("STOR "+"Add.txt", open("Add.txt", 'rb'));
                if(us[1] == "Subtract"):
                    dict[us[1]].add(us[0])
                    print(dict)
                    f1 = open("Subtract.txt","w")
                    f1.write(str(dict[us[1]])+"\n")
                    f1.close()
                    ftpObject.delete(i);
                    respMessage = ftpObject.storbinary("STOR "+"Subtract.txt", open("Subtract.txt", 'rb'));
                if(us[1] == "Multiply"):
                    dict[us[1]].add(us[0])
                    print(dict)
                    f1 = open("Multiply.txt","w")
                    f1.write(str(dict[us[1]])+"\n")
                    f1.close()
                    ftpObject.delete(i);
                    respMessage = ftpObject.storbinary("STOR "+"Multiply.txt", open("Multiply.txt", 'rb'));
                if(us[1] == "Inc"):
                    dict[us[1]].add(us[0])
                    print(dict)
                    f1 = open("Inc.txt","w")
                    f1.write(str(dict[us[1]])+"\n")
                    f1.close()
                    ftpObject.delete(i);
                    respMessage = ftpObject.storbinary("STOR "+"Inc.txt", open("Inc.txt", 'rb'));
                if(us[1] == "Remove"):
                    if(us[2]=="1"):
                        if us[0] in dict['Add']:
                            dict['Add'].remove(us[0])
                            print(dict)
                            f1 = open("Add.txt","w")
                            f1.write(str(dict["Add"])+"\n")
                            f1.close()
                            ftpObject.delete(i);
                            respMessage = ftpObject.storbinary("STOR "+"Add.txt", open("Add.txt", 'rb'));
                    if(us[2]=="2"):
                        if us[0] in dict['Subtract']:
                            dict['Subtract'].remove(us[0])
                            print(dict)
                            f1 = open("Subtract.txt","w")
                            f1.write(str(dict["Subtract"])+"\n")
                            f1.close()
                            ftpObject.delete(i);
                            respMessage = ftpObject.storbinary("STOR "+"Subtract.txt", open("Subtract.txt", 'rb'));
                    if(us[2]=="3"):
                        if us[0] in dict['Multiply']:
                            dict['Multiply'].remove(us[0])
                            print(dict)
                            f1 = open("Multiply.txt","w")
                            f1.write(str(dict["Multiply"])+"\n")
                            f1.close()
                            ftpObject.delete(i);
                            respMessage = ftpObject.storbinary("STOR "+"Multiply.txt", open("Multiply.txt", 'rb'));
                    if(us[2]=="4"):
                        if us[0] in dict['Inc']:
                            dict['Inc'].remove(us[0])
                            print(dict)
                            f1 = open("Inc.txt","w")
                            f1.write(str(dict["Inc"])+"\n")
                            f1.close()
                            ftpObject.delete(i);
                            respMessage = ftpObject.storbinary("STOR "+"Inc.txt", open("Inc.txt", 'rb'));
                    
                f.close()

t = Thread(target= check , args=())
t.start()

while(True):
    a=input()
    if(a=="LOOKUP"):
        print("Add: ", dict['Add'])
        print("Subtract: ", dict['Subtract'])
        print("Multply: ", dict['Multiply'])
        print("Increment: ", dict['Inc'])
