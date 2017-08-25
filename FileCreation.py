import datetime, os

def create_file(api_name=None,):
    """This function will take """
    mydir = app.directoryBox(title="myDirectory")
    if mydir is None:
        quit()
    else:
        file_name = api_name + datetime.date.today().strftime("%d%m%Y")
        file_path = os.path.join(mydir, file_name)
        file = open(file_path, mode='w')
        return file
