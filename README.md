# Winstaller

Winstaller is a one-click Linux software installer that supports various package formats. It allows you to install packages with a simple right-click action using the "Open With" context menu.

## Features

- Supports the following package formats:
  - `.deb`
  - `.rpm`
  - `.pkg.tar.xz`
  - `.snap`
  - `.flatpak`
  - `.appimage`
  - `.sh`
  - `.bash`
  - `.run`
  - `.bin`
  - `.tar`
  - `.gz`
  - `.bz2`
  - `.xz`
  - `.tgz`
  - `.tbz2`
  - `.txz`
  - `.zip`
  - `.7z`
- Easy to use with a right-click context menu integration.

## Installation

To install Winstaller, follow these steps:

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/winstaller.git
   cd winstaller
## Run the installation script:

chmod +x install.sh
sudo ./install.sh

Usage
Right-click on any supported package file.
Select "Open With" and then choose "Winstaller".
Winstaller will automatically detect the package format and proceed with the installation.

Uninstallation
To uninstall Winstaller, follow these steps:

Remove the installed files:

sudo rm /usr/local/bin/winstaller.py
sudo rm /usr/local/bin/winstaller.sh
sudo rm /usr/share/applications/winstaller.desktop

Update the desktop database:

sudo update-desktop-database

Contributing
If you would like to contribute to Winstaller, please fork the repository and submit a pull request. Contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Author
Developed by WalidDeveloper.com.


This `README.md` provides instructions for downloading, installing, and uninstalling Winstaller, along with other relevant information. Make sure to replace `Walid-Developer` with your actual GitHub username in the clone URL.
