# MhlFileVerify

Mhl File Verify for Linux is a tool written in Python and Qt to verify and seal data according to the implementation of the MHL standard.

This tool is useful to verify backups created from other tools such as Davinci Resolve Clone tool, which generates a mhl file during the copy process with file hashes (md5).

Data Wranglers and DIT's can verify video data in Linux Systems.

This software is based on and includes the original [mhl-tool](https://github.com/pomfort/mhl-tool) by Pomfort.

<img src="https://batikstudio.com/mhlfileverify/screenshot.png" title="" alt="" data-align="center">

## Features

- Verify mhl files

- Create mhl files from selected dir (Seal)

- Drag and drop files or dirs

- Choose the checksum type (MD5 and SHA1)

- Built in Linux / OSX mhl-tool binaries

## System requeriments

- Python3

- Pyside6

- Libcrypto3 to run mhl-tool in Linux

## Appimage version

Data Management can be a task which requires an high level of safety. By this reason, you may need an external tool like this to work on any linux system. So, we think a portable tool can be useful and to do this, and AppImage format is perfect.

This app is distributed as Appimage format. It has been tested on Ubuntu 22.04, Linux Mint and MxLinux. Other systems like like Rocky Linux 8 / Red Hat are not supponted currently due to the old GLIB version. However, you could make it work from source code if you install Pyside6.

## MacOS

MhlFileVerify app works on OSX as well. You can download app DMGs or run from source. If you run it from source, the platform is autodetected on boot and the correct mhltool binary will be selected. If you prefer use command line tool from pomfort, you can download from their [website](https://pomfort.com/downloads/).

From terminal:

- Install python3

- Install pySide6
  
  ```
  python3 -m pip install --upgrade pip --user
  python3 -m pip install pyside6
  ```

- Run main script from /src
  
  `python3 main.py`

## Known Issues

- From ISO / UDF volumes, the seal process is incorrect.
  
  

## Changelog

#### v.04

- Fixes for MacOS support

- Added new compiled binary mhl-tool ARM for Apple Sillicon

- New custom dialogs to manage errors and information

- First DMG app MacOS version

#### v0.3

- Added initial suppor for OSX intel based

- Added OS detection

- Added OSX mhl-tool binary

- Added status messages while the data is being verified

#### v0.2

- Changed the GUI to QT/Pyside

- Added new seal tab to create mhl files

- Added support Drag and Drop files and folders

- Added status bar messages

- Added error dialogs

- First version in Appimage

#### v0.1

- Initial GUI design in Tkinter

- Added new compilated binary of mhl-tool to current Linux distros which use libcrypto3

- Basic features to verify mhl files only

[BatikStudio](https://batikstudio.com) Home Page
