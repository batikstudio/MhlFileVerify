# Verifications
import os
import platform
import sys
import ctypes
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QStatusBar

mhltool_bin = ""
os_name = platform.system()


class initialVerifications:

    def __init__(self, parent):
        self.parent = parent
        self.libcrypto_lib = "libcrypto.so.3"
        
        
    def platform_detection(self):
        global mhltool_bin
        if os_name == "Linux":
            print("- Linux detected")
            mhltool_bin = "../bin/mhl_linux_x64"
            print("- Selected bin ", mhltool_bin)
        elif os_name == "Darwin":
            print("- OSX Detected")
            mhltool_bin = "../bin/mhl_osx_x64"

        
    def verify_libs(self, library_name):
        if os_name == "Linux":
            print("- Searching Linux libraries")
            try:
                # Try load the shared lib
                ctypes.CDLL(library_name)
                print(f"- Library {library_name} found.")
            except OSError:
                QMessageBox.critical(self.parent.window, "Error", f"{library_name} not found")
                self.parent.set_status_message(f"{library_name} tool not detected")
        elif os_name == "Darwin":
            print("- OSX no needs external libraries")
        
    def verify_mhltool_installed(self):
        
        if os.path.exists(mhltool_bin):
            print(f"- Mhl tool binary was found")
        else:
            mhltool_error = f"- Mhl tool {mhltool_bin} couldn't be found.."
            QMessageBox.critical(self.parent.window, "Error", mhltool_error)
            self.parent.set_status_message("mhl tool binary not detected")

