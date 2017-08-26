from appJar import gui
from FileCreation import create_file
init_buttons = [
    "Continue",
    "Quit"
]


def launch(button, app):
    if button == "Quit":
        quit()
    # get file location
    else:
        file_name = "RecognitionFile"
        file_dir = None
        app.infoBox(title="noBox", message="Blue box")
        print('going')
        quit()
    # launch API


def create_gui():
    app = gui()
    msg = "This utility will create two recognition files. \nOne for givers and one for receivers."
    app.addLabel(title="label_box", text=msg)
    app.addLabelEntry(title="API Launcher")
    app.addHorizontalSeparator()
    app.addButtons(
        names=init_buttons,
        funcs=launch
    )
    app.go()


create_gui()
