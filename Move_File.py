

import sys
import time
import random

import os
import shutil





from_dir = "C:/Users/HP/Downloads/"
to_dir = "C:/Users/HP/OneDrive/Desktop/Documents"

list_dir = {
   
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt']
    
}
#print(list_dir)


class Move_File():

    def on_created(self, event):
     name,extension=os.path.splitext(event.src_path)
     time.sleep(1)
     for key,value in list_dir.items():
        time.sleep(1)
        if extension in value:
           file_name=os.path.basename(event.src_path)
           print("downloaded")
           path1=from_dir+'/'+file_name
           path2=to_dir+'/'+key
           path3=to_dir+'/'+key+'/'+file_name

           if os.path.exists(path2):
                print("Directory Exists...")
                print("Moving " + file_name + "....")
                shutil.move(path1, path3)
                time.sleep(1)

                        
           else:
                print("Making Directory...")
                os.makedirs(path2)
                print("Moving " + file_name + "....")
                shutil.move(path1, path3)
                time.sleep(1)

           
                    




    