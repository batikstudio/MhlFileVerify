#! /usr/bin/env python3
import subprocess
import os
import sys
from components.verify_tab import verify_tab_class
from components.seal_tab import seal_tab_class
from components.dialogs import dialogs
from components.SharedClasses import ConfigFile

from components.verifications import initialVerifications
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView, QComboBox, QWidget,
    QMainWindow, QMenu, QMenuBar, QPushButton, QTabWidget,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget, QFileDialog, QMessageBox)
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QFile, QResource, QEvent)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QDragEnterEvent, QDropEvent, QFontDatabase)


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = "./components/main.ui"
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        self.window.setAcceptDrops(True)
        self.window.show()
        self.verifyTab = verify_tab_class(self) # Pass the main window as a parent
        self.sealTab = seal_tab_class(self) # Pass the main window as a parent
        self.dialogsClass = dialogs(self) # Pass the main window as a parent
        
        icon_mhl_file_label = self.window.icon_mhl_file_label
        icon_mhl_file_label.installEventFilter(self)
        icon_seal_dir = self.window.icon_drive
        icon_seal_dir.installEventFilter(self)


    def menu_actions(self):
        print("Actions loaded")
        action_Quit = self.window.actionQuit
        action_Quit.triggered.connect(QCoreApplication.quit)
        action_Open_file_mhl = self.window.actionOpen_mhl_file
        action_Open_file_mhl.triggered.connect(appVerifyMhl.select_mhl_file)
        action_verify = self.window.actionVerify
        action_verify.triggered.connect(appVerifyMhl.verify_mhl_file)
        action_create_mhl_file = self.window.actionCreate_mhl_file
        action_create_mhl_file.triggered.connect(appSeal.launch_seal)
        action_about = self.window.actionAbout
        action_about.triggered.connect(dialogsInstance.AboutDialog)
        action_shortcuts = self.window.actionShortcuts
        action_shortcuts.triggered.connect(dialogsInstance.ShortcutsDialog)


    def buttons_verify_tab(self):
        print("Buttons loaded")
        select_open_mhlFile_button = self.window.button_open_file
        select_open_mhlFile_button.clicked.connect(appVerifyMhl.select_mhl_file)
        verify_button = self.window.button_verify
        verify_button.clicked.connect(appVerifyMhl.verify_mhl_file)
        seal_button_choose_dir = self.window.button_choose_dir
        seal_button_choose_dir.clicked.connect(appSeal.select_dir_seal)
        seal_button_create = self.window.button_create
        seal_button_create.clicked.connect(appSeal.launch_seal)

    def set_status_message(self, message):
        self.window.statusBar().showMessage(message)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.DragEnter:
            self.dragEnterEvent(event)
        elif event.type() == QEvent.Drop:
            if obj == self.window.icon_mhl_file_label:
                self.dropEvent_verify(event)
            elif obj == self.window.icon_drive:
                self.dropEvent_seal(event)
        elif event.type() == QEvent.DragMove:
            self.dragMoveEvent(event)
        return super().eventFilter(obj, event)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent_verify(self, event):
        print("New file dropped")
        if event.mimeData().hasUrls():
            dropped_file = event.mimeData().urls()[0].toLocalFile()
            if os.path.isfile(dropped_file):
                line_edit_file = self.window.line_edit_file
                line_edit_file.setText(event.mimeData().urls()[0].toLocalFile())
            elif os.path.isdir(dropped_file):
                QMessageBox.critical(self.window,"Wrong selection", "Directories are not allowed. Please, select a valid MHL file.")
            else:
                QMessageBox.critical(self.window,"Wrong selection", "Please, select a valid MHL file.")


    def dropEvent_seal(self, event):
        print("New file dropped")
        if event.mimeData().hasUrls():
            dropped_file = event.mimeData().urls()[0].toLocalFile()
            if os.path.isdir(dropped_file):
                dir_to_seal = self.window.line_edit_directory
                dir_to_seal.setText(event.mimeData().urls()[0].toLocalFile())
            elif os.path.isfile(dropped_file):
                QMessageBox.critical(self.window,"Wrong selection", "Files are not allowed. Please, select a valid directory.")
            else:
                QMessageBox.critical(self.window,"Wrong selection", "Please, select a valid directory.")


    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super().dragMoveEvent(event)

    def load_fonts(self):
        # To find real name of a font "fc-scan OpenSans-SemiBold.ttf"
        print("Fonts Loaded")
        QFontDatabase.addApplicationFont('../share/fonts/OpenSans-Regular.ttf')
        QFontDatabase.addApplicationFont('../share/fonts/OpenSans-Light.ttf')
        QFontDatabase.addApplicationFont('../share/fonts/OpenSans-SemiBold.ttf')

if __name__ == "__main__":
    app = QApplication([])
    application = Mainwindow()
    application.load_fonts()
    ConfigFile.verify_config_file()
    appInitialVerifications = initialVerifications(application)
    appInitialVerifications.verify_mhltool_installed(appInitialVerifications.mhltool_bin)
    appInitialVerifications.verify_libs(appInitialVerifications.libcrypto_lib)
    appVerifyMhl = verify_tab_class(application) # To MainWindow instance
    appSeal = seal_tab_class(application)
    dialogsInstance = dialogs(application)
    application.menu_actions()
    application.buttons_verify_tab()
    app.exec()
