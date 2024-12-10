import os
import subprocess
from datetime import datetime

def export_mysql():
    # Database connection details
    host = "127.0.0.1"  # Database host
    port = "3308"       # Database port
    user = "root"       # Database username
    password = "123456" # Database password

    # Get the current date for naming the backup file
    current_date = datetime.now()

    try:
        # Automatically get the current user's desktop path
        username = os.getlogin()
        filename = current_date.strftime("%Y%m%d")  # Format the filename as YYYYMMDD
        # Define the path to save the backup file on the desktop
        desktop_path = os.path.join("C:\\Users", username, "Desktop", f"{filename}_backup.sql")

        command = [
            "C:\\Program Files\\MySQL\\MySQL Workbench 8.0 CE\\mysqldump",  # Path to mysqldump tool 
            f"--host={host}",
            f"--port={port}",
            f"--user={user}",
            f"--password={password}",
            "--databases",  
            "userve",      
            "--result-file", desktop_path,  
            "--single-transaction", 
            "--add-drop-database",  # Adds a command to drop the database before creating it
            "--add-drop-table"      # Adds a command to drop tables before creating them
        ]

        # Execute the command and capture the result
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            print("Database exported successfully")
        else:
            print(f"Error during export: {result.stderr}")

    except Exception as e:
        print(f"An error occurred: {e}")

'''
if __name__ == "__main__":
    export_mysql()
'''