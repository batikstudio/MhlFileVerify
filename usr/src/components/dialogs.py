from PySide6.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextBrowser, QScrollBar, QSpacerItem
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt

version_MhlFileVerify = "0.4"

class dialogs:

    def __init__(self, parent):
        self.parent = parent

    def SuccessDialog(self, title, description, detailed_text):
        success_window = QMessageBox(self.parent.window)
        success_window_icon = QPixmap("../share/icons/success.png")
        success_window.setIconPixmap(success_window_icon)
        success_window.setText(description)
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



class CustomDialogs:
    def __init__(self, parent):
        self.parent = parent

        global common_style
        common_style = """
            QDialog {
                background-color: rgb(28, 28, 32);
                selection-color: rgb(246, 97, 81);
                font: 11pt "Open Sans Regular";
                color: rgb(200,200,200);
                selection-background-color: rgb(20,20,20);
                }
                
            QLabel {
                color: rgb(180,180,180);
                }
                
            QTextBrowser {
                  background-color: rgb(30,30,40);
                  selection-color: rgb(246, 97, 81);
                  font: bold 10pt;
                  color: rgb(200,200,200);
                  selection-background-color: rgb(20,20,20);
                  border-style: outset;
                  border-width: 1px;
                  border-radius: 5px;
                  border-color: rgb(50,50,60);
                  padding: 6px;
                }
            QPushButton {
                    background-color:rgb(50, 50, 55);
                    color: white;
                    border: none;
                    padding: 5px 10px;
                    text-align: center;
                    text-decoration: none;
                    font-size: 16px;
                    margin: 4px 2px;
                    border-radius: 6px;
                }

            QPushButton::hover {
                    background-color: rgb(60, 60, 65);
                }

             QScrollBar {
                 background: rgb(30,30,40);
                 width: 10px;
                 margin: 0;
             }
             
             QScrollBar::handle {
                 background: grey;
                 border-radius: 5px;
             }
            QScrollBar::add-line:vertical {
            height: 0px;
            }

            QScrollBar::sub-line:vertical {
            height: 0px;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            height: 0px;
            }
        """


    def AboutDialog(self):
        AboutDialog = QDialog(self.parent)
        AboutDialog.setWindowTitle("About MhlFileVerify")
        AboutDialog.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        AboutDialog.setFixedSize(480, 480)
        AboutDialog.setStyleSheet(common_style)
        layout = QVBoxLayout(AboutDialog)
        top_layout = QHBoxLayout()
        logo_app = QPixmap("../share/icons/app_logo_128x128.png")
        logo_label = QLabel()
        logo_label.setPixmap(logo_app)
        top_layout.addWidget(logo_label, alignment=Qt.AlignCenter)
        
        version_label = QLabel(f"""Version: {version_MhlFileVerify}
Developer: Víctor Zamora

More info:
batikstudio.com
info@batikstudio.com""")
        version_label.setWordWrap(True)
        top_layout.addWidget(version_label)
        
        layout.addLayout(top_layout)
        
        licenses_browser = QTextBrowser()
        licenses_browser.setVerticalScrollBar(QScrollBar())
        with open("../share/doc/about_licenses.txt", "r") as f:
            file_about_licenses = f.read()
            licenses_browser.setPlainText(file_about_licenses)
        layout.addWidget(licenses_browser)
        
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(AboutDialog.accept)
        layout.addWidget(ok_button, alignment=Qt.AlignCenter)
        return AboutDialog

    def CustomSuccessDialog(self, title, description, detailed_text):

        SuccessDialog = QDialog(self.parent)
        SuccessDialog.setWindowTitle(title)
        SuccessDialog.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  # Removes help button
        SuccessDialog.setFixedSize(480, 480)
        SuccessDialog.setStyleSheet(common_style)
        layout = QVBoxLayout(SuccessDialog)
        top_layout = QHBoxLayout()
        icon = QPixmap("../share/icons/success.png")
        icon_label = QLabel()
        icon_label.setPixmap(icon)
        top_layout.addWidget(icon_label, 1, alignment=Qt.AlignCenter)
        shortDescription = QLabel(description)
        shortDescription.setWordWrap(True)
        top_layout.addWidget(shortDescription, 2)
        layout.addLayout(top_layout)
        layout.addItem(QSpacerItem(5, 10))
        detailedDescription = QTextBrowser()
        detailedDescription.setVerticalScrollBar(QScrollBar())
        detailedDescription.setPlainText(detailed_text)
        layout.addWidget(detailedDescription)
        
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(SuccessDialog.accept)
        layout.addWidget(ok_button, alignment=Qt.AlignCenter)
        SuccessDialog.exec()

    def CustomErrorDialog(self, title, description, detailed_text):

        ErrorDialog = QDialog(self.parent)
        ErrorDialog.setWindowTitle(title)
        ErrorDialog.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  # Removes help button
        ErrorDialog.setFixedSize(480, 480)
        ErrorDialog.setStyleSheet(common_style)
        layout = QVBoxLayout(ErrorDialog)
        top_layout = QHBoxLayout()
        icon = QPixmap("../share/icons/error.png")
        icon_label = QLabel()
        icon_label.setPixmap(icon)
        top_layout.addWidget(icon_label, 1, alignment=Qt.AlignCenter)
        shortDescription = QLabel(description)
        shortDescription.setWordWrap(True)
        top_layout.addWidget(shortDescription, 2)
        layout.addLayout(top_layout)
        layout.addItem(QSpacerItem(5, 10))
        detailedDescription = QTextBrowser()
        detailedDescription.setVerticalScrollBar(QScrollBar())
        detailedDescription.setPlainText(detailed_text)
        layout.addWidget(detailedDescription)
        
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(ErrorDialog.accept)
        layout.addWidget(ok_button, alignment=Qt.AlignCenter)
        ErrorDialog.exec()
