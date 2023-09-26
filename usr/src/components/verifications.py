# Verifications
import os
import sys
import ctypes
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QStatusBar


class initialVerifications:
    
    libcrypto_lib = "libcrypto.so.3"
    #libcrypto_lib = "libcrypto.so.1.0.0"
    mhltool_bin = "../bin/mhl"
    
    def __init__(self, parent):
        self.parent = parent
        
    def verify_libs(self, library_name):
        try:
            # Try load the shared lib
            ctypes.CDLL(library_name)
            print(f"Library {library_name} found.")
        except OSError:
            QMessageBox.critical(self.parent.window, "Error", f"{library_name} not found")
            self.parent.set_status_message(f"{library_name} tool not detected")

    def verify_mhltool_installed(self, mhlbin):
        
        if os.path.exists(mhlbin):
            print(f"Mhl tool was found")
        else:
            mhltool_error = f"Mhl tool {mhlbin} couldn't be found.."
            QMessageBox.critical(self.parent.window, "Error", mhltool_error)
            self.parent.set_status_message("mhl tool not detected")

