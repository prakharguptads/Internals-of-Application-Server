from ftplib import FTP
import socket
import os

url = input("URL : ").split(":")

ftpObject = FTP();

ftpResponseCode = ftpObject.connect(host=(url[0]), port=int(url[1]));
print("Response code for connect:%s"%ftpResponseCode)

username = input("Username : ")
password = input("Password : ")

name = input("Enter your name:")

ftpResponseCode = ftpObject.login(username,password);
print("Response code for login:%s"%ftpResponseCode)

while(True):
    print("\nChoice:\n1 List Messages\n2 Download a File\n3 Send a File\n4 Print in Byte Format\n5 Change Directory\n6 Quit\n7 Send Message\n8 List Users\n9 WHO AM I\n")
    a=input()
    if(a=="1"):
        lis = ftpObject.nlst()
        for i in lis:
            if name in i:
                print(i)
        #ftpResponseCode = ftpObject.retrlines("LIST", print);
        print("Response code for command LIST:%s"%ftpResponseCode);
    
    if(a=="2"):
        file = input("Enter Filename: ")
        respMessage = ftpObject.retrbinary("RETR "+file, open(file, 'wb').write);
        print(respMessage);
        
    if(a=="3"):
        file = input("Enter Filename: ")
        respMessage = ftpObject.storbinary("STOR "+file, open(file, 'rb'));
        print(respMessage);
        
    if(a=="4"):
        file = input("Enter Filename: ")
        respMessage = ftpObject.retrbinary("RETR "+file, print);
       
    if(a=="5"):
        file = input("Enter Directory: ")
        ftpObject.cwd(file)
        ftpObject.retrlines("LIST")
        
    if(a=="6"):
        respMessage = ftpObject.quit();
        print(respMessage)
        break
        
    if(a=="7"):
        file = input("Enter Reciever Name: ")
        f = open(name+file,"a")
        msg = input("Enter Message: ")
        f.write(name+"-->"+msg+"\n")
        f.close()
        respMessage = ftpObject.storbinary("STOR "+(name+file), open((name+file), 'rb'));
        print(respMessage);
        
    if(a=="8"):
        file = "Users"
        respMessage = ftpObject.retrbinary("RETR "+file, open(file, 'ab').write);
        f = open(file,"a")
        f.write(name+"\n")
        respMessage = ftpObject.storbinary("STOR "+file, open(file, 'rb'));
        f.close()
        print(open("Users",'r').read())
    if(a=="9"):
        print(name)
