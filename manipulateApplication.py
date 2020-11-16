import traceback
import tkinter as tk
from tkinter import filedialog

def select_file_path():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def overwrite_file_content(content,topic,github_handle):
    content = content.replace("____",topic)
    content = content.replace("<github-handle>",github_handle)
    return content

    
try:
    github_handle = input('enter your github handle')
    path = select_file_path()
    file_read = open(path,'r')
    orig_content = file_read.read()
    file_read.close()
    file_write = open(path,'w')
    topic = input('Enter the area you wish to apply for')
    content = overwrite_file_content(orig_content,topic,github_handle)
    file_write.write(content)
    file_write.close()
    print("If you want to use this again, copy the text in refresh file in courseraApp file")

except Exception:
    print('Check exception occured')
    print(traceback.print_exc())


