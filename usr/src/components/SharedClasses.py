import os, sys
import configparser
from PySide6.QtWidgets import QMessageBox

# Get config params from ini file

class ConfigFile:
    global CONFIG_FILE, config
    
    CONFIG_FILE = "../etc/config.ini"

    def verify_config_file():
        if os.path.exists(CONFIG_FILE):
            # Verify if exist config file and print in terminal
            print(f"The config file {CONFIG_FILE} was found")
        else:
            # If config file not exist, show an error dialog
            message = f"The config file {CONFIG_FILE} couldn't be found.."
            QMessageBox.critical(None, "Error", message)
            #app.exec()

    def get_config():
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        return config

# Get error descriptions from mhltool list of errors 

class errors:
    def get_error_description(error_code):

        error_output = ""

        error_list = {
        1: "Unknown error.",
        2: "Wrong or incompatible arguments are passed.",
        3: "File does not exist.",
        4: "IO error occured.",
        5: "Out of memory.",
        6: "Wrong or incompatible input data.",
        7: "Unknown time format.",
        8: "Internal error occured.",
        9: "Wrong file location.",
        10: "MHL file is not found. Verify URL",
        11: "Wrong or unsupported MHL file format. Select a correct file format.",
        12: "The code is not used, probably reserved for future.",
        13: "File not found.",
        14: "Error in crypto library occured.",
        15: "Real file size and the size contained in MHL file record are not equal.",
        16: "Calculated hash of file and hash from corresponding MHL file record are not equal.",
        17: "One or more items of MHL file contain an unsupported hash encoding.",
        18: "Error during conversion of character encodings.",
        19: "Unknown mode.",
    #   20: "Functionality is not implemented yet.",
        21: "Search stopped.",
        22: "Invalid sequence specification. Format: <start of file name>#...#<number1>-<number2><end of file name>",
        23: "Gap detected in the file sequence. One or more files are missing or can't be opened.",
        24: "File is not listed in MHL file.",
        127: "Error while loading shared libraries"
        }
        
        if error_code not in error_list.keys():
            error_output = "Unknown error."
        else:
            error_output = error_list[error_code]

        return error_output
