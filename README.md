# MhlToolVerify

Mhl File Verify for Linux is a tool written in Python and Qt to verify and seal data according to the implementation of the MHL standard.

This tool is useful to verify backups created from other tools such as Davinci Resolve Clone tool, which generates a mhl file during the copy with file hashes (md5).

Data Wranglers (DIT's) can verify video data in Linux Systems.

This software is based on and includes the original mhl-tool by Pomfort.

<img src="https://batikstudio.com/mhlfileverify/screenshot.png" title="" alt="" data-align="center">

## Features

- Verify mhl files

- Create mhl files from selected dir (Seal)

- Drag and drop files or dirs

- Choose the checksum type (MD5 and SHA1)

- Built in mhl-tool

## System requeriments

- Python3

- Pyside6

- Libcrypto3 to run mhl-tool

## Appimage version

Data Management can be a task which requires an high level of safety. By this reason, you may need an external tool like this to work on any linux system. So, we think a portable tool can be useful and to do this, and AppImage format is perfect.

This app is distributed as Appimage format. It has been tested on Ubuntu 22.04, Linux Mint and MxLinux. Other systems like like Rocky Linux 8 / Red Hat are not supponted currently due to the old GLIB version. However, you could make it work from source code if you install Pyside6.


