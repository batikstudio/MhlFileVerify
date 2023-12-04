# ----------------------------------#
#             Verify Tab            #
#-----------------------------------#

import os
import subprocess
import time
from PySide6.QtWidgets import (QFileDialog, QLineEdit, QMessageBox, QStatusBar, QApplication)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QCoreApplication, Qt
from components.dialogs import dialogs, CustomDialogs
from components.SharedClasses import errors
import components.verifications

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
        file_name = os.path.basename(file_to_verify)
        binary = components.verifications.mhltool_bin
        
        if file_to_verify == "":
            QMessageBox.information(self.parent.window,"File not selected", "Please, select a file.")
        elif os.path.isdir(file_to_verify):
            QMessageBox.critical(self.parent.window,"Wrong selection", "Directories are not allowed. Please, select a valid MHL file.")
        elif not os.path.exists(file_to_verify):
            QMessageBox.information(self.parent.window,"File not found", "Missing file. Please, select a file.")
        else:
            try:
                self.parent.set_status_message("Analyzing files...")
                command_verify = f"./{binary} verify -v -f \'{file_to_verify}\'"
                start_process_time = time.time()
                exec_command_verify = subprocess.Popen(command_verify, shell=True, text=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                while exec_command_verify.poll() is None:
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
                standard_out, standard_error = exec_command_verify.communicate()
                verify_returncode = exec_command_verify.returncode
                title_error = f"Error: {verify_returncode}"
                print("Selected file", file_to_verify)
                self.parent.reset_status_message()
                QApplication.processEvents()
                
            except UnicodeDecodeError:
                QMessageBox.critical(self.parent.window,"Incorrect file", "Please, select a correct UTF-8 mhl file.")

                ####       SUCCESS       ####

            if verify_returncode == 0:

                title = "Successful"
                description = f"Verification Completed.\nTotal time --> {total_time}\nThe file {file_name} is correct."
                CustomDialogs.CustomSuccessDialog(self, title, description, standard_out)
                self.parent.set_status_message("Verification successful")
                QApplication.processEvents()
                self.parent.reset_status_message()
                QApplication.processEvents()
                print("------------------\nThe verify was correct!")
                

                ####       ERRORS       ####

            elif verify_returncode != 0:
                description_error = f"Error analyzing {file_name}.\n{errors.get_error_description(verify_returncode)}"
                CustomDialogs.CustomErrorDialog(self, title_error, description_error, standard_error)
                self.parent.set_status_message(f"Failed verification - {title_error}")
                QApplication.processEvents()
                self.parent.reset_status_message()
                QApplication.processEvents()

            else:
                QMessageBox.information(self.parent.window,"Unknown Error", "Unknown Error")
