import argparse
import subprocess
import os
import shutil

def install_deb(package_path):
    try:
        subprocess.run(["sudo", "dpkg", "-i", package_path], check=True)
        subprocess.run(["sudo", "apt-get", "install", "-f"], check=True)
        print("Installed .deb package successfully. - WalidDeveloper.com")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install .deb package: {e} - WalidDeveloper.com")

def install_rpm(package_path):
    try:
        subprocess.run(["sudo", "rpm", "-i", package_path], check=True)
        print("Installed .rpm package successfully. - WalidDeveloper.com")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install .rpm package: {e} - WalidDeveloper.com")

def install_snap(package_name):
    try:
        subprocess.run(["sudo", "snap", "install", package_name], check=True)
        print("Installed snap package successfully. - WalidDeveloper.com")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install snap package: {e} - WalidDeveloper.com")

def install_flatpak(package_name):
    try:
        subprocess.run(["flatpak", "install", package_name, "-y"], check=True)
        print("Installed flatpak package successfully. - WalidDeveloper.com")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install flatpak package: {e} - WalidDeveloper.com")

def install_appimage(package_path):
    try:
        os.chmod(package_path, 0o755)
        subprocess.run([package_path], check=True)
        print("Ran AppImage successfully. - WalidDeveloper.com")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run AppImage: {e} - WalidDeveloper.com")

def install_script(package_path):
    try:
        os.chmod(package_path, 0o755)
        subprocess.run([package_path], check=True)
        print(f"Ran script {package_path} successfully. - WalidDeveloper.com")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run script {package_path}: {e} - WalidDeveloper.com")

def install_tar(package_path):
    try:
        dir_path = "/tmp/install_dir"
        os.makedirs(dir_path, exist_ok=True)
        shutil.unpack_archive(package_path, dir_path)
        print(f"Unpacked {package_path} to {dir_path}. - WalidDeveloper.com")
    except Exception as e:
        print(f"Failed to unpack tar archive: {e} - WalidDeveloper.com")

def install_zip(package_path):
    try:
        dir_path = "/tmp/install_dir"
        os.makedirs(dir_path, exist_ok=True)
        subprocess.run(["unzip", package_path, "-d", dir_path], check=True)
        print(f"Unpacked {package_path} to {dir_path}. - WalidDeveloper.com")
    except subprocess.CalledProcessError as e:
        print(f"Failed to unzip archive: {e} - WalidDeveloper.com")

def install_package(package_path):
    if package_path.endswith(".deb"):
        install_deb(package_path)
    elif package_path.endswith(".rpm"):
        install_rpm(package_path)
    elif package_path.endswith(".snap"):
        install_snap(package_path)
    elif package_path.endswith(".flatpak"):
        install_flatpak(package_path)
    elif package_path.endswith(".AppImage"):
        install_appimage(package_path)
    elif package_path.endswith((".sh", ".bash", ".run", ".bin")):
        install_script(package_path)
    elif package_path.endswith((".tar", ".gz", ".bz2", ".xz", ".tgz", ".tbz2", ".txz")):
        install_tar(package_path)
    elif package_path.endswith(".zip"):
        install_zip(package_path)
    else:
        print(f"Unsupported package format: {package_path} - WalidDeveloper.com")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='One-click Linux software installer by WalidDeveloper.com.')
    parser.add_argument('package', type=str, help='Path to the package to install')
    args = parser.parse_args()
    install_package(args.package)
