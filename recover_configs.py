import os
import shutil

def recover_configs():
    # Get desktop directory path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Configuration of files to replace with their destination paths
    files_to_replace = [
        {
            "source": os.path.join(desktop_path, "uServeService.exe.config"),
            "destination": r"C:\uServePro\Server"
        },
        {
            "source": os.path.join(desktop_path, "config.json"),
            "destination": r"C:\uServePro\Server\www\assets"
        },
        {
            "source": os.path.join(desktop_path, "config.ini"),
            "destination": r"C:\uServePro\App"
        }
    ]

    # List to track successfully replaced files
    successfully_replaced_files = []

    for file_config in files_to_replace:
        try:
            source_file = file_config["source"]
            destination_path = file_config["destination"]

            # Check if source file exists
            if not os.path.exists(source_file):
                print(f"Source file does not exist: {source_file}")
                continue

            # Ensure destination path exists
            os.makedirs(destination_path, exist_ok=True)

            # Get destination file path
            destination_file = os.path.join(destination_path, os.path.basename(source_file))

            # Replace file
            shutil.copy2(source_file, destination_file)
            print(f"File successfully replaced at: {destination_file}")
            
            # Record successfully replaced file
            successfully_replaced_files.append(source_file)

        except PermissionError:
            print(f"Insufficient permissions to replace file: {source_file}")
        except Exception as e:
            print(f"Error replacing {source_file}: {e}")

    # Delete successfully replaced files
    for file in successfully_replaced_files:
        try:
            os.remove(file)
            print(f"Deleted file: {file}")
        except Exception as e:
            print(f"Error deleting file {file}: {e}")

'''
if __name__ == "__main__":
    replace_file_in_c_drive()
'''