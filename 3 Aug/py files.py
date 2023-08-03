 
import os
import shutil

os.mkdir("pyt")

# Loop through all the files in the current directory
for file in os.listdir(r'C:\\Users\\user\\Desktop'):
    # Check if the file has the .mp3 extension
    if file.endswith(".py"):
        # Copy the file to the new directory
        shutil.copy(file, "pyt",'C:\\Users\\user\\Desktop')
