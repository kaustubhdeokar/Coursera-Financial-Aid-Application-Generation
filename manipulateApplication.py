import traceback
import tkinter as tk
from tkinter import filedialog


def select_file_path():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()


def overwrite_file_content(file_content, field, handle):
    file_content = file_content.replace("____", field)
    file_content = file_content.replace("<github-handle>", handle)
    return file_content


if __name__ == "__main__":
    try:
        github_handle = input('enter your github handle: ')
        path = select_file_path()
        file_read = open(path, 'r')
        orig_content = file_read.read()
        file_read.close()
        file_write = open('application', 'w')
        topic = input('Enter the area you wish to apply for: ')
        content = overwrite_file_content(orig_content, topic, github_handle)
        file_write.write(content)
        file_write.close()
        print("Your script can be found in application text file")

    except FileNotFoundError:
        print(traceback.print_exc())
