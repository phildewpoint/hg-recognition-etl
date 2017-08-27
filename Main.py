from appJar import gui
from FileCreation import create_file
from recETL import rec_etl
init_buttons = [
    "Continue",
    "Quit"
]


def launch(button):
    if button == "Quit":
        quit()
    # get file location
    else:
        # initialize variables and create file
        file_name = "RecognitionFile"
        file_dir = app.directoryBox(title="dir_msg_box")
        file = create_file(file_name=file_name, file_dir=file_dir)
        # get API key
        client_key = app.getLabel(name="Client Key")
        # launch functions to manage APIs and writing into file
        rec_etl(file=file, client_key=client_key)


def create_gui():
    msg = "This utility will create two recognition files. \nOne for givers and one for receivers."
    dir_msg = "Select the directory for where you'll store the recognition file."
    app.addLabel(title="label_box", text=msg)
    app.addLabelEntry(title="Client Key")
    app.addLabel(title="dir_label", text=dir_msg)
    app.addDirectoryEntry(title="dir_msg_box")
    app.addHorizontalSeparator()
    app.addButtons(
        names=init_buttons,
        funcs=launch
    )
    app.go()


# Create the GUI as a global
app = gui(title="Recognition Extract Utility", geom="265x125")
create_gui()
