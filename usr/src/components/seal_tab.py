# ----------------------------------#
#             Seal Tab              #
#-----------------------------------#

import os
import subprocess
import time
from PySide6.QtWidgets import (QFileDialog, QLineEdit, QMessageBox, QStatusBar, QComboBox, QApplication)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QCoreApplication, Qt
from components.dialogs import dialogs, CustomDialogs
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

    def launch_seal(self):
        dir_to_seal_raw = self.parent.window.line_edit_directory.text()
        # Next line avoid double slash problem in MacOS
        dir_to_seal = dir_to_seal_raw[:-1] if dir_to_seal_raw.endswith("/") else dir_to_seal_raw
        hash_type = self.hash_type.currentText()
        binary = components.verifications.mhltool_bin


        if dir_to_seal == "":
            QMessageBox.information(self.parent.window,"Directory not selected", "Please, select a directory.")
        elif not os.path.exists(dir_to_seal):
            QMessageBox.information(self.parent.window,"Directory not found", "Missing file. Please, select a correct path.")
        elif os.path.isfile(dir_to_seal):
            QMessageBox.critical(self.parent.window,"Wrong selection", "Files are not allowed. Please, select a valid directory.")
        else:
            self.parent.set_status_message("Analyzing folder...")
            QApplication.processEvents() # Update UI
            command_seal = f"./{binary} seal -v -t \'{hash_type}\' -o \'{dir_to_seal}\' \'{dir_to_seal}\'"
            print(command_seal)
            start_process_time = time.time()
            exec_command_seal = subprocess.Popen(command_seal, shell=True, text=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            
            while exec_command_seal.poll() is None:
                dialogs.AnalyzingDialog
                self.parent.window.button_create.setEnabled(False)
                QApplication.processEvents()
                time.sleep(0.5)
                self.parent.set_status_message("Analyzing files")
                QApplication.processEvents()
                time.sleep(0.5)
                self.parent.set_status_message("Analyzing files.")
                QApplication.processEvents()
                time.sleep(0.5)
                self.parent.set_status_message("Analyzing files..")
                QApplication.processEvents()
                time.sleep(0.5)
                self.parent.set_status_message("Analyzing files...")
            
            end_process_time = time.time()
            total_time = time.strftime("%H:%M:%S", time.gmtime(end_process_time - start_process_time))
            standard_out, standard_error = exec_command_seal.communicate()
            seal_returncode = exec_command_seal.returncode
            self.parent.window.button_create.setEnabled(True)

                            
            if seal_returncode == 0:
                title = "Successful"
                description = f"The seal process was successful.\nTotal time --> {total_time}\nMhl file created in:\n{dir_to_seal}"
                CustomDialogs.CustomSuccessDialog(self, title, description, standard_out)
                self.parent.set_status_message("Seal successful")
                QApplication.processEvents()
                self.parent.reset_status_message()
                QApplication.processEvents()
                print("------------------\nThe seal was correct!")

            elif seal_returncode != 0:
                title_error = f"Error: {seal_returncode}"
                description_error = errors.get_error_description(seal_returncode)
                CustomDialogs.CustomErrorDialog(self, title_error, description_error, standard_error)
                self.parent.set_status_message(f"Failed sealing process - {title_error}")
                QApplication.processEvents()
                self.parent.reset_status_message()
                QApplication.processEvents()
                print(title_error)
            else:
                QMessageBox.information(self.parent.window,"Unknown Error", "Unknown Error")
    
