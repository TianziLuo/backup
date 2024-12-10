import shutil
import os

def copy_configs():
    # Set the source file paths
    app_path = r"C:\uServePro\App\config.ini"
    service_file_path = r"C:\uServePro\Server\uServeService.exe.config"
    www_path = r"C:\uServePro\Server\www\assets\config.json"

    # Get the current user's desktop path
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')

    # List of files to copy
    files_to_copy = [app_path, service_file_path, www_path]

    # Loop through the list of files and copy them to the desktop
    for file_path in files_to_copy:
        try:
            # Get the file name (keep the original file name)
            file_name = os.path.basename(file_path)
            destination = os.path.join(desktop_path, file_name)  # Set the destination file path

            # Copy the file to the desktop
            shutil.copy(file_path, destination)
            print(f"File successfully copied to desktop: {destination}")
        except Exception as e:
            print(f"Failed to copy file {file_path}: {e}")
            
'''
if __name__ == "__main__":
    copy_configs()
'''