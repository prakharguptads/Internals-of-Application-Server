from ftplib import FTP

url = input("URL : ").split(":")

ftpObject = FTP();

ftpResponseCode = ftpObject.connect(host=(url[0]), port=int(url[1]));
print("Response code for connect:%s"%ftpResponseCode)

username = input("Username : ")
password = input("Password : ")

ftpResponseCode = ftpObject.login(username,password);
print("Response code for login:%s"%ftpResponseCode)

while(True):
    print("\nChoice:\n1 List Files\n2 Download a File\n3 Upload a File\n4 Print File in Byte Format\n5 Change Directory\n6 Quit")
    a=input()
    if(a=="1"):
        ftpResponseCode = ftpObject.retrlines("LIST", print);
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
