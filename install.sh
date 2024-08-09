#!/bin/bash

# Install directories
INSTALL_DIR="/usr/local/bin"
DESKTOP_FILE_DIR="/usr/share/applications"

# Copy the scripts
sudo cp winstaller.py $INSTALL_DIR/winstaller.py
sudo cp winstaller.sh $INSTALL_DIR/winstaller.sh

# Make the shell script executable
sudo chmod +x $INSTALL_DIR/winstaller.sh

# Create the .desktop file
sudo cp winstaller.desktop $DESKTOP_FILE_DIR/winstaller.desktop

# Update desktop database
sudo update-desktop-database

echo "Winstaller has been installed successfully."
