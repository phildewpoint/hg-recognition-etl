import datetime
import os
from appJar import gui


def create_file(file_name, file_dir):
    """This function will take a name and directory and return a file object.
    
    
    Keyword arguments:
    file_name -- name of a file to save (str)
    file_dir -- directory path where the file is saved (str)
    """

    if file_name is None or file_dir is None:
        msg = "The file you're trying to save is missing a directory or name. Please try the program again"
        app = gui()
        app.errorBox(title="Missing Key Information", message=msg)
        app.go()
        app.stop()
        quit()
    else:
        file_name = file_name + datetime.date.today().strftime("%d%m%Y")
        file_path = os.path.join(file_dir, file_name)
        file = open(file_path, mode='w')
        return file
