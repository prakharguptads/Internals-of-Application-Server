from ftplib import FTP
import os
import time
from threading import Thread

url = input("URL : ").split(":")
flag=True
ftpObject = FTP();
dict = {}
ftpResponseCode = ftpObject.connect(host=(url[0]), port=int(url[1]));
print("Response code for connect:%s"%ftpResponseCode)

username = input("Username : ")
password = input("Password : ")
# while(True):
#     print("Enter Your Choice:\n1: Login\n2: Signup")
#     a=input()
#     if(a==1):
name = input("Enter your Username:")
pass1 = input("Enter your Password:")

ftpResponseCode = ftpObject.login(username,password);#change
print("Response code for login:%s"%ftpResponseCode)

def Listening():
    # while(True):
    lis = ftpObject.nlst()
    for i in lis:
        checkname = name+"_request"
        checkname1 = "response_"+name
        if checkname in i:
            respMessage = ftpObject.retrbinary("RETR "+i, open(i, 'wb').write);
            print(i)
            ff = open(i,'r').read().split(";")
            print(ff)
            if ff[1]=="+":
                result = int(ff[0])+int(ff[2])
            if ff[1]=="-":
                result = int(ff[0])-int(ff[2])
            if ff[1]=="*":
                result = int(ff[0])*int(ff[2])
            if ff[1]=="/": 
                result = int(ff[0])/int(ff[2])
            if ff[1]=="^":
                result = int(ff[0])^int(ff[2])
            ftpResponse = ftpObject.delete(i);
            sendname = i.split("_")
            f = open(sendname[2]+"_response_"+sendname[0],"w")
            f.write(name + " Response: "+str(result))
            f.close()
            respMessage = ftpObject.storbinary("STOR "+(sendname[2]+"_response_"+sendname[0]), open((sendname[2]+"_response_"+sendname[0]), 'rb'));
            os.remove(i)
            # print(respMessage);
        if checkname1 in i:
            respMessage = ftpObject.retrbinary("RETR "+i, open(i, 'wb').write);
            print(open(i,'r').read())
            # respMessage = ftpObject.retrbinary("RETR "+i, print);
            ftpResponse = ftpObject.delete(i);
            os.remove(i)
    #ftpResponseCode = ftpObject.retrlines("LIST", print);
    # print("Response code for command LIST:%s"%ftpResponseCode);
def Listening1():
    while(flag):
        time.sleep(4)
        Listening()
t = Thread(target=Listening1,args=())
t.start()
while(flag):
    print("\nChoice:\n1 List Messages\n2 Send Message\n3 List Users\n4 Quit\n")
    a=input()
    if(a=="1"):
        lis = ftpObject.nlst()
        for i in lis:
            if name in i:
                print(i)
        #ftpResponseCode = ftpObject.retrlines("LIST", print);
        print("Response code for command LIST:%s"%ftpResponseCode);
        
    if(a=="2"):
        file = input("Enter Reciever Name: ")
        if file in dict:
            dict[file]+=1
            f = open(name+file+"_request_"+str(dict[file]),"w")
            msg1 = input("Enter 1st Number: ")
            msg2 = input("Enter 2st Number: ")
            msg3 = input("Enter Operation: ")
            msg = msg1+";"+msg3+";"+msg2
            f.write(msg+"\n")
            f.close()
            respMessage = ftpObject.storbinary("STOR "+(name+file+"_request_"+str(dict[file])), open((name+file+"_request_"+str(dict[file])), 'rb'));
            print(respMessage);
            os.remove(name+file+"_request_"+str(dict[file]))
        else:
            dict[file]=1
            f = open(name+file+"_request_1","w")
            msg1 = input("Enter 1st Number: ")
            msg2 = input("Enter 2st Number: ")
            msg3 = input("Enter Operation: ")
            msg = msg1+";"+msg3+";"+msg2
            f.write(msg+"\n")
            f.close()
            respMessage = ftpObject.storbinary("STOR "+(name+file+"_request_1"), open((name+file+"_request_1"), 'rb'));
            print(respMessage);
            os.remove(name+file+"_request_1")
        
    if(a=="3"):
        file = "Users.txt"
        respMessage = ftpObject.retrbinary("RETR "+file, open(file, 'wb').write);
        f = open(file,"a")
        us = open(file,"r").read().split("\n")
        if name not in us:
            f.write(name+"\n")
        f.close()
        respMessage = ftpObject.storbinary("STOR "+file, open(file, 'rb'));
        print(open("Users.txt",'r').read())
    
    if(a=="4"):
        # respMessage = ftpObject.quit();
        # print(respMessage)
        flag=False
        break
t.join()
exit()
