import os
import datetime
import pywhatkit

inp=int(input("Enter a choice (1-4) : "))

if(inp==1):
    print(datetime.datetime.now())
elif(inp==2):
    path = "C:\\Users\\user\\Desktop"
    dir_list = os.listdir(path) 
    print("Files and directories in '", path, "' :")  
    # print the list 
    print(dir_list) 
elif(inp==3):
    directory = "PythonLinux"
    # Parent Directory path 
    parent_dir = "C:\\Users\\user\\Desktop"
    # Path 
    path = os.path.join(parent_dir, directory)
    os.mkdir(path) 
    print("Directory '% s' created" % directory) 
elif(inp==4):
    pywhatkit.sendwhatmsg("+918005524478","Ji!",20, 30)
    print("pywhatkit sent message succesfully!")
else:
    print("Enter valid input!")