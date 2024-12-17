import os
import shutil
import rarfile

# Specify the path to unrar and rar executables
rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\unrar.exe"
rarfile.RAR_TOOL = r"C:\Program Files\WinRAR\rar.exe"

# Set folder paths
downloads_path = os.path.expanduser("~/Downloads")
desktop_path = os.path.expanduser("~/Desktop")
final_folder_name = "uServePro"  # 最终的文件夹名称
d_drive_target = r"D:\uServePro"  # D盘的目标路径

# Find .rar files starting with "uServePro"
files = [f for f in os.listdir(downloads_path) if f.startswith("uServePro") and f.endswith(".rar")]

if not files:
    print("未找到以 'uServePro' 开头的 .rar 文件！")
else:
    print(f"找到文件: {files[0]}")

    try:
        # Full path to the .rar file
        rar_file = os.path.join(downloads_path, files[0])
        
        # Temporary extraction directory
        temp_extract_dir = os.path.join(desktop_path, "temp_extracted")
        if not os.path.exists(temp_extract_dir):
            os.makedirs(temp_extract_dir)
        
        # Extract the .rar file
        with rarfile.RarFile(rar_file, 'r') as rar_ref:
            rar_ref.extractall(temp_extract_dir)
        
        # Handle extracted content
        extracted_items = os.listdir(temp_extract_dir)
        if len(extracted_items) == 1 and os.path.isdir(os.path.join(temp_extract_dir, extracted_items[0])):
            # If a single folder exists, rename it directly
            extracted_folder = os.path.join(temp_extract_dir, extracted_items[0])
        else:
            # If multiple items exist, treat temp_extract_dir as the folder
            extracted_folder = temp_extract_dir

        # Final target folder on Desktop
        final_path = os.path.join(desktop_path, final_folder_name)
        
        # Remove existing folder with the same name, if exists
        if os.path.exists(final_path):
            shutil.rmtree(final_path)
        
        # Rename or move extracted folder to the final name
        shutil.move(extracted_folder, final_path)
        
        # Cleanup temporary directory if it was not renamed
        if os.path.exists(temp_extract_dir):
            os.rmdir(temp_extract_dir)

        # Handle D drive target
        if os.path.exists(d_drive_target):
            shutil.rmtree(d_drive_target)  # Remove the old folder if it exists
            print(f"已删除 D 盘中旧文件夹: {d_drive_target}")
        
        # Copy to D drive
        shutil.copytree(final_path, d_drive_target)
        print(f"文件已成功拷贝至 D 盘: {d_drive_target}")
        
        # Delete the renamed folder on Desktop
        shutil.rmtree(final_path)
        print(f"桌面上的文件夹已删除: {final_path}")
        
    except rarfile.BadRarFile:
        print("无法读取 .rar 文件，请检查文件是否损坏或路径是否正确！")
    except Exception as e:
        print(f"解压或拷贝过程中发生错误: {e}")
