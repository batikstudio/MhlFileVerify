# -----------------------------------
#             Seal Tab
#------------------------------------

import os
import subprocess
from PySide6.QtWidgets import (QFileDialog, QLineEdit, QMessageBox, QStatusBar, QComboBox, QApplication)
from components.dialogs import dialogs
from components.SharedClasses import errors
import components.verifications

class seal_tab_class:

    def __init__(self, parent):
        #super().__init__()
        self.parent = parent
        self.hash_type = self.parent.window.comboBox_checksum
        self.dir_to_seal = self.parent.window.line_edit_directory

    def select_dir_seal(self):
        default_dir = os.environ['HOME']
        selected_dir = QFileDialog.getExistingDirectory(self.parent.window, "Select a directory to seal", default_dir)
        self.dir_to_seal.setText(selected_dir)
        print("- Selected dir", selected_dir)

    def show_message(self):
        self.parent.set_status_message("Analyzing files... Please, wait")

    def launch_seal(self):
        dir_to_seal = self.parent.window.line_edit_directory.text()
        hash_type = self.hash_type.currentText()
        binary = components.verifications.mhltool_bin
        self.parent.set_status_message("Analyzing folder... Please, wait")
        QApplication.processEvents() # Update UI

        if dir_to_seal == "":
            QMessageBox.information(self.parent.window,"Directory not selected", "Please, select a directory.")
        elif not os.path.exists(dir_to_seal):
            QMessageBox.information(self.parent.window,"Directory not found", "Missing file. Please, select a correct path.")
        elif os.path.isfile(dir_to_seal):
            QMessageBox.critical(self.parent.window,"Wrong selection", "Files are not allowed. Please, select a valid directory.")
        else:
            command_seal = f"./{binary} seal -v -t \'{hash_type}\' -o \'{dir_to_seal}\' \'{dir_to_seal}\'"
            print(command_seal)
            exec_command_seal = subprocess.run(command_seal, shell=True, text=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            seal_returncode = exec_command_seal.returncode
            
            if seal_returncode == 0:
                standard_out = exec_command_seal.stdout
                title = "Successful"
                description = f"The seal process was successful. Mhl file created in {dir_to_seal}"
                self.parent.set_status_message("Seal successful")
                dialogs.SuccessDialog(self, title, description, standard_out)
                print("------------------\nThe seal was correct!")

            elif seal_returncode != 0:
                standard_error = exec_command_seal.stderr
                title_error = f"Error: {seal_returncode}"
                description_error = errors.get_error_description(seal_returncode)
                InformativeText = ""
                self.parent.set_status_message(f"Failed verification - {title_error}")
                dialogs.ErrorDialog(self, title_error, description_error, standard_error, None)
                print(title_error)
            else:
                QMessageBox.information(self.parent.window,"Unknown Error", "Unknown Error")
    
