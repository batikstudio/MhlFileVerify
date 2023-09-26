from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QPixmap, QIcon

class dialogs:

    def __init__(self, parent):
        self.parent = parent

    def SuccessDialog(self, title, description, detailed_text):
        success_window = QMessageBox(self.parent.window)
        success_window.resize(800, 800)
        success_window.setFixedSize(800, 800)
        success_window_icon = QPixmap("../share/icons/success.png")
        success_window.setIconPixmap(success_window_icon)
        success_window.setText(description)
        #success_window.setInformativeText("This is additional information")
        success_window.setWindowTitle(title)
        success_window.setDetailedText(detailed_text)
        success_window.setStandardButtons(QMessageBox.Ok)
        success_window.exec()

    def ErrorDialog(self, title, description_error, standard_error, InformativeText):
        error_window = QMessageBox(self.parent.window)
        error_window.resize(800, 800)
        error_window.setFixedSize(800, 800)
        error_window.setIcon(QMessageBox.Critical)
        error_window.setText(description_error)
        error_window.setInformativeText(InformativeText)
        error_window.setWindowTitle(title)
        error_window.setDetailedText(standard_error)
        error_window.setStandardButtons(QMessageBox.Ok)
        error_window.exec()


    def AboutDialog(self):
        with open("../share/doc/about_licenses.txt", "r") as f:
            file_about_licenses = f.read()
        about_window = QMessageBox(self.parent.window)
        # about_window.setStyleSheet("QLabel{font-style: Open Sans Light; font-size: 20px;}")
        logo_batik = QPixmap("../share/icons/app_logo_128x128.png")
        about_window.setWindowTitle("About MHL File Verify")
        about_window.setText("""Version: 0.2\n
Simple tool to verify mhl hash files\n
This software is licensed under the GNU General Public License v3.0 (GPLv3).\n
This software includes a binary from third-party mhltool by Pomfort licensed under the MIT License.\n
Developer: Batik Studio - Víctor Zamora.\n
More info batikstudio.com\n
info@batikstudio.com""")
        #print(file_about_licenses)
        about_window.setDetailedText(file_about_licenses)
        about_window.setIconPixmap(logo_batik)
        about_window.setStandardButtons(QMessageBox.Ok)
        about_window.exec()
        
    def ShortcutsDialog(self):
        shortcut_window = QMessageBox(self.parent.window)
        shortcut_window.setWindowTitle("ShortCuts")
        shortcut_window.setText("""
Ctrl + O - Open MHL file
F5 - Verify file
Ctrl + N - Create a mhl file from selected dir
Ctrl + Q - Quit""")
        shortcut_window.setIcon(QMessageBox.Information)
        shortcut_window.setStandardButtons(QMessageBox.Ok)
        shortcut_window.exec()
