import os
import time
import getpass
user = getpass.getuser()
time.sleep(2)
target = '\Desktop'
os.chdir("C:\\Users")
os.chdir("C:\\Users"+"\\"+user+target)
attack = 0
while attack <= 1000:
    Rattack = str(attack)
    directory = "Malicious Folder"+Rattack
    print(directory)
    if os.path.exists(directory) == True:
        pass
    else:
        os.mkdir("Malicious Folder"+Rattack)
    attack = attack+1
