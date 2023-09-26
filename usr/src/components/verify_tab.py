# -----------------------------------
#             Verify Tab
#------------------------------------

import os
import subprocess
from PySide6.QtWidgets import (QFileDialog, QLineEdit, QMessageBox, QStatusBar)
from PySide6.QtGui import QIcon, QPixmap
from components.dialogs import dialogs
from components.SharedClasses import errors

class verify_tab_class:

    def __init__(self, parent):
        self.parent = parent
        self.line_edit_file = self.parent.window.line_edit_file


    def select_mhl_file(self):
        default_dir = os.environ['HOME']
        selected_file = QFileDialog.getOpenFileName(self.parent, "Select file", default_dir, "MHL Files (*.mhl)")
        self.line_edit_file.setText(selected_file[0])


    def verify_mhl_file(self):
        file_to_verify = self.parent.window.line_edit_file.text()
        
        if file_to_verify == "":
            QMessageBox.information(self.parent.window,"File not selected", "Please, select a file.")
        elif os.path.isdir(file_to_verify):
            QMessageBox.critical(self.parent.window,"Wrong selection", "Directories are not allowed. Please, select a valid MHL file.")
        elif not os.path.exists(file_to_verify):
            QMessageBox.information(self.parent.window,"File not found", "Missing file. Please, select a file.")
        else:
            try:
                command_verify = f"./../bin/mhl verify -v -f \'{file_to_verify}\'"
                exec_command_verify = subprocess.run(command_verify, shell=True, text=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                verify_returncode = exec_command_verify.returncode
                title_error = f"Error: {verify_returncode}"
                print("Selected file", file_to_verify)
                # print(command_verify)
            except UnicodeDecodeError:
                QMessageBox.critical(self.parent.window,"Incorrect file", "Please, select a correct UTF-8 mhl file.")

                ####       SUCCESS       ####

            if verify_returncode == 0:
                standard_out = exec_command_verify.stdout
                title = "Successful"
                description = f"Verification Completed. The file {file_to_verify} is correct."
                dialogs.SuccessDialog(self, title, description, standard_out)
                print("------------------\nThe verify was correct!")
                self.parent.set_status_message("Verification successful")

                ####       ERRORS       ####

            elif verify_returncode != 0:
                standard_error = exec_command_verify.stderr
                description_error = errors.get_error_description(verify_returncode)
                InformativeText = ""
                self.parent.set_status_message(f"Failed verification - {title_error}")
                dialogs.ErrorDialog(self, title_error, description_error, standard_error, None)
            else:
                QMessageBox.information(self.parent.window,"Unknown Error", "Unknown Error")
