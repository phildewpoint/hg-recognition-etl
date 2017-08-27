from appJar import gui
from FileCreation import create_file
from recETL import rec_etl
import datetime
init_buttons = [
    "Continue",
    "Quit"
]
today = datetime.date.today()


def launch(button):
    # add error handling for missing values
    if button == "Quit":
        app.stop()
    # if the value doesn't exit (False) fire this warning
    elif not app.getEntry(name="dir_msg_box"):
        app.errorBox(title="ERROR: Missing Critical information", message="Please select a directory before continuing")
    elif not app.getEntry("Client Key"):
        app.errorBox(title="ERROR: Missing Critical information", message="Please enter an API key before continuing.")
    # get file location
    else:
        # initialize variables and create file
        file_name = "RecognitionFile"
        file_dir = app.getEntry(name="dir_msg_box")
        file = create_file(file_name=file_name, file_dir=file_dir)
        # get date values
        start_date = app.getDatePicker("dp_start")
        end_date = app.getDatePicker("dp_end")
        # get API key
        client_key = app.getLabel(name="Client Key")
        # launch functions to manage APIs and writing into file
        rec_etl(file=file, client_key=client_key, start=start_date, end=end_date)


def create_gui():
    # text variables to populate messages
    msg = "This utility will create two recognition files. \nOne for givers and one for receivers."
    key_msg = "Add your client or API key."
    dir_msg = "Select the directory for where you'll store the recognition file."
    date_msg = "Select the start and stop dates to extract recognitions."
    app.setLabelFont(size="14")
    # Header message
    app.addLabel(title="label_box", text=msg)
    app.addHorizontalSeparator()
    # API key box
    app.addLabel(title="key_label", text=key_msg)
    app.addLabelEntry(title="Client Key")
    app.addHorizontalSeparator()
    # date picker boxes
    app.addLabel(title="date_label", text=date_msg)
    app.startLabelFrame(title="Start Date")
    app.addDatePicker(name="dp_start")
    app.setDatePickerRange(title="dp_start", startYear=(today.year - 1), endYear=today.year)
    app.setDatePicker(title="dp_start", date=today)
    app.stopLabelFrame()
    app.startLabelFrame(title="End Date")
    app.addDatePicker(name="dp_end")
    app.setDatePickerRange(title="dp_end", startYear=(today.year - 1), endYear=today.year)
    app.setDatePicker(title="dp_end", date=today)
    app.stopLabelFrame()
    app.addHorizontalSeparator()
    # directory picker box
    app.addLabel(title="dir_label", text=dir_msg)
    app.addDirectoryEntry(title="dir_msg_box")
    app.addHorizontalSeparator()
    app.addButtons(
        names=init_buttons,
        funcs=launch
    )
    app.go()


# Create the GUI as a global
app = gui(title="Recognition Extract Utility")
create_gui()
