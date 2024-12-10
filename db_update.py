import os
def db_update():
    # File path for the input
    input_file_path = r"C:\uServePro\Server\DB_Update.txt"

    # Get the current user's desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file_path = os.path.join(desktop_path, "db_update_filtered.sql")

    # Get the user input for the target year and month (yyyymm format)
    yyyymm = input("Please enter the target yyyymm (e.g., 202411): ").strip()

    # Validate the input format
    if not yyyymm.isdigit() or len(yyyymm) != 6:
        print("Invalid year-month format. Please enter a 6-digit number like '202411'.")
    else:
        # Construct the search keyword
        keyword = f"-- {yyyymm}"

        try:
            # Open the input file and read all lines
            with open(input_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Find the position of the first occurrence of the keyword
            start_index = next((index for index, line in enumerate(lines) if keyword in line), None)

            if start_index is not None:
                # Extract all lines starting from the first occurrence of the keyword
                filtered_lines = lines[start_index:]
                
                # Write the filtered lines to the output .sql file
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.writelines(filtered_lines)

                print(f"Successfully generated the filtered SQL file: {output_file_path}")
            else:
                print(f"Keyword '{keyword}' not found in the file.")

        except FileNotFoundError:
            print(f"File not found: {input_file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

'''
if __name__ == "__main__":
    db_update()
'''